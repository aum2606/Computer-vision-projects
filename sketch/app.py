import streamlit as st
from PIL import Image
from io import BytesIO
import numpy as np
import cv2


def convert_to_water_color_sketch(input_image):
    image1 = cv2.edgePreservingFilter(input_image,flags=2,sigma_s=50,sigma_r=0.8)
    image_water_color = cv2.stylization(image1,sigma_r=0.5,sigma_s=100)
    return image_water_color

def pencil_sketch(input_image):
    pencil_sketch_image, pencil_color_sketch = cv2.pencilSketch(input_image,sigma_r=0.07,sigma_s=50,shade_factor=0.0825)
    return (pencil_sketch_image)

def load_image(image):
    img = Image.open(image)
    return img


def main():
    st.title("Image Processing App")
    st.write("This app allows you to upload an image and apply different image processing techniques to it")
    st.subheader("Please upload your image")
    image_file = st.file_uploader("Upload an image", type=["jpg", "png"])
    if image_file is not None:
        option = st.selectbox('How would you like to convert the image',
                              ('Water Color Sketch', 'Pencil Sketch'))
        if option == 'Water Color Sketch':
            image = Image.open(image_file)
            final_sketch = convert_to_water_color_sketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)
            col1,col2 = st.columns(2)
            with col1:
                st.header("Original image")
                st.image(load_image(image_file),width=250)
            with col2:
                st.header("Water Color Sketch")
                st.image(im_pil,width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.download_button(
                    label='Download image',
                    data = byte_im,
                    file_name='water_color_sketch.png',
                    mime='image/png'
                )
        if option == 'Pencil Sketch':
            image = Image.open(image_file)
            final_sketch = pencil_sketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)
            col1,col2 = st.columns(2)
            with col1:
                st.header("Original image")
                st.image(load_image(image_file),width=250)
            with col2:
                st.header("Pencil sketch")
                st.image(im_pil,width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.download_button(
                    label='Download image',
                    data = byte_im,
                    file_name='pencil_sketch.png',
                    mime='image/png'
                )


if __name__ == '__main__':
    main()