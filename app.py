import streamlit as st

st.title("Tes Streamlit")
st.write

# ============================
# HEADER
# ============================
st.markdown("""
<style>
h1 {
    text-align: center;
    color: #2c3e50;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Analisis Penerapan Algoritma Klasifikasi Penyakit</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Perbandingan KNN, Decision Tree, dan Naïve Bayes Berdasarkan Gejala</p>", unsafe_allow_html=True)

st.divider()

# ============================
# FORM INPUT GEJALA
# ============================
st.header("Simulasi Prediksi Penyakit")

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

# ============================
# TOMBOL PREDIKSI
# ============================
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
        "nyeriDada": nyeri_dada
    }

    symptom_count = sum(symptoms.values())

    if symptom_count == 0:
        st.warning("⚠ Pilih minimal satu gejala untuk melakukan prediksi.")
        st.stop()

    # =====================================
    # LOGIKA PREDIKSI (SAMA PERSIS DENGAN HTML)
    # =====================================
    if demam and batuk and nyeri_tenggorokan:
        knn = ("Flu", "87%")
        dt = ("Flu", "92%")
        nb = ("Flu", "85%")

    elif demam and ruam and not batuk:
        knn = ("Demam Berdarah", "82%")
        dt = ("Demam Berdarah", "89%")
        nb = ("Demam Berdarah", "79%")

    elif demam and sesak_napas and batuk:
        knn = ("COVID-19", "85%")
        dt = ("COVID-19", "91%")
        nb = ("COVID-19", "83%")

    elif demam and muntah and diare:
        knn = ("Gastroenteritis", "84%")
        dt = ("Gastroenteritis", "88%")
        nb = ("Gastroenteritis", "81%")

    elif sakit_kepala and not demam:
        knn = ("Migrain", "79%")
        dt = ("Migrain", "85%")
        nb = ("Migrain", "76%")

    elif sesak_napas and nyeri_dada:
        knn = ("Pneumonia", "86%")
        dt = ("Pneumonia", "90%")
        nb = ("Pneumonia", "82%")

    elif batuk and nyeri_tenggorokan and not demam:
        knn = ("Alergi", "81%")
        dt = ("Alergi", "87%")
        nb = ("Alergi", "78%")

    elif demam and muntah and not diare:
        knn = ("Tifus", "83%")
        dt = ("Tifus", "86%")
        nb = ("Tifus", "80%")

    else:
        knn = dt = nb = ("Tidak dapat diprediksi dengan pasti", "")

    # ============================
    # OUTPUT PREDIKSI
    # ============================
    st.subheader("Hasil Prediksi")

    colA, colB, colC = st.columns(3)

    with colA:
        st.markdown("### 🟥 K-Nearest Neighbor")
        st.info(f"**{knn[0]}**  \nKeyakinan: *{knn[1]}*")

    with colB:
        st.markdown("### 🟩 Decision Tree")
        st.success(f"**{dt[0]}**  \nKeyakinan: *{dt[1]}*")

    with colC:
        st.markdown("### 🟨 Naïve Bayes")
        st.warning(f"**{nb[0]}**  \nKeyakinan: *{nb[1]}*")

    st.divider()


# ============================
# INFORMASI TAMBAHAN
# ============================
st.header("Perbandingan Performa Algoritma")

st.table({
    "Metrik": ["Akurasi", "Presisi", "Recall", "F1-Score"],
    "KNN": ["87.5%", "85.2%", "86.8%", "86.0%"],
    "Decision Tree": ["91.2%", "90.5%", "89.8%", "90.1%"],
    "Naïve Bayes": ["83.7%", "82.1%", "84.3%", "83.2%"]
})

st.caption("Sumber logika & tampilan berasal dari file HTML asli. :contentReference[oaicite:1]{index=1}")

st.write("---")
st.write("© 2023 – Aplikasi Streamlit Analisis Penyakit")

