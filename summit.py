import streamlit as st
from PIL import Image

st.title("Summit")
st.subheader("Spacious 4BR Home Walks to Purdue, Golf, & Arcade!")
st.image('summit_exterior.jpg')
st.write("how many bedrooms and bathrooms")

bed, bath = st.columns(2, border=True)

with bed:
    st.write("this is where you can put pictures and descriptions")
 
with bath:
    st.write("same for bathrooms")

st.subheader("Amenities")
st.write("blah blah blah")
