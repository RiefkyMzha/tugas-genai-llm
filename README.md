# GenAI Application

## Project Information

**Nama Project:** Learning Material Generator

**Use Case:** Generator materi pembelajaran otomatis berbasis Generative AI

**Deskripsi Singkat:** Aplikasi FastAPI yang menerima input topik pembelajaran, tingkat kesulitan, dan durasi waktu, lalu menghasilkan materi pembelajaran terstruktur dalam bentuk JSON menggunakan LLM Groq. Output mencsayap tujuan pembelajaran, ringkasan materi, poin penting, kuis, dan saran sumber belajar.

------------------------------------------------------

## Tech Stack

- Python 3.14
- FastAPI
- Pydantic
- Groq (LLM API)
- python-dotenv
- Uvicorn

------------------------------------------------------

## Application Flow
User Input
↓
FastAPI (POST /generate)
↓
LLM API (Groq)
↓
Structured Output (JSON)

Penjelasan: User mengirim data input (topik, tingkat kesulitan, durasi) melalui endpoint `POST /generate`. FastAPI memvalidasi request menggunakan Pydantic model, kemudian mengirim input bersama system prompt ke Groq LLM. LLM menghasilkan materi pembelajaran dalam format JSON yang sudah ditentukan, lalu FastAPI mengembalikannya sebagai response terstruktur ke user.

------------------------------------------------------

## API Endpoint

Endpoint kalian:
POST /generate

Endpoint tambahan:
- `GET /` — informasi API
- `GET /health` — health check

------------------------------------------------------

## Example Request

{
  "topik": "Pengenalan Kecerdasan Buatan",
  "tingkat_kesulitan": "pemula",
  "durasi_menit": 60
}

------------------------------------------------------

## Example Response

{
  "topik": "Pengenalan Kecerdasan Buatan",
  "tingkat_kesulitan": "pemula",
  "tujuan_pembelajaran": [
    "Memahami definisi dan ruang lingkup kecerdasan buatan (AI)",
    "Mengenali contoh penerapan AI dalam kehidupan sehari-hari",
    "Menjelaskan konsep dasar pembelajaran mesin (machine learning) sebagai bagian dari AI"
  ],
  "ringkasan_materi": "Materi ini memberikan gambaran umum tentang kecerdasan buatan, mulai dari definisi, sejarah singkat, hingga contoh aplikasi nyata di berbagai bidang seperti kesehatan, transportasi, dan hiburan. Selain itu, peserta akan diperkenalkan pada konsep dasar pembelajaran mesin, perbedaan antara AI, machine learning, dan deep learning, serta tantangan etika yang terkait dengan penggunaan AI.",
  "poin_penting": [
    "AI adalah bidang ilmu komputer yang berusaha menciptakan sistem yang dapat meniru perilaku manusia dalam memecahkan masalah.",
    "Pembelajaran mesin adalah teknik utama AI yang memungkinkan komputer belajar dari data tanpa diprogram secara eksplisit.",
    "Contoh aplikasi AI meliputi asisten virtual, rekomendasi produk, deteksi penipuan, dan mobil otonom.",
    "Deep learning adalah sub‑tipe pembelajaran mesin yang menggunakan jaringan saraf tiruan dengan banyak lapisan.",
    "Isu etika AI meliputi privasi data, bias algoritma, dan dampak otomatisasi pada tenaga kerja."
  ],
  "kuis": [
    {
      "pertanyaan": "Apa yang dimaksud dengan kecerdasan buatan (AI)?",
      "opsi_a": "Sebuah program yang dapat melakukan perhitungan matematika cepat",
      "opsi_b": "Sistem komputer yang meniru perilaku manusia dalam menyelesaikan tugas",
      "opsi_c": "Hardware khusus untuk mempercepat proses komputasi",
      "opsi_d": "Jaringan internet yang menghubungkan banyak komputer",
      "jawaban_benar": "B",
      "penjelasan": "AI adalah bidang yang berfokus pada pembuatan sistem yang dapat meniru cara berpikir, belajar, dan memecahkan masalah seperti manusia."
    },
    {
      "pertanyaan": "Manakah contoh aplikasi pembelajaran mesin (machine learning) yang paling tepat?",
      "opsi_a": "Pemutar musik MP3",
      "opsi_b": "Sistem rekomendasi film di platform streaming",
      "opsi_c": "Kalkulator sederhana",
      "opsi_d": "Editor teks standar",
      "jawaban_benar": "B",
      "penjelasan": "Sistem rekomendasi film menggunakan data perilaku pengguna untuk mempelajari pola dan memberikan saran yang relevan, yang merupakan contoh utama machine learning."
    },
    {
      "pertanyaan": "Apa perbedaan utama antara machine learning dan deep learning?",
      "opsi_a": "Machine learning menggunakan jaringan saraf, sedangkan deep learning tidak",
      "opsi_b": "Deep learning adalah sub‑tipe machine learning yang menggunakan jaringan saraf dengan banyak lapisan",
      "opsi_c": "Machine learning hanya bekerja pada data teks, sementara deep learning hanya pada gambar",
      "opsi_d": "Tidak ada perbedaan; keduanya istilah yang sama",
      "jawaban_benar": "B",
      "penjelasan": "Deep learning merupakan bagian dari machine learning yang memanfaatkan jaringan saraf tiruan berlapis‑lapis (deep) untuk menangkap representasi data yang lebih kompleks."
    },
    {
      "pertanyaan": "Salah satu tantangan etika dalam penggunaan AI adalah:",
      "opsi_a": "Kecepatan prosesor yang lambat",
      "opsi_b": "Keterbatasan memori komputer",
      "opsi_c": "Bias algoritma yang dapat memperkuat diskriminasi",
      "opsi_d": "Kesulitan dalam menghubungkan kabel jaringan",
      "jawaban_benar": "C",
      "penjelasan": "Bias algoritma muncul ketika data pelatihan mengandung bias, sehingga keputusan AI dapat memperkuat ketidakadilan atau diskriminasi."
    }
  ],
  "saran_sumber_belajar": [
    "Buku: \"Artificial Intelligence: A Modern Approach\" (edisi ringkas) – Bab 1 dan 2",
    "Kursus online gratis: \"AI For Everyone\" oleh Andrew Ng di Coursera"
  ],
  "estimasi_durasi_menit": 60
}

