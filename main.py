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

