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


def load_audio_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


try:
    audio_base64 = load_audio_base64("backsound.mp3")

    st.components.v1.html(
        f"""
        <div style="background: #f1f3f4; padding: 10px; border-radius: 30px; display: inline-block;">
            <span style="font-family: sans-serif; font-size: 14px; margin-right: 10px; vertical-align: middle;">🎵 Backsound:</span>
            <audio controls autoplay loop style="vertical-align: middle; height: 32px;">
                <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
                Browser kamu tidak mendukung pemutar audio ini.
            </audio>
        </div>
        """,
        height=70,
    )

except FileNotFoundError:
    st.error(
        "❌ File 'backsound.mp3' tidak ditemukan! Pastikan file lagunya ada di folder yang sama dengan app.py kamu."
    )

st.write("---")
st.subheader("Dashboard Utama")
st.write("Silakan berinteraksi dengan website ini.")