------------------------------------------------------

# Structured Output

Structured output yang digunakan pada aplikasi:
 
{
  "topik": "string",
  "tingkat_kesulitan": "string",
  "tujuan_pembelajaran": ["string"],
  "ringkasan_materi": "string",
  "poin_penting": ["string"],
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
  "saran_sumber_belajar": ["string"],
  "estimasi_durasi_menit": integer
}

### Kenapa kalian memilih field-field tersebut?

Field-field tersebut dipilih sesuai dengan fungsi aplikasi sebagai generator materi pembelajaran:
- `topik` dan `tingkat_kesulitan` untuk mengidentifikasi materi yang dihasilkan.
- `tujuan_pembelajaran` untuk mengetahui capaian pembelajaran yang ingin dicapai.
- `ringkasan_materi` sebagai gambaran umum keseluruhan materi.
- `poin_penting` untuk highlight konsep-konsep kunci yang harus dipahami peserta.
- `kuis` sebagai evaluasi pemahaman dengan format pilihan ganda beserta penjelasan jawaban.
- `saran_sumber_belajar` untuk referensi pembelajaran lebih lanjut.
- `estimasi_durasi_menit` untuk perkiraan waktu yang dibutuhkan dalam mempelajari materi tersebut.
------------------------------------------------------

# Prompt Experiment

Gunakan input yang sama untuk Prompt A, Prompt B, dan Prompt C.

## Input yang Digunakan

{
  "topik": "Pengenalan Kecerdasan Buatan",
  "tingkat_kesulitan": "pemula",
  "durasi_menit": 60
}

------------------------------------------------------

## Prompt A

 
Buat materi pembelajaran tentang {topik}.
 

