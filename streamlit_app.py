import streamlit as st

st.title("#THANKERENBANGET")
st.write(
    "Mari bermain dengan gw [docs.streamlit.io](https://docs.streamlit.io)"
)
st.markdown("*Fathan* is **really** ***cool***.")
st.markdown('''
    :red[Fathan] :orange[keren] :green[banget] :blue[anjay] :violet[mabar]
    :gray[profesional] :rainbow[mantap].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
st.set_page_config(page_title="Kalkulator Sederhana", page_layout="centered")

# Judul Aplikasi
st.title("🧮 Kalkulator Interaktif Streamlit")
st.write("Aplikasi web sederhana untuk melakukan operasi matematika dasar.")

# Layout kolom untuk input
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Masukkan angka pertama:", value=0.0)

with col2:
    num2 = st.number_input("Masukkan angka kedua:", value=0.0)

# Pilihan Operasi
operasi = st.selectbox(
    "Pilih operasi matematika:",
    ("Penjumlahan (+)", "Pengurangan (-)", "Perkalian (x)", "Pembagian (/)")
)

# Tombol Hitung
if st.button("Hitung", type="primary"):
    if operasi == "Penjumlahan (+)":
        hasil = num1 + num2
        simbol = "+"
    elif operasi == "Pengurangan (-)":
        hasil = num1 - num2
        simbol = "-"
    elif operasi == "Perkalian (x)":
        hasil = num1 * num2
        simbol = "×"
    elif operasi == "Pembagian (/)":
        if num2 != 0:
            hasil = num1 / num2
            simbol = "÷"
        else:
            st.error("Error: Tidak bisa melakukan pembagian dengan nol (0)!")
            hasil = None

    # Tampilkan hasil jika tidak ada error
    if hasil is not None:
        st.success(f"Hasil dari **$num1$ $simbol$ $num2$ = $hasil$**")

sentiment_mapping = ["satu", "dua", "tiga", "empat", "lima"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"Terimakasih atas bintang {sentiment_mapping[selected]}.")
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"Memberi: {sentiment_mapping[selected]}")
