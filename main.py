# import libraries
import streamlit as st
import tkinter as tk
from tkinter import filedialog
from streamlit_cropper import st_cropper
from PIL import Image
import os



# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button

st.title('01 CHOOSE THE WORKING DIRECTORY')
clicked = st.button('Select a folder')
if clicked:
    path = st.text_input('Selected folder:', filedialog.askdirectory(master=root))
    os.chdir(path)

st.title('02 LOCATE THE CARTOUCHE ON THE IMAGE')
st.set_option('deprecation.showfileUploaderEncoding', False)
# Upload an image and set some options for demo purposes
img_file = "cartouche.png"
realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=False)
box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
aspect_dict = {
        "1:1": (1, 1),
        "16:9": (16, 9),
        "4:3": (4, 3),
        "2:3": (2, 3),
        "Free": None
    }
aspect_ratio = aspect_dict[aspect_choice]
if img_file:
    img = Image.open(img_file)
    if not realtime_update:
        st.write("Double click to save crop")
    # Get a cropped image from the frontend
    cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
    # Manipulate cropped image at will
    st.write("Preview")
    #_ = cropped_img.thumbnail((150,150))
    st.image(cropped_img)