### Actual Output A

 
{
  "topic": "Pengenalan Kecerdasan Buatan",
  "level": "Pemula",
  "duration_minutes": 60,
  "learning_objectives": [
    "Menjelaskan apa itu Kecerdasan Buatan (AI) secara sederhana.",
    "Membedakan antara AI, Machine Learning, dan Deep Learning.",
    "Menyebutkan contoh aplikasi AI dalam kehidupan sehari-hari.",
    "Memahami konsep dasar data, algoritma, dan model dalam AI.",
    "Mengidentifikasi peluang dan tantangan etika penggunaan AI."
  ],
  "materials_needed": [
    "Proyektor atau layar laptop",
    "Slide presentasi (PDF/PowerPoint)",
    "Video pendek tentang AI (2‑3 menit)",
    "Kartu/kertas sticky notes",
    "Kertas flipchart atau whiteboard",
    "Koneksi internet (opsional untuk demo online)",
    "Kuis singkat (Google Form atau kertas)"
  ],
  "lesson_plan": [
    {
      "segment": 1,
      "time_minutes": 5,
      "title": "Pembukaan & Ice‑breaker",
      "description": "Guru menyapa peserta, memperkenalkan diri, dan menanyakan contoh teknologi yang mereka gunakan setiap hari.",
      "activity": "Polling cepat: ‘Apa yang paling sering Anda gunakan? (Smartphone, GPS, rekomendasi video, dll.)’",
      "resources": [
        "Slide pembuka",
        "Polling tool (Mentimeter/hand‑raise)"
      ]
    },
    {
      "segment": 2,
      "time_minutes": 10,
      "title": "Definisi Kecerdasan Buatan",
      "description": "Penjelasan singkat tentang apa itu AI, mengapa penting, dan sejarah singkat (Dartmouth 1956, AI winter, kebangkitan kembali).",
      "activity": "Diskusi kelompok kecil: ‘Bagaimana AI dapat membantu pekerjaan Anda?’",
      "resources": [
        "Slide definisi AI",
        "Timeline visual"
      ]
    },
    {
      "segment": 3,
      "time_minutes": 10,
      "title": "AI vs Machine Learning vs Deep Learning",
      "description": "Menjelaskan perbedaan tiga istilah utama dengan analogi sederhana (misalnya, resep, koki, dan robot dapur).",
      "activity": "Game kartu: Setiap kartu berisi contoh (AI, ML, DL). Peserta mencocokkan contoh dengan istilah yang tepat.",
      "resources": [
        "Kartu contoh",
        "Slide perbandingan"
      ]
    },
    {
      "segment": 4,
      "time_minutes": 10,
      "title": "Contoh Aplikasi AI dalam Kehidupan Sehari‑hari",
      "description": "Menampilkan video 2‑3 menit tentang AI di asisten virtual, rekomendasi belanja, deteksi wajah, mobil otonom, dll.",
      "activity": "Brainstorm di papan: peserta menuliskan aplikasi AI lain yang mereka ketahui.",
      "resources": [
        "Video contoh AI",
        "Whiteboard/flipchart",
        "Sticky notes"
      ]
    },
    {
      "segment": 5,
      "time_minutes": 10,
      "title": "Komponen Dasar AI: Data, Algoritma, Model",
      "description": "Penjelasan sederhana tentang mengapa data penting, apa itu algoritma, dan bagaimana model “belajar”.",
      "activity": "Simulasi mini: Menggunakan kertas dan spidol, peserta membuat ‘model’ sederhana untuk menebak warna favorit teman berdasarkan data yang diberikan.",
      "resources": [
        "Kertas",
        "Spidol",
        "Contoh dataset sederhana"
      ]
    },
    {
      "segment": 6,
      "time_minutes": 10,
      "title": "Etika & Tantangan AI",
      "description": "Membahas bias data, privasi, dan dampak pekerjaan. Menggunakan studi kasus singkat (mis. sistem rekrutmen yang bias).",
      "activity": "Debat singkat: “Apakah AI harus diatur secara ketat?” – masing‑masing tim berargumen pro atau kontra.",
      "resources": [
        "Studi kasus satu halaman",
        "Timer"
      ]
    },
    {
      "segment": 7,
      "time_minutes": 5,
      "title": "Penutup & Evaluasi",
      "description": "Merangkum poin utama, menjawab pertanyaan, dan melakukan kuis singkat untuk mengukur pemahaman.",
      "activity": "Kuis 5 soal (pilihan ganda) via Google Form atau lembar kertas.",
      "resources": [
        "Kuis",
        "Link Google Form"
      ]
    }
  ],
  "assessment": {
    "type": "Kuis pilihan ganda (5 soal)",
    "passing_score": 70,
    "sample_questions": [
      {
        "question": "Apa singkatan dari AI?",
        "options": [
          "Artificial Intelligence",
          "Automated Interface",
          "Advanced Integration",
          "Artificial Interaction"
        ],
        "answer": "Artificial Intelligence"
      },
      {
        "question": "Manakah contoh aplikasi Machine Learning?",
        "options": [
          "Sistem GPS",
          "Rekomendasi film di platform streaming",
          "Pengatur suhu ruangan otomatis",
          "Pencarian Google"
        ],
        "answer": "Rekomendasi film di platform streaming"
      },
      {
        "question": "Apa perbedaan utama antara Machine Learning dan Deep Learning?",
        "options": [
          "ML menggunakan data kecil, DL menggunakan data besar",
          "ML memerlukan jaringan saraf sederhana, DL menggunakan jaringan saraf dalam",
          "ML tidak memerlukan data, DL memerlukan data",
          "Tidak ada perbedaan"
        ],
        "answer": "ML memerlukan jaringan saraf sederhana, DL menggunakan jaringan saraf dalam"
      },
      {
        "question": "Salah satu tantangan etika AI adalah:",
        "options": [
          "Kecepatan prosesor",
          "Bias data",
          "Warna layar",
          "Ukuran memori"
        ],
        "answer": "Bias data"
      },
      {
        "question": "Komponen utama dalam proses AI adalah:",
        "options": [
          "Data, Algoritma, Model",
          "Hardware, Software, Jaringan",
          "Input, Output, Feedback",
          "Sensor, Aktuator, Controller"
        ],
        "answer": "Data, Algoritma, Model"
      }
    ]
  },
  "references": [
    "Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach*.",
    "Google AI Blog – https://ai.googleblog.com/",
    "Video: ‘What is Artificial Intelligence?’ – 3Blue1Brown (YouTube)",
    "Artikel: ‘Ethics of AI’ – Harvard Business Review"
  ]
}
 

------------------------------------------------------

## Prompt B

 
Anda adalah pembuat materi pembelajaran ahli.

Tugas Anda adalah membuat materi pembelajaran tentang {topik}.

Konteks: Materi pembelajaran ini akan digunakan oleh peserta didik atau pemula yang ingin memahami sebuah topik secara sistematis. Output akan digunakan sebagai referensi pembelajaran mandiri atau bahan ajar.


### Actual Output B

