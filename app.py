import streamlit as st

st.title("Penentu Aktivitas Gabut")

# Input nama
nama = st.text_input("Masukkan nama kamu:")

# Input mood
mood = st.selectbox(
    "Mood kamu:",
    ["Bosan", "Capek", "Semangat"]
)

# Input waktu hari
waktu = st.selectbox(
    "Sekarang waktu:",
    ["Pagi", "Siang", "Malam"]
)

# Tombol
if st.button("Cari Aktivitas"):
    if nama == "":
        st.warning("Masukkan nama dulu!")
    else:
        # PAGI
        if waktu == "Pagi" and mood == "Semangat":
            hasil = f" {nama}, olahraga atau mulai aktivitas produktif 💪"
        elif waktu == "Pagi" and mood == "Capek":
            hasil = f" {nama}, santai dulu sambil minum kopi"
        elif waktu == "Pagi" and mood == "Bosan":
            hasil = f" {nama}, scroll santai atau nonton video ringan"

        # SIANG
        elif waktu == "Siang" and mood == "Semangat":
            hasil = f" {nama}, lanjut kerja / belajar atau coba hal baru"
        elif waktu == "Siang" and mood == "Capek":
            hasil = f" {nama}, power nap bentar atau istirahat"
        elif waktu == "Siang" and mood == "Bosan":
            hasil = f" {nama}, main game atau nonton film"

        # MALAM
        elif waktu == "Malam" and mood == "Semangat":
            hasil = f" {nama}, belajar santai atau self improvement"
        elif waktu == "Malam" and mood == "Capek":
            hasil = f" {nama}, waktunya tidur biar fresh besok"
        elif waktu == "Malam" and mood == "Bosan":
            hasil = f" {nama}, doomscrolling bentar tapi jangan kebablasan 😆"

        else:
            hasil = f" {nama}, coba cari makanan atau jalan santai"

        st.success(hasil)