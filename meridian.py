import streamlit as st
from PIL import Image

st.title("Meridian")
st.subheader("Adorable 4B3B Cottage walk to Purdue +Game Arcade!")
st.image('meridian_backdeck.jpg')
st.write("how many bedrooms and bathrooms")

bed, bath = st.columns(2, border=True)

with bed:
    st.write("this is where you can put pictures and descriptions")
 
with bath:
    st.write("same for bathrooms")

st.subheader("Amenities")
st.write("blah blah blah")