{
  "title": "Pengenalan Kecerdasan Buatan (AI) untuk Pemula",
  "level": "Pemula",
  "durationMinutes": 60,
  "learningObjectives": [
    "Mengenal definisi dan sejarah singkat kecerdasan buatan.",
    "Memahami konsep dasar AI: machine learning, deep learning, dan neural network.",
    "Mengenali contoh aplikasi AI dalam kehidupan sehari‑hari.",
    "Menjelaskan etika dasar dan tantangan penggunaan AI.",
    "Mampu mengidentifikasi sumber belajar lanjutan untuk mengembangkan pengetahuan AI."
  ],
  "materialsNeeded": [
    "Laptop/komputer dengan koneksi internet",
    "Proyektor atau layar (untuk instruktur)",
    "Slide presentasi (PDF/PowerPoint)",
    "Kertas dan pulpen untuk catatan",
    "Akses ke video contoh (YouTube/edX) dan artikel singkat"
  ],
  "outline": [
    {
      "sectionId": 1,
      "title": "Pembukaan & Motivasi",
      "durationMinutes": 5,
      "content": "Perkenalan singkat instruktur, agenda 60 menit, dan pertanyaan pemantik: Di mana Anda pernah melihat AI?",
      "activity": "Brainstorming cepat (peserta menyebutkan contoh AI yang mereka ketahui, ditulis di papan)."
    },
    {
      "sectionId": 2,
      "title": "Apa Itu Kecerdasan Buatan?",
      "durationMinutes": 10,
      "content": "Definisi AI, perbedaan AI, Machine Learning (ML), dan Deep Learning (DL). Sejarah singkat: Turing (1950), perceptron (1958), AI winter, kebangkitan ML (2000-sekarang).",
      "visualAid": "Slide timeline AI + diagram Venn AI/ML/DL",
      "activity": "Quiz interaktif (kahoot/mentimeter) 3 pertanyaan definisi."
    },
    {
      "sectionId": 3,
      "title": "Komponen Dasar AI",
      "durationMinutes": 12,
      "subsections": [
        {
          "title": "Data",
          "content": "Peran data dalam melatih model, contoh dataset gambar, teks, dan suara."
        },
        {
          "title": "Algoritma",
          "content": "Pengantar supervised vs unsupervised learning, contoh algoritma sederhana (linear regression, k-means)."
        },
        {
          "title": "Model & Inferensi",
          "content": "Bagaimana model dipelajari dan digunakan untuk prediksi."
        }
      ],
      "visualAid": "Diagram alur data algoritma model inferensi",
      "activity": "Demo singkat (Google Teachable Machine) peserta mengupload gambar dan melihat model belajar dalam 2 menit."
    },
    {
      "sectionId": 4,
      "title": "Aplikasi AI dalam Kehidupan Sehari-hari",
      "durationMinutes": 10,
      "content": [
        "Asisten virtual (Siri, Google Assistant)",
        "Rekomendasi konten (Netflix, YouTube)",
        "Deteksi penipuan pada kartu kredit",
        "Mobil otonom",
        "Diagnostik medis berbasis gambar"
      ],
      "visualAid": "Video kompilasi 1 menit contoh aplikasi AI",
      "activity": "Diskusi kelompok kecil (2-3 orang): pilih satu aplikasi, jelaskan cara kerjanya secara sederhana, lalu presentasikan dalam 1 menit."
    },
    {
      "sectionId": 5,
      "title": "Etika & Tantangan AI",
      "durationMinutes": 8,
      "content": [
        "Bias data dan diskriminasi",
        "Privasi dan keamanan data",
        "Transparansi (explainable AI)",
        "Dampak pekerjaan dan ekonomi"
      ],
      "visualAid": "Infografik 4 pilar etika AI",
      "activity": "Polling cepat: Apakah Anda khawatir AI menggantikan pekerjaan Anda? (Ya/Tidak/Netral) alasan singkat."
    },
    {
      "sectionId": 6,
      "title": "Langkah Selanjutnya untuk Belajar AI",
      "durationMinutes": 5,
      "content": [
        "Platform belajar gratis: Coursera, edX, Fast.ai, Google AI Hub",
        "Bahasa pemrograman yang umum: Python library (scikit-learn, TensorFlow, PyTorch)",
        "Proyek mini: klasifikasi gambar dengan Teachable Machine, chatbot sederhana dengan Dialogflow"
      ],
      "activity": "Menyusun rencana belajar 30-hari: peserta menuliskan 1 kursus, 1 proyek, dan 1 komunitas yang akan diikuti."
    },
    {
      "sectionId": 7,
      "title": "Penutup & Evaluasi",
      "durationMinutes": 5,
      "content": "Ringkasan poin utama, tanya-jawab, dan instruksi mengakses materi tambahan.",
      "assessment": {
        "type": "Formulir Google",
        "questions": [
          {
            "type": "pilihan_ganda",
            "question": "Apa perbedaan utama antara Machine Learning dan Deep Learning?",
            "options": [
              "ML menggunakan data, DL tidak",
              "DL menggunakan jaringan saraf berlapis banyak, ML tidak",
              "ML hanya untuk gambar, DL hanya untuk teks",
              "Tidak ada perbedaan"
            ],
            "answer": 1
          },
          {
            "type": "esai_singkat",
            "question": "Sebutkan satu contoh bias data dan bagaimana cara menguranginya."
          }
        ]
      }
    }
  ],
  "references": [
    {
      "title": "Artificial Intelligence: A Modern Approach (Stuart Russell & Peter Norvig)",
      "type": "buku",
      "link": "https://www.pearson.com"
    },
    {
      "title": "Google AI Education",
      "type": "website",
      "link": "https://ai.google/education/"
    },
    {
      "title": "Machine Learning Crash Course Google",
      "type": "kursus_online",
      "link": "https://developers.google.com/machine-learning/crash-course"
    },
    {
      "title": "Fast.ai Practical Deep Learning for Coders",
      "type": "kursus_online",
      "link": "https://www.fast.ai"
    }
  ]
}


