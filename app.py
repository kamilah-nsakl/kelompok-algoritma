import streamlit as st
import pandas as pd

# -------------------------------------------------
# Konfigurasi dasar halaman
# -------------------------------------------------
st.set_page_config(
    page_title="Analisis Klasifikasi Penyakit",
    layout="wide"
)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 2.0rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        font-size: 1.0rem;
        color: #555;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<div class='main-title'>Analisis Penerapan Algoritma Klasifikasi Penyakit</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div class='subtitle'>Perbandingan K-Nearest Neighbor, Decision Tree, dan Naïve Bayes dalam Klasifikasi Penyakit Berdasarkan Gejala</div>",
    unsafe_allow_html=True
)

st.write("---")

# -------------------------------------------------
# DATASET SAMPLE (20 data seperti di HTML)
# -------------------------------------------------
st.header("Sampel Data Penyakit")

st.write(
    "Berikut adalah 20 sampel data dari dataset klasifikasi penyakit "
    "berdasarkan gejala:"
)

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

df_sample = pd.DataFrame(data, columns=columns)

st.dataframe(df_sample, use_container_width=True)

st.write("---")

# -------------------------------------------------
# ANALISIS ALGORITMA & METRIK
# -------------------------------------------------
st.header("Analisis Algoritma Klasifikasi")

st.write(
    "Berikut adalah perbandingan performa tiga algoritma klasifikasi "
    "yang diterapkan pada dataset penyakit:"
)

col_knn, col_dt, col_nb = st.columns(3)

with col_knn:
    st.subheader("K-Nearest Neighbor (KNN)")
    st.write(
        "Algoritma berbasis instance yang mengklasifikasikan data "
        "berdasarkan kedekatan dengan tetangga terdekat."
    )
    st.metric("Akurasi", "87.5%")
    st.metric("Presisi", "85.2%")
    st.metric("Recall", "86.8%")
    st.metric("F1-Score", "86.0%")

with col_dt:
    st.subheader("Decision Tree")
    st.write(
        "Algoritma berbasis pohon keputusan yang membagi data "
        "berdasarkan nilai atribut."
    )
    st.metric("Akurasi", "91.2%")
    st.metric("Presisi", "90.5%")
    st.metric("Recall", "89.8%")
    st.metric("F1-Score", "90.1%")

with col_nb:
    st.subheader("Naïve Bayes")
    st.write(
        "Algoritma probabilistik berdasarkan Teorema Bayes dengan "
        "asumsi independensi antar fitur."
    )
    st.metric("Akurasi", "83.7%")
    st.metric("Presisi", "82.1%")
    st.metric("Recall", "84.3%")
    st.metric("F1-Score", "83.2%")

st.subheader("Perbandingan Performa")

df_metrics = pd.DataFrame(
    {
        "Metrik": ["Akurasi", "Presisi", "Recall", "F1-Score", "Waktu Pelatihan", "Interpretabilitas"],
        "K-NN": ["87.5%", "85.2%", "86.8%", "86.0%", "Sedang", "Rendah"],
        "Decision Tree": ["91.2%", "90.5%", "89.8%", "90.1%", "Cepat", "Tinggi"],
        "Naïve Bayes": ["83.7%", "82.1%", "84.3%", "83.2%", "Sangat Cepat", "Sedang"],
    }
)

st.table(df_metrics)

st.write("---")

# -------------------------------------------------
# SIMULASI PREDIKSI PENYAKIT (LOGIKA SAMA DENGAN JAVASCRIPT)
# -------------------------------------------------
st.header("Simulasi Prediksi Penyakit")
st.write("Pilih gejala yang dialami untuk melihat prediksi dari ketiga algoritma:")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Gejala Umum")
    demam = st.checkbox("Demam")
    batuk = st.checkbox("Batuk")
    kelelahan = st.checkbox("Kelelahan")
    sakit_kepala = st.checkbox("Sakit Kepala")

with col2:
    st.subheader("Gejala Pernapasan & Pencernaan")
    nyeri_tenggorokan = st.checkbox("Nyeri Tenggorokan")
    sesak_napas = st.checkbox("Sesak Napas")
    muntah = st.checkbox("Muntah")
    diare = st.checkbox("Diare")

with col3:
    st.subheader("Gejala Lainnya")
    ruam = st.checkbox("Ruam")
    nyeri_dada = st.checkbox("Nyeri Dada")

# Tombol prediksi
if st.button("Prediksi Penyakit"):
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
        st.warning("Silakan pilih minimal satu gejala untuk melakukan prediksi.")
    else:
        # Logika rule-based sama dengan JavaScript pada HTML
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

        st.subheader("Hasil Prediksi")

        colA, colB, colC = st.columns(3)
        with colA:
            st.markdown("### K-Nearest Neighbor")
            st.info(f"**{knnPrediction}**  \nTingkat keyakinan: {knnConf}")
        with colB:
            st.markdown("### Decision Tree")
            st.success(f"**{dtPrediction}**  \nTingkat keyakinan: {dtConf}")
        with colC:
            st.markdown("### Naïve Bayes")
            st.warning(f"**{nbPrediction}**  \nTingkat keyakinan: {nbConf}")

st.write("---")
st.caption(
    "Aplikasi ini dibangun berdasarkan template HTML analisis klasifikasi penyakit "
    "yang kemudian diadaptasi ke dalam Streamlit. :contentReference[oaicite:0]{index=0}"
)
