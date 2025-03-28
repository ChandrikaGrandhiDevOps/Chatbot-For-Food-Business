import streamlit as st
import langchain_helper


st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian","Mexican","Japanees","Korean","Thai","American","Arabic"))

def generate_restaurant_name_and_items(cuisine):
    return {
        'restaurant_name' : 'curry delight',
        'menu_items': 'tea,samosa'
    }
if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response ['menu_items'].strip().split(",")
    st.write("**MENU ITEMS**")
    for item in menu_items:
        st.write("-", item)
