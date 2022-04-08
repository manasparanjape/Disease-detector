import streamlit as st
from PIL import Image as img
import pickle as pk
import numpy as np

model_filename = 'model.sav'
pixels = 150
dimensions = (pixels, pixels)

def load_image(image_file):
    im = img.open(image_file)
    return im

def main():
    st.title("Welcome to Manas' Pneumonia Detector")

    menu = ["Image", "Dataset","DocumentFiles","About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Image":
        st.subheader("Image")
        image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

        if image_file is not None:
            file_details = {"filename":image_file.name, "filetype":image_file.type, "filesize":image_file.size}
            st.write(file_details)
            st.image(load_image(image_file), width=250)
            
            model = pk.load(open(model_filename, 'rb'))
            image = img.open(image_file)
            image = image.resize(dimensions)
            image = image.convert('L')
            image = np.asarray(image)
            image = np.reshape(image, (pixels, pixels, 1))
            image = np.expand_dims(image, 0)
            image = image / 255.0
            result = model.predict(image)
            st.write(result)
            result = np.argmax(result)
            if result == 0:
                st.write("The image shown does not indicate pneumonia in the patient")
            elif result == 1:
                st.write("Unfortunately, the image indicates pneumonia in the patient")


    
    elif choice == "Dataset":
        st.subheader("Dataset")

    elif choice == "DocumentFiles":
        st.subheader("DocumentFiles")


if __name__ == "__main__":
    main()
