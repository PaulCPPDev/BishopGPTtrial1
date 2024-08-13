import streamlit as st
import streamlit_lottie

def app():
    st.title("BishopGPT")
    st.write("Automate your life with BishopGPT")
    with st.echo():
        st.lottie("https://lottie.host/a304d8e3-2fea-426d-82c4-866acb84244e/mQ1luxAuNq.json")