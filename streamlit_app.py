import base64
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
sentiment_mapping = ["satu", "dua", "tiga", "empat", "lima"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"Terimakasih atas bintang {sentiment_mapping[selected]}.")
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"Memberi: {sentiment_mapping[selected]}")


st.title("Web Keren Saya 🚀")

with st.sidebar:
    st.write("🎵 **Musik Latar Belakang**")

    st.audio("backsound.mp3", format="audio/mp3", autoplay=True, loop=True)

    st.caption(
        "Tip: Jika suara belum muncul, tekan tombol 'Play' di atas akibat aturan browser."
    )


st.write("---")
st.subheader("Isi Halaman Web")
st.write(
    "Sekarang halaman web kamu memiliki panel pemutar musik mini yang manis di sebelah kiri (Sidebar)!"
)


st.title("Web Keren Saya 🚀")
st.write("Dengarkan lagu backsound-nya yang sedang berjalan di latar belakang!")
