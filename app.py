import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Analisis Klasifikasi Penyakit",
    page_icon="🩺",
    layout="wide"
)

# =========================
# CSS Kustom untuk Desain
# =========================
st.markdown("""
<style>
/* Background utama */
.stApp {
    background: linear-gradient(135deg, #eef4ff 0%, #f8fbff 40%, #ffffff 100%);
}

/* Container utama */
.main-card {
    background-color: #ffffff;
    border-radius: 18px;
    padding: 24px 26px;
    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.12);
    border: 1px solid #e5e7eb;
}

/* Header gradient */
.hero {
    background: linear-gradient(120deg, #2563eb, #1d4ed8, #0f172a);
    color: #ffffff;
    padding: 26px 30px;
    border-radius: 20px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}

.hero::after {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    background: radial-gradient(circle, rgba(255,255,255,0.22), transparent 70%);
    top: -60px;
    right: -40px;
}

.hero-title {
    font-size: 1.9rem;
    font-weight: 700;
    margin-bottom: 6px;
}

.hero-subtitle {
    font-size: 1.02rem;
    max-width: 700px;
    opacity: 0.94;
}

/* Badge kecil */
.hero-badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.4);
    font-size: 0.75rem;
    margin-bottom: 10px;
    background: rgba(15,23,42,0.28);
    backdrop-filter: blur(6px);
}

/* Informasi singkat praktis */
.info-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 14px;
}

.info-pill {
    padding: 6px 10px;
    border-radius: 999px;
    background: rgba(15,23,42,0.18);
    font-size: 0.78rem;
}

/* Judul section */
.section-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 4px;
}

.section-caption {
    font-size: 0.9rem;
    color: #6b7280;
}

/* Card kecil info */
.info-card {
    background: #f9fafb;
    border-radius: 14px;
    padding: 12px 14px;
    border: 1px solid #e5e7eb;
    font-size: 0.86rem;
}

/* Card algoritma */
.alg-card {
    background: #ffffff;
    border-radius: 14px;
    padding: 14px 16px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 12px rgba(15,23,42,0.08);
}

.alg-title {
    font-weight: 700;
    margin-bottom: 4px;
}

.alg-subtitle {
    font-size: 0.86rem;
    color: #6b7280;
    margin-bottom: 10px;
}

/* Badge algoritma */
.alg-badge-knn {
    display: inline-block;
    padding: 3px 8px;
    border-radius: 999px;
    font-size: 0.72rem;
    background: rgba(239, 68, 68, 0.09);
    color: #b91c1c;
    margin-bottom: 6px;
}

.alg-badge-dt {
    display: inline-block;
    padding: 3px 8px;
    border-radius: 999px;
    font-size: 0.72rem;
    background: rgba(22, 163, 74, 0.09);
    color: #166534;
    margin-bottom: 6px;
}

.alg-badge-nb {
    display: inline-block;
    padding: 3px 8px;
    border-radius: 999px;
    font-size: 0.72rem;
    background: rgba(245, 158, 11, 0.09);
    color: #92400e;
    margin-bottom: 6px;
}

/* Baris metrik */
.metric-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.85rem;
    padding: 4px 0;
    border-bottom: 1px dashed #e5e7eb;
}

.metric-row:last-child {
    border-bottom: none;
}

.metric-label {
    color: #4b5563;
}

.metric-value {
    font-weight: 700;
    color: #111827;
}

/* Tabel perbandingan */
.comparison-note {
    font-size: 0.8rem;
    color: #6b7280;
    margin-bottom: 6px;
}

/* Hasil prediksi */
.result-card {
    background: #ecfdf5;
    border-radius: 14px;
    padding: 16px 16px 10px 16px;
    border: 1px solid #bbf7d0;
}

.result-title {
    font-weight: 700;
    margin-bottom: 6px;
    color: #166534;
}

.alg-result-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.9rem;
    padding: 5px 0;
    border-bottom: 1px dashed #d1fae5;
}

.alg-result-row:last-child {
    border-bottom: none;
}

.alg-name {
    font-weight: 600;
    color: #064e3b;
}

.alg-pred {
    font-weight: 600;
    color: #111827;
}

.alg-conf {
    font-size: 0.8rem;
    color: #6b7280;
}

/* Footer */
.app-footer {
    text-align: center;
    margin-top: 16px;
    font-size: 0.8rem;
    color: #9ca3af;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Data sampel (20 baris)
# =========================
data = [
    [1,1,1,1,1,0,0,0,0,0,"Flu"],
    [0,1,1,1,1,0,0,0,0,0,"Flu"],
    [1,1,1,1,1,0,0,0,0,1,"Flu"],
    [1,1,1,1,1,0,0,0,0,0,"Flu"],
    [1,1,0,1,1,0,0,0,0,0,"Flu"],
    [1,0,1,1,0,1,0,0,0,0,"Demam Berdarah"],
    [1,0,1,0,0,0,0,0,0,0,"Demam Berdarah"],
    [1,0,1,1,0,1,0,0,0,0,"Demam Berdarah"],
    [1,1,1,1,0,0,0,0,1,0,"COVID-19"],
    [1,1,1,1,0,0,0,0,1,0,"COVID-19"],
    [1,0,1,1,0,0,1,0,0,0,"Tifus"],
    [1,0,1,1,0,0,1,0,0,0,"Tifus"],
    [0,1,0,0,1,0,0,0,0,0,"Alergi"],
    [0,1,0,0,1,0,0,0,0,0,"Alergi"],
    [0,0,1,1,0,0,0,0,0,0,"Migrain"],
    [0,0,0,1,0,0,0,0,0,0,"Migrain"],
    [1,0,1,0,0,0,1,1,0,0,"Gastroenteritis"],
    [1,0,1,0,0,0,1,1,1,0,"Gastroenteritis"],
    [0,0,1,1,0,0,0,0,1,1,"Pneumonia"],
    [1,1,1,1,0,0,0,0,1,1,"Pneumonia"],
]

columns = [
    "Demam", "Batuk", "Kelelahan", "Sakit Kepala", "Nyeri Tenggorokan",
    "Ruam", "Muntah", "Diare", "Sesak Napas", "Nyeri Dada", "Penyakit"
]
df_samples = pd.DataFrame(data, columns=columns)

# =========================
# Header / Hero
# =========================
st.markdown(
    """
<div class="hero">
    <div class="hero-badge">Dashboard Edukatif • Klasifikasi Penyakit Berbasis Gejala</div>
    <div class="hero-title">Analisis Penerapan Algoritma Klasifikasi Penyakit</div>
    <div class="hero-subtitle">
        Perbandingan K-Nearest Neighbor, Decision Tree, dan Naïve Bayes 
        dalam mengklasifikasikan penyakit berdasarkan kombinasi gejala klinis yang sering muncul.
    </div>
    <div class="info-strip">
        <div class="info-pill">👨‍⚕️ Cocok untuk edukasi mahasiswa & tenaga kesehatan pemula</div>
        <div class="info-pill">📊 Menampilkan sampel data, metrik performa, dan simulasi prediksi</div>
        <div class="info-pill">⚠️ Untuk tujuan pembelajaran, bukan alat diagnosis medis resmi</div>
    </div>
</div>
""",
    unsafe_allow_html=True
)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

# =========================
# Tabs utama
# =========================
tab1, tab2, tab3 = st.tabs(
    ["📁 Sampel Dataset", "📊 Perbandingan Algoritma", "🔍 Simulasi Prediksi Penyakit"]
)

# =========================
# TAB 1: Dataset Sampel
# =========================
with tab1:
    st.markdown('<p class="section-title">1. Sampel Data Klasifikasi Penyakit</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-caption">'
        'Tabel berikut menampilkan 20 sampel data gejala dengan label penyakit yang digunakan sebagai contoh '
        'untuk menjelaskan cara kerja algoritma klasifikasi.</p>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns([2, 1.2])
    with c1:
        st.dataframe(df_samples, use_container_width=True, height=420)

    with c2:
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown(
            """
**Cara membaca tabel:**

- Kolom gejala berisi nilai:
  - `1` = gejala muncul
  - `0` = gejala tidak muncul  
- Kolom **Penyakit** adalah label kelas target:
  - *Flu, Demam Berdarah, COVID-19, Tifus, Alergi, Migrain, Gastroenteritis, Pneumonia*  
- Data ini bersifat fiktif untuk keperluan pembelajaran klasifikasi dan pemodelan.
            """,
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("ℹ️ Penjelasan singkat tiap gejala"):
        st.write(
            """
- **Demam**: peningkatan suhu tubuh di atas normal.  
- **Batuk**: respon refleks saluran napas.  
- **Kelelahan**: rasa lelah berlebihan atau tidak biasa.  
- **Sakit Kepala**: nyeri di area kepala.  
- **Nyeri Tenggorokan**: rasa sakit atau tidak nyaman saat menelan.  
- **Ruam**: perubahan warna/tekstur kulit.  
- **Muntah**: pengosongan isi lambung secara paksa.  
- **Diare**: buang air besar cair dengan frekuensi meningkat.  
- **Sesak Napas**: kesulitan bernapas atau rasa berat di dada.  
- **Nyeri Dada**: rasa nyeri/tekanan di area dada.
            """
        )

# =========================
# TAB 2: Perbandingan Algoritma
# =========================
with tab2:
    st.markdown('<p class="section-title">2. Perbandingan Performa Algoritma</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-caption">'
        'Tiga algoritma umum pada klasifikasi—K-NN, Decision Tree, dan Naïve Bayes—'
        'dibandingkan berdasarkan metrik akurasi, presisi, recall, F1-Score, waktu pelatihan, '
        'dan tingkat interpretabilitas.</p>',
        unsafe_allow_html=True
    )

    col_knn, col_dt, col_nb = st.columns(3)

    with col_knn:
        st.markdown('<div class="alg-card">', unsafe_allow_html=True)
        st.markdown('<div class="alg-badge-knn">Instance-based Learning</div>', unsafe_allow_html=True)
        st.markdown('<div class="alg-title">K-Nearest Neighbor (K-NN)</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="alg-subtitle">Mengklasifikasikan data baru dengan melihat tetangga terdekat '
            'pada ruang fitur.</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            """
<div class="metric-row"><span class="metric-label">Akurasi</span><span class="metric-value">87,5%</span></div>
<div class="metric-row"><span class="metric-label">Presisi</span><span class="metric-value">85,2%</span></div>
<div class="metric-row"><span class="metric-label">Recall</span><span class="metric-value">86,8%</span></div>
<div class="metric-row"><span class="metric-label">F1-Score</span><span class="metric-value">86,0%</span></div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_dt:
        st.markdown('<div class="alg-card">', unsafe_allow_html=True)
        st.markdown('<div class="alg-badge-dt">Rule-based Model</div>', unsafe_allow_html=True)
        st.markdown('<div class="alg-title">Decision Tree</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="alg-subtitle">Membentuk pohon keputusan berdasarkan pemisahan atribut '
            'yang paling informatif.</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            """
<div class="metric-row"><span class="metric-label">Akurasi</span><span class="metric-value">91,2%</span></div>
<div class="metric-row"><span class="metric-label">Presisi</span><span class="metric-value">90,5%</span></div>
<div class="metric-row"><span class="metric-label">Recall</span><span class="metric-value">89,8%</span></div>
<div class="metric-row"><span class="metric-label">F1-Score</span><span class="metric-value">90,1%</span></div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_nb:
        st.markdown('<div class="alg-card">', unsafe_allow_html=True)
        st.markdown('<div class="alg-badge-nb">Probabilistic Model</div>', unsafe_allow_html=True)
        st.markdown('<div class="alg-title">Naïve Bayes</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="alg-subtitle">Menggunakan Teorema Bayes dengan asumsi kemandirian antar fitur.</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            """
<div class="metric-row"><span class="metric-label">Akurasi</span><span class="metric-value">83,7%</span></div>
<div class="metric-row"><span class="metric-label">Presisi</span><span class="metric-value">82,1%</span></div>
<div class="metric-row"><span class="metric-label">Recall</span><span class="metric-value">84,3%</span></div>
<div class="metric-row"><span class="metric-label">F1-Score</span><span class="metric-value">83,2%</span></div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<p class="comparison-note">Ringkasan perbandingan:</p>', unsafe_allow_html=True)

    df_compare = pd.DataFrame(
        {
            "Metrik": [
                "Akurasi", "Presisi", "Recall", "F1-Score",
                "Waktu Pelatihan", "Interpretabilitas"
            ],
            "K-NN": ["87,5%", "85,2%", "86,8%", "86,0%", "Sedang", "Rendah"],
            "Decision Tree": ["91,2%", "90,5%", "89,8%", "90,1%", "Cepat", "Tinggi"],
            "Naïve Bayes": ["83,7%", "82,1%", "84,3%", "83,2%", "Sangat Cepat", "Sedang"],
        }
    )
    st.table(df_compare)

    with st.expander("💡 Interpretasi cepat untuk pengguna"):
        st.write(
            """
- **Decision Tree** sering menjadi pilihan terbaik jika Bapak/Ibu/mahasiswa ingin:
  - Performa yang baik **dan**
  - Model yang mudah dijelaskan ke pihak non-teknis (interpretabilitas tinggi).  
- **K-NN** cocok sebagai baseline sederhana, namun kurang efisien untuk data sangat besar.  
- **Naïve Bayes** sangat cepat dan cocok untuk sistem yang membutuhkan respon real-time,
  dengan asumsi bahwa fitur relatif independen.
            """
        )

# =========================
# TAB 3: Simulasi Prediksi Penyakit
# =========================
with tab3:
    st.markdown('<p class="section-title">3. Simulasi Prediksi Berdasarkan Gejala</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-caption">'
        'Pilih kombinasi gejala yang dialami pasien secara hipotetik, kemudian lihat prediksi '
        'dari ketiga algoritma berdasarkan aturan sederhana yang diturunkan dari pola data sampel.</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="info-card">Simulasi ini untuk tujuan pelatihan dan ilustrasi. '
        '<b>Bukan</b> untuk pengambilan keputusan klinis nyata.</div>',
        unsafe_allow_html=True
    )
    st.write(" ")

    col_g1, col_g2, col_g3 = st.columns(3)

    with col_g1:
        st.markdown("**Gejala Umum**")
        demam = st.checkbox("Demam")
        batuk = st.checkbox("Batuk")
        kelelahan = st.checkbox("Kelelahan")
        sakit_kepala = st.checkbox("Sakit Kepala")

    with col_g2:
        st.markdown("**Gejala Pernapasan & Pencernaan**")
        nyeri_tenggorokan = st.checkbox("Nyeri Tenggorokan")
        sesak_napas = st.checkbox("Sesak Napas")
        muntah = st.checkbox("Muntah")
        diare = st.checkbox("Diare")

    with col_g3:
        st.markdown("**Gejala Lainnya**")
        ruam = st.checkbox("Ruam (bintik/ruam kulit)")
        nyeri_dada = st.checkbox("Nyeri Dada")

    st.write(" ")
    prediksi = st.button("🔍 Jalankan Prediksi")

    if prediksi:
        symptoms = {
            "demam": demam,
            "batuk": batuk,
            "kelelahan": kelelahan,
            "sakitKepala": sakit_kepala,
            "nyeriTenggorokan": nyeri_tenggorokan,
            "sesakNapas": sesak_napas,
            "muntah": muntah,
            "diare": diare,
            "ruam": ruam,
            "nyeriDada": nyeri_dada,
        }

        symptomCount = sum(1 for v in symptoms.values() if v)

        if symptomCount == 0:
            st.warning("Silakan pilih minimal satu gejala terlebih dahulu.")
        else:
            # -------------------------
            # Logika prediksi (sama persis dengan JS asli)
            # -------------------------
            knnPrediction = dtPrediction = nbPrediction = ""
            knnConfidence = dtConfidence = nbConfidence = ""

            if symptoms["demam"] and symptoms["batuk"] and symptoms["nyeriTenggorokan"]:
                knnPrediction = "Flu"
                knnConfidence = "87%"
                dtPrediction = "Flu"
                dtConfidence = "92%"
                nbPrediction = "Flu"
                nbConfidence = "85%"
            elif symptoms["demam"] and symptoms["ruam"] and not symptoms["batuk"]:
                knnPrediction = "Demam Berdarah"
                knnConfidence = "82%"
                dtPrediction = "Demam Berdarah"
                dtConfidence = "89%"
                nbPrediction = "Demam Berdarah"
                nbConfidence = "79%"
            elif symptoms["demam"] and symptoms["sesakNapas"] and symptoms["batuk"]:
                knnPrediction = "COVID-19"
                knnConfidence = "85%"
                dtPrediction = "COVID-19"
                dtConfidence = "91%"
                nbPrediction = "COVID-19"
                nbConfidence = "83%"
            elif symptoms["demam"] and symptoms["muntah"] and symptoms["diare"]:
                knnPrediction = "Gastroenteritis"
                knnConfidence = "84%"
                dtPrediction = "Gastroenteritis"
                dtConfidence = "88%"
                nbPrediction = "Gastroenteritis"
                nbConfidence = "81%"
            elif symptoms["sakitKepala"] and not symptoms["demam"]:
                knnPrediction = "Migrain"
                knnConfidence = "79%"
                dtPrediction = "Migrain"
                dtConfidence = "85%"
                nbPrediction = "Migrain"
                nbConfidence = "76%"
            elif symptoms["sesakNapas"] and symptoms["nyeriDada"]:
                knnPrediction = "Pneumonia"
                knnConfidence = "86%"
                dtPrediction = "Pneumonia"
                dtConfidence = "90%"
                nbPrediction = "Pneumonia"
                nbConfidence = "82%"
            elif symptoms["batuk"] and symptoms["nyeriTenggorokan"] and not symptoms["demam"]:
                knnPrediction = "Alergi"
                knnConfidence = "81%"
                dtPrediction = "Alergi"
                dtConfidence = "87%"
                nbPrediction = "Alergi"
                nbConfidence = "78%"
            elif symptoms["demam"] and symptoms["muntah"] and not symptoms["diare"]:
                knnPrediction = "Tifus"
                knnConfidence = "83%"
                dtPrediction = "Tifus"
                dtConfidence = "86%"
                nbPrediction = "Tifus"
                nbConfidence = "80%"
            else:
                knnPrediction = "Tidak dapat diprediksi dengan pasti"
                knnConfidence = ""
                dtPrediction = "Tidak dapat diprediksi dengan pasti"
                dtConfidence = ""
                nbPrediction = "Tidak dapat diprediksi dengan pasti"
                nbConfidence = ""

            st.markdown(
                f"""
<div class="result-card">
    <div class="result-title">Hasil Prediksi dari Tiga Algoritma</div>
    <div class="alg-result-row">
        <span class="alg-name">K-Nearest Neighbor</span>
        <span class="alg-pred">{knnPrediction} <span class="alg-conf">{knnConfidence}</span></span>
    </div>
    <div class="alg-result-row">
        <span class="alg-name">Decision Tree</span>
        <span class="alg-pred">{dtPrediction} <span class="alg-conf">{dtConfidence}</span></span>
    </div>
    <div class="alg-result-row">
        <span class="alg-name">Naïve Bayes</span>
        <span class="alg-pred">{nbPrediction} <span class="alg-conf">{nbConfidence}</span></span>
    </div>
</div>
                """,
                unsafe_allow_html=True
            )

            with st.expander("📘 Cara menafsirkan hasil untuk pengguna awam"):
                st.write(
                    """
- Jika ketiga algoritma memberikan **penyakit yang sama**, maka model cenderung konsisten pada pola gejala tersebut.  
- Persentase **confidence** di sini adalah ilustrasi tingkat keyakinan model (bukan probabilitas klinis).  
- Jika hasilnya *“Tidak dapat diprediksi dengan pasti”*, berarti kombinasi gejala tidak cocok dengan pola aturan
  sederhana yang digunakan pada contoh ini.
                    """
                )

# =========================
# Footer
# =========================
st.markdown(
    """
<div class="app-footer">
    Analisis Klasifikasi Penyakit Berdasarkan Gejala &copy; 2023 — Dibangun untuk tujuan edukasi dan simulasi.
</div>
</div>
""",
    unsafe_allow_html=True
)