------------------------------------------------------

## Prompt C

Anda adalah pembuat materi pembelajaran ahli yang berpengalaman dalam merancang kurikulum dan modul ajar untuk berbagai tingkat pemula.

Tugas Anda adalah membuat materi pembelajaran yang lengkap dan terstruktur berdasarkan topik, tingkat kesulitan, dan durasi waktu yang diberikan oleh pengguna.

Konteks: Materi pembelajaran ini akan digunakan oleh peserta didik atau pemula yang ingin memahami sebuah topik secara sistematis. Output akan digunakan sebagai referensi pembelajaran mandiri atau bahan ajar.

Batasan:
- Output HARUS berupa JSON valid dan tidak boleh menyertakan teks apa pun di luar JSON.
- Jangan sertakan markdown code block ( json ...  ).
- Semua field wajib diisi, tidak boleh kosong atau null.
- Field kuis minimal berisi 3 soal.
- Semua konten harus dalam bahasa Indonesia.
- Estimasi durasi harus sesuai dengan input durasi_menit yang diberikan.

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


### Actual Output C

{
  "topik": "Pengenalan Kecerdasan Buatan",
  "tingkat_kesulitan": "pemula",
  "tujuan_pembelajaran": [
    "Menjelaskan definisi dan ruang lingkup Kecerdasan Buatan (AI)",
    "Mengenali contoh penerapan AI dalam kehidupan sehari-hari",
    "Memahami konsep dasar Machine Learning dan perbedaannya dengan AI serta Deep Learning"
  ],
  "ringkasan_materi": "Materi ini memberikan gambaran umum tentang Kecerdasan Buatan, mulai dari definisi, sejarah singkat, hingga contoh aplikasi di berbagai bidang seperti kesehatan, transportasi, dan hiburan. Selanjutnya dijelaskan perbedaan antara AI, Machine Learning (ML), dan Deep Learning (DL), serta konsep dasar seperti data, model, pelatihan, dan inferensi. Peserta juga diperkenalkan pada tantangan etika dan masa depan AI.",
  "poin_penting": [
    "AI merupakan bidang ilmu yang berfokus pada pembuatan sistem yang dapat meniru perilaku cerdas manusia.",
    "Machine Learning adalah teknik utama dalam AI yang memungkinkan komputer belajar dari data tanpa diprogram secara eksplisit.",
    "Deep Learning adalah sub‑tipe Machine Learning yang menggunakan jaringan saraf tiruan dengan banyak lapisan untuk menangani data kompleks.",
    "Contoh aplikasi AI meliputi asisten virtual, rekomendasi produk, mobil otonom, dan diagnosis medis.",
    "Isu etika seperti bias data, privasi, dan dampak pekerjaan harus dipertimbangkan dalam pengembangan AI."
  ],
  "kuis": [
    {
      "pertanyaan": "Apa yang dimaksud dengan Kecerdasan Buatan (AI)?",
      "opsi_a": "Sebuah program yang dapat menulis kode secara otomatis",
      "opsi_b": "Sistem komputer yang meniru perilaku cerdas manusia",
      "opsi_c": "Hardware khusus untuk menghitung angka besar",
      "opsi_d": "Jaringan internet yang menghubungkan semua perangkat",
      "jawaban_benar": "B",
      "penjelasan": "AI adalah bidang ilmu yang berupaya menciptakan sistem yang dapat meniru atau mensimulasikan perilaku cerdas manusia, seperti belajar, berpikir, dan memecahkan masalah."
    },
    {
      "pertanyaan": "Manakah contoh aplikasi Machine Learning?",
      "opsi_a": "Pengaturan lampu lalu lintas manual",
      "opsi_b": "Sistem rekomendasi film di platform streaming",
      "opsi_c": "Kalkulator standar",
      "opsi_d": "Printer laser",
      "jawaban_benar": "B",
      "penjelasan": "Sistem rekomendasi film menggunakan algoritma Machine Learning untuk menganalisis perilaku pengguna dan menyarankan konten yang relevan."
    },
    {
      "pertanyaan": "Perbedaan utama antara Machine Learning dan Deep Learning terletak pada:",
      "opsi_a": "Deep Learning tidak memerlukan data untuk pelatihan",
      "opsi_b": "Machine Learning menggunakan jaringan saraf tiruan sederhana, sedangkan Deep Learning menggunakan jaringan dengan banyak lapisan",
      "opsi_c": "Machine Learning hanya dapat digunakan untuk gambar, sedangkan Deep Learning hanya untuk teks",
      "opsi_d": "Tidak ada perbedaan, keduanya istilah yang sama",
      "jawaban_benar": "B",
      "penjelasan": "Deep Learning merupakan sub‑tipe Machine Learning yang menggunakan jaringan saraf tiruan dengan banyak lapisan (deep) untuk menangani data yang lebih kompleks."
    }
  ],
  "saran_sumber_belajar": [
    "Buku: \"Artificial Intelligence: A Modern Approach\" oleh Stuart Russell & Peter Norvig (edisi bahasa Indonesia)",
    "Kursus online: \"AI For Everyone\" oleh Andrew Ng di Coursera"
  ],
  "estimasi_durasi_menit": 60
}
------------------------------------------------------


