import streamlit as st
from PIL import Image


st.title("Z Cube Air BnBs")
st.subheader(
    "About us"
)
col1, col2 = st.columns(2)

with col1:
    image = Image.open("/workspaces/z-cube/images/mockup_about.jpg")
    st.image(image)
with col2:  
    st.write("text blah blah blah")
    st.write("For more information on each house, see the navigation bar on your left.")

st.subheader(
    "Contact us directly for discounted booking!"
)

st.markdown('<a href="mailto:kaylaxu@gmail.com">Email: your email here</a>', unsafe_allow_html=True)
