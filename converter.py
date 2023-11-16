import streamlit as st
from PIL import Image
import io

file = st.file_uploader(label="Select file")

if file:
    # Conversion
    img = Image.open(file)
    gray_img = img.convert("L")

    # Viewing
    st.image(img)
    st.image(gray_img)

    # Conversion PIL.Image to io.BytesIO
    gray_img_bytes = io.BytesIO()
    gray_img.save(gray_img_bytes, format="JPEG")

    # Generating new name for BW image file
    original_name = file.name
    file_format = original_name.split('.')[-1]
    file_name = original_name.strip('.' + file_format) + "_bw"
    new_full_name = file_name + '.' + file_format
    st.text("Original name: " + original_name)
    st.text("New name: " + new_full_name)

    # Saving to the hard drive
    st.download_button("Save image", help="Save image to the hard drive",
                       data=gray_img_bytes,
                       file_name=new_full_name)