# Prompt Evaluation

### Dari ketiga prompt tersebut, mana yang menurut kalian menghasilkan output paling baik?

Prompt C menghasilkan output paling baik karena instruksi yang diberikan lebih lengkap dan spesifik dibandingkan Prompt A dan Prompt B. Output yang dihasilkan juga lebih terstruktur karena format JSON sudah ditentukan sejak awal.

### Kenapa?

Prompt C tidak hanya memberikan tugas, peran, dan konteks, tetapi juga menetapkan batasan yang harus diikuti oleh AI. Output yang dihasilkan lebih konsisten dan mudah kalau mau diimplementasikan ke dalam sistem pembelajaran. Tapi isinya belum bisa dipastikan akurat.

### Apa perbedaan paling terlihat antara Prompt A, Prompt B, dan Prompt C berdasarkan hasil testing kalian?

- Prompt A : Output cukup lengkap, ada tujuan pembelajaran, rencana kegiatan, kuis, dan referensi. Tapi formatnya masih bebas karena tidak ada aturan khusus.
- Prompt B : Output lebih terarah karena ada role dan context. Materi lebih bervariasi, aktivitas pembelajaran lebih banyak, dan ada saran untuk belajar lebih lanjut.
- Prompt C : Output lebih ringkas dan terstruktur karena format JSON sudah ditentukan. Ada batasan jumlah soal, bahasa, kelengkapan field, dan durasi. Prompt C menghasilkan output yang lebih konsisten.

------------------------------------------------------

# Failure Case

### Input yang menghasilkan output kurang baik

{
  "topik": "Apa arti kehidupan di dunia",
  "tingkat_kesulitan": "profesor",
  "durasi_menit": 5
}

### Actual Output

{
  "topik": "Apa arti kehidupan di dunia",
  "tingkat_kesulitan": "profesor",
  "tujuan_pembelajaran": [
    "Menganalisis konsep eksistensial dan teleologis dalam filsafat Barat dan Timur.",
    "Mengevaluasi argumen-argumen utama tentang makna hidup dari perspektif metafisika, psikologi, dan sains.",
    "Menyintesis pandangan lintas disiplin untuk membentuk kerangka kritis dalam menafsirkan arti kehidupan pribadi."
  ],
  "ringkasan_materi": "Materi ini membahas pertanyaan fundamental tentang arti kehidupan melalui lensa filsafat eksistensial (Sartre, Camus), teleologi (Aristoteles, Aquinas), serta perspektif kontemporer dalam neurobiologi dan psikologi positif. Pembahasan meliputi konsep nihilisme, absurdisme, dan humanisme, serta bagaimana narasi pribadi dapat diintegrasikan dengan temuan ilmiah tentang tujuan evolusioner dan kebahagiaan. Dengan pendekatan kritis, peserta diharapkan dapat menilai keabsahan masing-masing argumen dan merumuskan posisi intelektual yang koheren.",
  "poin_penting": [
    "Eksistensialisme menekankan kebebasan individu dalam menciptakan makna, bukan menemukan makna yang sudah ada.",
    "Teleologi berargumen bahwa tujuan akhir (telos) merupakan inti dari keberadaan, baik dalam konteks metafisik maupun biologis.",
    "Nihilisme menolak adanya nilai intrinsik, sementara absurdisme menerima ketidaksesuaian antara pencarian makna dan realitas yang tidak bermakna.",
    "Neurobiologi menunjukkan bahwa perasaan makna berhubungan dengan jaringan reward otak, namun tidak menjelaskan nilai normatif.",
    "Integrasi narasi pribadi dengan pemahaman ilmiah dapat menghasilkan kerangka makna yang dinamis dan adaptif."
  ],
  "kuis": [
    {
      "pertanyaan": "Menurut Jean-Paul Sartre, apa yang menjadi sumber utama makna hidup manusia?",
      "opsi_a": "Keberadaan Tuhan yang mutlak",
      "opsi_b": "Kebebasan dan pilihan individu",
      "opsi_c": "Hukum alam semesta",
      "opsi_d": "Takdir yang telah ditetapkan",
      "jawaban_benar": "B",
      "penjelasan": "Sartre berpendapat bahwa eksistensi mendahului esensi, sehingga manusia menciptakan makna melalui kebebasan dan pilihan mereka."
    },
    {
      "pertanyaan": "Dalam kerangka teleologi Aristoteles, apa yang dimaksud dengan 'telos'?",
      "opsi_a": "Kekacauan alam semesta",
      "opsi_b": "Tujuan atau akhir yang mendasari keberadaan sesuatu",
      "opsi_c": "Kekuatan destruktif",
      "opsi_d": "Kebetulan evolusioner",
      "jawaban_benar": "B",
      "penjelasan": "Telos merujuk pada tujuan akhir atau fungsi intrinsik yang memberi arah pada setiap entitas, termasuk makhluk hidup."
    },
    {
      "pertanyaan": "Manakah pernyataan berikut yang paling tepat menggambarkan posisi nihilisme?",
      "opsi_a": "Semua nilai moral bersifat relatif namun tetap ada",
      "opsi_b": "Tidak ada nilai atau makna yang bersifat objektif dalam kehidupan",
      "opsi_c": "Makna hidup ditentukan oleh hukum fisika",
      "opsi_d": "Manusia secara inheren mencari kebahagiaan sebagai tujuan akhir",
      "jawaban_benar": "B",
      "penjelasan": "Nihilisme menolak keberadaan nilai atau makna objektif, menyatakan bahwa segala sesuatu pada dasarnya tidak memiliki tujuan intrinsik."
    }
  ],
  "saran_sumber_belajar": [
    "Buku: \"Being and Nothingness\" oleh Jean-Paul Sartre",
    "Kursus daring: \"Philosophy of Meaning\" di Coursera, dipandu oleh profesor filsafat terkemuka"
  ],
  "estimasi_durasi_menit": 5
}

