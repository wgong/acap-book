import streamlit as st
from streamlit_card import card

st.title("Streamlit Card - demo")

images = [
    "https://cdn.pixabay.com/photo/2023/12/13/06/47/footprints-8446394_1280.jpg",
    "https://www.gettyimages.com/photos/pacific-ocean",  
    "https://www.istockphoto.com/photos/ocean",
]
texts = ["This is a test card", "This is a subtext - very long ........... ............. ......", "这是一个副标题"]

res = card(
    title="Streamlit Card",
    text=texts,
    url="https://github.com/gamcoh/st-card",
    image=images[0],
    styles={
        "card": {
            "width": "300px",
            "height": "300px",
            "border-radius": "10px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            "display": "flex",
            "flex-direction": "column",
            "justify-content": "flex-start",
            "padding-top": "10px",  
            "padding-left": "10px",            
        },
        "title": {
            "color": "red",
            "text-align": "left",           
            "width": "100%",
        },
        "text": {
            "color": "yellow",
            "text-align": "left",            
            "width": "100%",
        },
        "div": {
            "display": "flex",
            "flex-direction": "column",
            "justify-content": "flex-start",
            "align-items": "flex-start",
            "padding": "20px",
        },
    },
)