import streamlit as st

pages = {
    "Homepage": [
        st.Page("homepage.py", title="Home")
    ],
    "Locations": [
    st.Page("benson.py", title="Benson"),
    st.Page("hillcrest.py", title="Hillcrest"),
    st.Page("summit.py", title="Summit"),
    st.Page("meridian.py", title="Meridian")
    ]
}

pg = st.navigation(pages)

pg.run()