### Menurut kalian apa masalah dari output tersebut?

Isinya terlalu berat dan terlalu panjang untuk durasi 5 menit. Di situ ada 5 poin penting, 3 tujuan pembelajaran tingkat profesor, dan 3 soal kuis lengkap dengan penjelasan. Realistisnya materi seperti itu butuh 60–90 menit, bukan 5 menit. Masalahnya, field `estimasi_durasi_menit` tetap berisi 5, jadi model cuma menyalin angka durasi dari input tapi tidak menyesuaikan jumlah dan panjang isinya. Batasan lama cuma bilang "estimasi durasi harus sesuai dengan input", jadi model menuruti aturan itu secara harfiah tanpa memikirkan apakah isinya masuk akal. Selain itu, ketiga jawaban kuisnya kebetulan semuanya "B", jadi jawabannya tidak bervariasi.

### Apa yang kalian ubah pada prompt / constraint / kode?

batasan lama:

- Estimasi durasi harus sesuai dengan input durasi_menit yang diberikan.

saya ganti jadi aturan yang mengikat jumlah dan panjang isi ke durasi, sekaligus mengatur variasi jawaban kuis:

- Sesuaikan jumlah dan panjang isi dengan durasi_menit: durasi kurang dari 15 menit = ringkasan maksimal 3 kalimat, 3 poin penting, dan 3 soal kuis; durasi 15 sampai 60 menit = 5 poin penting dan 4 soal kuis; durasi lebih dari 60 menit = boleh lebih lengkap.
- Jawaban kuis harus bervariasi (A, B, C, dan D), tidak boleh semuanya sama.
- estimasi_durasi_menit WAJIB sama persis dengan durasi_menit pada input.

Selain prompt, saya juga tambah validasi di kode setelah JSON berhasil di-parse, supaya kalau LLM tetap tidak patuh, aplikasi tidak diam-diam mengembalikan output yang salah:

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

Jadi sekarang ada dua lapis pengaman: prompt mengatur isi supaya proporsional, dan kode memastikan durasi serta jumlah soal tetap benar.

### Output setelah diperbaiki

{
  "topik": "Apa arti kehidupan di dunia",
  "tingkat_kesulitan": "profesor",
  "tujuan_pembelajaran": [
    "Menganalisis konsep arti kehidupan dari perspektif filosofis",
    "Mengevaluasi pandangan eksistensial, religius, dan ilmiah tentang makna hidup",
    "Menyusun argumen pribadi yang terinformasi mengenai tujuan eksistensi manusia"
  ],
  "ringkasan_materi": "Arti kehidupan dipandang beragam melalui lensa filosofis, agama, dan ilmu pengetahuan; eksistensialisme menekankan penciptaan makna oleh individu, sementara tradisi religius sering mengaitkannya dengan tujuan transendental. Pendekatan ilmiah melihat kehidupan sebagai hasil evolusi biologis tanpa tujuan intrinsik, namun memberi ruang bagi pencarian nilai subjektif. Integrasi perspektif ini membantu membentuk pemahaman kritis tentang eksistensi manusia.",
  "poin_penting": [
    "Eksistensialisme menegaskan bahwa makna hidup diciptakan secara sadar oleh individu melalui pilihan dan tindakan.",
    "Pandangan religius biasanya mengaitkan arti kehidupan dengan tujuan ilahi atau transendensi spiritual.",
    "Ilmu pengetahuan menjelaskan kehidupan sebagai fenomena biologis, menyoroti pentingnya pencarian nilai subjektif dalam konteks evolusi."
  ],
  "kuis": [
    {
      "pertanyaan": "Menurut eksistensialisme, bagaimana arti kehidupan ditentukan?",
      "opsi_a": "Melalui takdir yang telah ditetapkan sejak lahir",
      "opsi_b": "Dengan penciptaan makna secara sadar oleh individu",
      "opsi_c": "Dengan mengikuti aturan agama secara ketat",
      "opsi_d": "Melalui proses evolusi biologis",
      "jawaban_benar": "B",
      "penjelasan": "Eksistensialisme menekankan bahwa individu bebas memilih dan menciptakan makna hidupnya sendiri."
    },
    {
      "pertanyaan": "Dalam pandangan religius, arti kehidupan biasanya dihubungkan dengan:",
      "opsi_a": "Pencapaian kepuasan material",
      "opsi_b": "Pengembangan teknologi",
      "opsi_c": "Tujuan ilahi atau transendensi spiritual",
      "opsi_d": "Adaptasi evolusioner",
      "jawaban_benar": "C",
      "penjelasan": "Kebanyakan tradisi agama mengaitkan makna hidup dengan tujuan yang diberikan oleh kekuatan supranatural."
    },
    {
      "pertanyaan": "Menurut perspektif ilmiah, apa yang paling tepat menggambarkan arti kehidupan?",
      "opsi_a": "Kehidupan memiliki tujuan intrinsik yang universal",
      "opsi_b": "Makna hidup ditentukan oleh hukum fisika semata",
      "opsi_c": "Kehidupan adalah hasil evolusi tanpa tujuan intrinsik, namun manusia dapat memberi nilai subjektif",
      "opsi_d": "Kehidupan hanya dapat dipahami melalui teks suci",
      "jawaban_benar": "C",
      "penjelasan": "Ilmu pengetahuan menjelaskan kehidupan sebagai proses biologis; makna hidup tidak inheren, melainkan dibangun secara subjektif."
    }
  ],
  "saran_sumber_belajar": [
    "Buku: \"Existentialism is a Humanism\" oleh Jean-Paul Sartre",
    "Artikel: \"The Meaning of Life\" di Stanford Encyclopedia of Philosophy"
  ],
  "estimasi_durasi_menit": 5
}

