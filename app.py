import streamlit as st
from PIL import Image

st.set_page_config(page_title="CV Dashboard", layout="wide")

st.title("🖥️ Computer Vision Dashboard")
st.write("Choose any task below:")

col1, col2, col3 = st.columns(3)

with col1:
    filter_btn = st.button("🎨 Image Filters")

with col2:
    crop_btn = st.button("✂️ Image Crop")

with col3:
    emoji_btn = st.button("😂 Emoji Image")

if filter_btn:
    st.header("🎨 Image Filter Task")
    img = Image.open("image.png")
    st.image(img, caption="Original Image")

    st.write("Yaha filter wala code add hoga")

elif crop_btn:
    st.header("✂️ Image Crop Task")
    img = Image.open("image.png")

    width = st.slider("Width", 50, img.width, 300)
    height = st.slider("Height", 50, img.height, 200)

    cropped = img.crop((0, 0, width, height))
    st.image(cropped, caption="Cropped Image")

elif emoji_btn:
    st.header("😂 Emoji Task")
    emoji = Image.open("emoji.png")
    st.image(emoji, caption="Emoji Image")

else:
    st.info("👈 Upar se koi task select karo")