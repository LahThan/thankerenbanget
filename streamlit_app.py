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

def putar_backsound(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode()

    html_audio = f"""
    <audio autoplay loop style="display:none;">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(html_audio, unsafe_allow_html=True)


putar_backsound("backsound.mp3")
st.title("Web Keren Saya 🚀")
st.write("Dengarkan lagu backsound-nya yang sedang berjalan di latar belakang!")
