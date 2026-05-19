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
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")