------------------------------------------------------

# Personal Reflection

Jawab menggunakan pendapat dan pengalaman kalian sendiri selama mengerjakan project.

### 1. Menurut kalian, bagian apa yang paling sulit dari project ini?

- Json yang kotor dari llm 
- Sebelumny pakai .format() yang bikin llm gagal kasih output karena format jsonnya

### 2. Bagian kode mana yang paling banyak dibantu oleh AI?

- def bersihkan_json_dari_llm
- eror handling

### 3. Setelah melihat kode tersebut, jelaskan menggunakan bahasa kalian sendiri bagaimana bagian tersebut bekerja.

- bersihkan_json_dari_llm(): Fungsi ini membersihkan output LLM biar jadi JSON murni. Sebelumnya LLM sering balik dengan markdown fence json ...  atau teks penjelasan di luar JSON. Fungsi ini sebelumnya buang fence-nya pakai regex, terus cari kurung kurawal buka { pertama. Dari situ dia hitung kedalaman: setiap ketemu { tambah 1, ketemu } kurang 1. Kalau hitungan balik ke 0, berarti JSON-nya sudah lengkap (termasuk nested object di dalam kuis). Dia potong substring itu dan return. Kalau gagal, fallback ambil sampai } terakhir.

- error handling (try/except → HTTPException): endpoint /generate, kode dibungkus try/except. Kalau json.loads() gagal parsing (LLM balik teks bukan JSON), tangkap JSONDecodeError dan raise HTTPException 502 dengan pesan jelas. Kalau error lain (timeout Groq, API error, validasi output gagal), tangkap Exception umum dan raise HTTPException 500. Jadi user selalu dapat response JSON dengan status code dan detail error yang bermakna, bukan crash server.

### 4. Menurut kalian, apa kekurangan terbesar dari aplikasi yang kalian buat jika digunakan oleh user sungguhan?

banyak si kekurangan nya hehe, tapi yang paling besar itu validasi inputnya hampir tidak ada, bisa di input apa saja sama user, dan tidak ada rate limit, jadi bisa spam request ke groq.

### 5. Jika provider LLM kalian diganti, misalnya dari Groq ke Gemini atau OpenAI, bagian mana dari project yang menurut kalian perlu diubah?

Kalau ke Gemini import google.genai, nama model yang digunakan, ganti API KEY di .env dan sesuaikan parameter.

### 6. Setelah mencoba aplikasi kalian sendiri, apa satu improvement yang menurut kalian paling penting jika project ini dilanjutkan?

Menurut saya improvement paling penting itu validasi input ketat, bisa tambahin enum tingkat_kesulitan (pemula/menengah/lanjutan) dan filter topik supaya nggak ada input aneh yang sampai ke LLM. Kedua, retry otomatis kalau validasi output gagal, biar nggak perlu manual jalanin ulang. Kalau ada streaming response juga bagus biar user nggak nunggu 10–20 detik diam.

------------------------------------------------------

# AI Usage

### AI tools yang digunakan

Gemini

### AI digunakan untuk membantu bagian apa?

fungsi bersihkan_json_dari_llm() pakai nested-brace counting, struktur Pydantic model dengan Field validation, dan setup error handling FastAPI. Juga bantu debugging error .format() vs JSON brace.

### Bagian apa yang kalian tentukan, perbaiki, atau ubah sendiri setelah melihat hasil dari AI?

Saya yang tentuin use case (Learning Material Generator), schema JSON 8 field, buat promptnya, constraint durasi di prompt, validasi output di kode (guardrail estimasi_durasi_menit & kuis >= 3), dan Failure Case input/output. Saya juga yang tes API, bandingin Prompt A/B/C, dan nulis Prompt Evaluation serta README.#   t u g a s - g e n a i - l l m  
 