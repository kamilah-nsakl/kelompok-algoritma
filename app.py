import streamlit as st

# -------------------------------------------------
# KONFIGURASI HALAMAN
# -------------------------------------------------
st.set_page_config(
    page_title="Analisis Klasifikasi Penyakit",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS UNTUK DESAIN
# -------------------------------------------------
st.markdown(
    """
    <style>
    /* Background halaman */
    .stApp {
        background: linear-gradient(135deg, #eef2f7 0%, #dbeafe 50%, #eef2ff 100%);
        font-family: "Segoe UI", sans-serif;
    }

    /* Container utama */
    .main-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 25px 30px;
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.15);
        margin-bottom: 25px;
        border: 1px solid rgba(148, 163, 184, 0.3);
    }

    /* Judul utama */
    .main-title {
        text-align: center;
        font-size: 2.1rem;
        font-weight: 800;
        color: #111827;
        letter-spacing: .03em;
        margin-bottom: 6px;
    }

    .subtitle {
        text-align: center;
        font-size: 0.95rem;
        color: #4b5563;
        margin-bottom: 18px;
    }

    .badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: .08em;
        text-transform: uppercase;
        background: rgba(59, 130, 246, 0.1);
        color: #1d4ed8;
        margin-bottom: 8px;
    }

    /* Garis pemisah halus */
    .soft-divider {
        height: 1px;
        background: linear-gradient(to right, transparent, #cbd5f5, transparent);
        margin: 10px 0 20px 0;
    }

    /* Kartu algoritma */
    .algo-card {
        background: linear-gradient(135deg, #f9fafb, #eef2ff);
        border-radius: 16px;
        padding: 16px 18px;
        border: 1px solid rgba(148, 163, 184, 0.4);
        box-shadow: 0 4px 12px rgba(148, 163, 184, 0.25);
    }
    .algo-title {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .algo-sub {
        font-size: 0.82rem;
        color: #4b5563;
        margin-bottom: 10px;
    }
    .algo-tag {
        display: inline-block;
        font-size: 0.7rem;
        padding: 2px 8px;
        border-radius: 999px;
        margin-bottom: 6px;
        font-weight: 600;
    }
    .tag-knn { background: rgba(239, 68, 68, 0.1); color: #b91c1c; }
    .tag-dt  { background: rgba(34, 197, 94, 0.1); color: #166534; }
    .tag-nb  { background: rgba(245, 158, 11, 0.1); color: #92400e; }

    .metric-row {
        display: flex;
        justify-content: space-between;
        font-size: 0.82rem;
        padding: 2px 0;
    }
    .metric-name {
        color: #4b5563;
    }
    .metric-value {
        font-weight: 700;
        color: #111827;
    }

    /* Panel gejala */
    .section-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 2px;
    }
    .section-caption {
        font-size: 0.85rem;
        color: #6b7280;
        margin-bottom: 8px;
    }

    /* Hasil prediksi */
    .result-card {
        background: linear-gradient(135deg, #eff6ff, #e0f2fe);
        border-radius: 16px;
        padding: 16px 18px;
        border: 1px solid rgba(59, 130, 246, 0.4);
        box-shadow: 0 6px 18px rgba(37, 99, 235, 0.25);
    }
    .result-title {
        font-size: 1.0rem;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 8px;
    }
    .result-item-label {
        font-size: 0.85rem;
        color: #374151;
    }
    .result-item-value {
        font-size: 0.9rem;
        font-weight: 700;
        color: #111827;
    }
    .result-badge {
        font-size: 0.8rem;
        font-weight: 600;
        color: #1d4ed8;
    }
    .result-conf {
        font-size: 0.78rem;
        color: #4b5563;
    }

    /* Footer */
    .footer-text {
        text-align: center;
        font-size: 0.75rem;
        color: #6b7280;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("<div class='badge'>Klasifikasi Penyakit Berbasis Gejala</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='main-title'>Analisis Penerapan Algoritma Klasifikasi Penyakit</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div class='subtitle'>Perbandingan K-Nearest Neighbor, Decision Tree, dan Naïve Bayes "
    "dalam Klasifikasi Penyakit Berdasarkan Gejala</div>",
    unsafe_allow_html=True
)

st.markdown("<div class='soft-divider'></div>", unsafe_allow_html=True)

# -------------------------------------------------
# KARTU PERBANDINGAN ALGORITMA
# -------------------------------------------------
st.markdown("**Ringkasan Performa Algoritma**")
st.caption("Nilai berikut bersifat ilustratif sebagai gambaran performa model pada dataset klasifikasi penyakit.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='algo-card'>", unsafe_allow_html=True)
    st.markdown("<span class='algo-tag tag-knn'>KNN</span>", unsafe_allow_html=True)
    st.markdown("<div class='algo-title'>K-Nearest Neighbor</div>", unsafe_allow_html=True)
    st.markdown("<div class='algo-sub'>Mengklasifikasikan data berdasarkan kedekatan ke tetangga terdekat.</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='metric-row'><span class='metric-name'>Akurasi</span><span class='metric-value'>87.5%</span></div>
        <div class='metric-row'><span class='metric-name'>Presisi</span><span class='metric-value'>85.2%</span></div>
        <div class='metric-row'><span class='metric-name'>Recall</span><span class='metric-value'>86.8%</span></div>
        <div class='metric-row'><span class='metric-name'>F1-Score</span><span class='metric-value'>86.0%</span></div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='algo-card'>", unsafe_allow_html=True)
    st.markdown("<span class='algo-tag tag-dt'>Decision Tree</span>", unsafe_allow_html=True)
    st.markdown("<div class='algo-title'>Decision Tree</div>", unsafe_allow_html=True)
    st.markdown("<div class='algo-sub'>Membagi data berdasarkan aturan if–else dalam struktur pohon keputusan.</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='metric-row'><span class='metric-name'>Akurasi</span><span class='metric-value'>91.2%</span></div>
        <div class='metric-row'><span class='metric-name'>Presisi</span><span class='metric-value'>90.5%</span></div>
        <div class='metric-row'><span class='metric-name'>Recall</span><span class='metric-value'>89.8%</span></div>
        <div class='metric-row'><span class='metric-name'>F1-Score</span><span class='metric-value'>90.1%</span></div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='algo-card'>", unsafe_allow_html=True)
    st.markdown("<span class='algo-tag tag-nb'>Naïve Bayes</span>", unsafe_allow_html=True)
    st.markdown("<div class='algo-title'>Naïve Bayes</div>", unsafe_allow_html=True)
    st.markdown("<div class='algo-sub'>Model probabilistik berbasis Teorema Bayes dengan asumsi independensi antar fitur.</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='metric-row'><span class='metric-name'>Akurasi</span><span class='metric-value'>83.7%</span></div>
        <div class='metric-row'><span class='metric-name'>Presisi</span><span class='metric-value'>82.1%</span></div>
        <div class='metric-row'><span class='metric-name'>Recall</span><span class='metric-value'>84.3%</span></div>
        <div class='metric-row'><span class='metric-name'>F1-Score</span><span class='metric-value'>83.2%</span></div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # Tutup main-container pertama

# -------------------------------------------------
# PANEL GEJALA & PREDIKSI
# -------------------------------------------------
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>Simulasi Prediksi Penyakit</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-caption'>Pilih kombinasi gejala yang dialami, kemudian jalankan simulasi untuk melihat prediksi "
    "dari ketiga algoritma klasifikasi.</div>",
    unsafe_allow_html=True
)

colg1, colg2, colg3 = st.columns(3)

with colg1:
    st.markdown("**Gejala Umum**")
    demam = st.checkbox("Demam")
    batuk = st.checkbox("Batuk")
    kelelahan = st.checkbox("Kelelahan")
    sakit_kepala = st.checkbox("Sakit Kepala")

with colg2:
    st.markdown("**Gejala Pernapasan & Pencernaan**")
    nyeri_tenggorokan = st.checkbox("Nyeri Tenggorokan")
    sesak_napas = st.checkbox("Sesak Napas")
    muntah = st.checkbox("Muntah")
    diare = st.checkbox("Diare")

with colg3:
    st.markdown("**Gejala Lainnya**")
    ruam = st.checkbox("Ruam")
    nyeri_dada = st.checkbox("Nyeri Dada")

st.markdown("---")

prediksi_btn = st.button("🔍 Jalankan Prediksi Penyakit")

if prediksi_btn:
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

    symptom_count = sum(symptoms.values())

    if symptom_count == 0:
        st.warning("Silakan pilih minimal satu gejala untuk melakukan simulasi prediksi.")
    else:
        # Logika rule-based yang diadaptasi dari JavaScript HTML awal
        if demam and batuk and nyeri_tenggorokan:
            knnPrediction, knnConf = "Flu", "87%"
            dtPrediction, dtConf = "Flu", "92%"
            nbPrediction, nbConf = "Flu", "85%"

        elif demam and ruam and (not batuk):
            knnPrediction, knnConf = "Demam Berdarah", "82%"
            dtPrediction, dtConf = "Demam Berdarah", "89%"
            nbPrediction, nbConf = "Demam Berdarah", "79%"

        elif demam and sesak_napas and batuk:
            knnPrediction, knnConf = "COVID-19", "85%"
            dtPrediction, dtConf = "COVID-19", "91%"
            nbPrediction, nbConf = "COVID-19", "83%"

        elif demam and muntah and diare:
            knnPrediction, knnConf = "Gastroenteritis", "84%"
            dtPrediction, dtConf = "Gastroenteritis", "88%"
            nbPrediction, nbConf = "Gastroenteritis", "81%"

        elif sakit_kepala and (not demam):
            knnPrediction, knnConf = "Migrain", "79%"
            dtPrediction, dtConf = "Migrain", "85%"
            nbPrediction, nbConf = "Migrain", "76%"

        elif sesak_napas and nyeri_dada:
            knnPrediction, knnConf = "Pneumonia", "86%"
            dtPrediction, dtConf = "Pneumonia", "90%"
            nbPrediction, nbConf = "Pneumonia", "82%"

        elif batuk and nyeri_tenggorokan and (not demam):
            knnPrediction, knnConf = "Alergi", "81%"
            dtPrediction, dtConf = "Alergi", "87%"
            nbPrediction, nbConf = "Alergi", "78%"

        elif demam and muntah and (not diare):
            knnPrediction, knnConf = "Tifus", "83%"
            dtPrediction, dtConf = "Tifus", "86%"
            nbPrediction, nbConf = "Tifus", "80%"

        else:
            knnPrediction, knnConf = "Tidak dapat diprediksi dengan pasti", ""
            dtPrediction, dtConf = "Tidak dapat diprediksi dengan pasti", ""
            nbPrediction, nbConf = "Tidak dapat diprediksi dengan pasti", ""

        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown("<div class='result-title'>Hasil Simulasi Prediksi Penyakit</div>", unsafe_allow_html=True)

        colr1, colr2, colr3 = st.columns(3)

        with colr1:
            st.markdown(
                f"""
                <div class='result-item-label'>K-Nearest Neighbor</div>
                <div class='result-item-value'>{knnPrediction}</div>
                <div class='result-conf'>Tingkat keyakinan: <strong>{knnConf}</strong></div>
                """,
                unsafe_allow_html=True
            )

        with colr2:
            st.markdown(
                f"""
                <div class='result-item-label'>Decision Tree</div>
                <div class='result-item-value'>{dtPrediction}</div>
                <div class='result-conf'>Tingkat keyakinan: <strong>{dtConf}</strong></div>
                """,
                unsafe_allow_html=True
            )

        with colr3:
            st.markdown(
                f"""
                <div class='result-item-label'>Naïve Bayes</div>
                <div class='result-item-value'>{nbPrediction}</div>
                <div class='result-conf'>Tingkat keyakinan: <strong>{nbConf}</strong></div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)  # Tutup result-card

st.markdown("</div>", unsafe_allow_html=True)  # Tutup main-container kedua

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown(
    "<div class='footer-text'>Simulasi ini bersifat edukatif untuk memahami perbandingan algoritma klasifikasi penyakit berbasis gejala.</div>",
    unsafe_allow_html=True
)
