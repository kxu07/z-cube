import streamlit as st
from PIL import Image

st.title("Benson")
st.subheader("Modern Spacious Retreat by Purdue/Nature & Arcade")
st.image('benson_exterior.jpg')
st.write("how many bedrooms and bathrooms")

bed, bath = st.columns(2, border=True)

with bed:
    st.write("this is where you can put pictures and descriptions")
 
with bath:
    st.write("same for bathrooms")

st.subheader("Amenities")
st.write("blah blah blah")