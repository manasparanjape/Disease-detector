import streamlit as st
from PIL import Image as img
import pickle as pk
import numpy as np

pixels = 150
dimensions = (pixels, pixels)
bins = 3
model_filename = "model_" + str(bins) + "_bins.sav"

def load_image(image_file):
    im = img.open(image_file)
    return im

def predict_2_bins(image, model):
    image = image.resize(dimensions)
    image = image.convert('L')
    image = np.asarray(image)
    image = np.reshape(image, (pixels, pixels, 1))
    image = np.expand_dims(image, 0)
    image = image / 255.0
    result = model.predict(image)
    result = np.argmax(result)
    if result == 0:
        return "The image shown does not indicate pneumonia in the patient"
    elif result == 1:
        return "Unfortunately, the image indicates pneumonia in the patient"

def predict_3_bins(image, model):
    image = image.resize(dimensions)
    image = image.convert('L')
    image = np.asarray(image)
    image = np.reshape(image, (pixels, pixels, 1))
    image = np.expand_dims(image, 0)
    image = image / 255.0
    result = model.predict(image)
    result = np.argmax(result)
    if result == 0:
        return "The image shown does not indicate pneumonia in the patient"
    elif result == 1:
        return "Unfortunately, the image indicates bacterial pneumonia in the patient"
    elif result == 2:
        return "Unfortunately, the image indicates viral pneumonia in the patient"

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
            
            image = img.open(image_file)
            model = pk.load(open(model_filename, "rb"))
            if bins == 2:
                result = predict_2_bins(image, model)
                st.write(result)
            elif bins == 3:
                result = predict_2_bins(image, model)
                st.write(result)



    
    elif choice == "Dataset":
        st.subheader("Dataset")

    elif choice == "DocumentFiles":
        st.subheader("DocumentFiles")


if __name__ == "__main__":
    main()
