import os
import re
import json
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from groq import AsyncGroq

load_dotenv()

app = FastAPI(title="Learning Material Generator", version="1.0.0")

client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))


class GenerateRequest(BaseModel):
    topik: str = Field(..., min_length=3, description="Topik materi pembelajaran")
    tingkat_kesulitan: str = Field("pemula", description="pemula | menengah | lanjutan")
    durasi_menit: int = Field(60, ge=5, le=240, description="Durasi dalam menit")


# PROMPT A sederhana, hanya Task
# SYSTEM_PROMPT_A = """
# Buat materi pembelajaran tentang {topik}.
# """

# PROMPT B Role + Task + Context
# SYSTEM_PROMPT_B = """
# Anda adalah pembuat materi pembelajaran ahli.
#
# Tugas Anda adalah membuat materi pembelajaran tentang {topik}.
#
# Konteks: Materi pembelajaran ini akan digunakan oleh peserta didik atau pemula yang ingin memahami sebuah topik secara sistematis. Output akan digunakan sebagai referensi pembelajaran mandiri atau bahan ajar.
# """

# PROMPT C Role + Task + Context + Constraint + Output Format
SYSTEM_PROMPT = """
Anda adalah pembuat materi pembelajaran ahli yang berpengalaman dalam merancang kurikulum dan modul ajar untuk berbagai tingkat pemula.

Tugas Anda adalah membuat materi pembelajaran yang lengkap dan terstruktur berdasarkan topik, tingkat kesulitan, dan durasi waktu yang diberikan oleh pengguna.

Konteks: Materi pembelajaran ini akan digunakan oleh peserta didik atau pemula yang ingin memahami sebuah topik secara sistematis. Output akan digunakan sebagai referensi pembelajaran mandiri atau bahan ajar.

Batasan:
- Output HARUS berupa JSON valid dan tidak boleh menyertakan teks apa pun di luar JSON.
- Jangan sertakan markdown code block (```json ... ```).
- Semua field wajib diisi, tidak boleh kosong atau null.
- Field kuis minimal berisi 3 soal.
- Semua konten harus dalam bahasa Indonesia.
- Sesuaikan jumlah dan panjang isi dengan durasi_menit: durasi kurang dari 15 menit = ringkasan maksimal 3 kalimat, 3 poin penting, dan 3 soal kuis; durasi 15 sampai 60 menit = 5 poin penting dan 4 soal kuis; durasi lebih dari 60 menit = boleh lebih lengkap.
- Jawaban kuis harus bervariasi (A, B, C, dan D), tidak boleh semuanya sama.
- estimasi_durasi_menit WAJIB sama persis dengan durasi_menit pada input.

Format Output (JSON):
{
  "topik": "string",
  "tingkat_kesulitan": "string",
  "tujuan_pembelajaran": ["string", "string", "string"],
  "ringkasan_materi": "string",
  "poin_penting": ["string", "string", "string"],
  "kuis": [
    {
      "pertanyaan": "string",
      "opsi_a": "string",
      "opsi_b": "string",
      "opsi_c": "string",
      "opsi_d": "string",
      "jawaban_benar": "A | B | C | D",
      "penjelasan": "string"
    }
  ],
  "saran_sumber_belajar": ["string", "string"],
  "estimasi_durasi_menit": integer
}
"""


def bersihkan_json_dari_llm(teks: str) -> str:
    teks = re.sub(r"```json\s*", "", teks)
    teks = re.sub(r"```\s*$", "", teks)
    teks = teks.strip()

    start = teks.find("{")
    if start == -1:
        return teks

    depth = 0
    for i in range(start, len(teks)):
        if teks[i] == "{":
            depth += 1
        elif teks[i] == "}":
            depth -= 1
            if depth == 0:
                return teks[start : i + 1]

    end = teks.rfind("}")
    if end != -1 and end > start:
        return teks[start : end + 1]

    return teks


@app.get("/")
def home():
    return {
        "message": "Learning Material Generator API is running",
        "endpoint": "POST /generate",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health():
    return {"status": "healthy", "service": "learning-material-generator"}


@app.post("/generate")
async def generate_material(request: GenerateRequest):
    try:
        user_prompt = f"""
Topik: {request.topik}
Tingkat Kesulitan: {request.tingkat_kesulitan}
Durasi: {request.durasi_menit} menit

Buatlah materi pembelajaran sesuai dengan format JSON yang ditentukan di system prompt.
"""

        system_prompt = SYSTEM_PROMPT.replace("{topik}", request.topik)

        response = await client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
            max_tokens=2000,
        )

        content = response.choices[0].message.content

        json_str = bersihkan_json_dari_llm(content)
        try:
            result = json.loads(json_str)
        except json.JSONDecodeError:
            raise HTTPException(
                status_code=502,
                detail="Gagal memparsing respons LLM ke dalam JSON yang valid."
            )

        if result.get("estimasi_durasi_menit") != request.durasi_menit:
            raise HTTPException(
                status_code=502,
                detail="estimasi_durasi_menit tidak sesuai dengan durasi_menit pada input."
            )

        if not isinstance(result.get("kuis"), list) or len(result["kuis"]) < 3:
            raise HTTPException(
                status_code=502,
                detail="Field kuis harus berisi minimal 3 soal."
            )

        return result

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Terjadi kesalahan saat menghubungi LLM: {str(e)}"
        )
