
import streamlit as st

from lang_chain_helper import get_restaurant_name


st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", (
    "Indian", "American", "Mexican", "Turkish"
))


if cuisine:
    response = get_restaurant_name(cuisine)

    st.header(response['restaurant_name'])
    st.write("Menu Items:")
    menu_items = response['menu_items'].split(',')

    for item in menu_items:
        st.write("- ", item)
