
import streamlit as st
import os
import io
from datetime import date
import glob as glob
import pandas as pd
import numpy as np
from PIL import Image
import base64
from streamlit_image_comparison import image_comparison

MODEL_PATH = './Models/'

ALLOWED_EXTENSIONS = ["jpg","jpeg","png"]


WIDTH=300

HEIGHT=300


HEADER_STYLE=f"""<style>
 	    [data-testid="stToolbar"]{{
	    visibility: hidden;
	    }}
            footer {{
            visibility: hidden;
            position: relative;
            }}
            footer:before {{
            visibility: visible;
            position: relative;
	          content: "Project by Omdena Cameroon Chapter - {date.today().year}"
            }}
        </style>
    """

@st.cache_resource
def get_model(path):
  return path

def modelpredict(model, upload_image_obj):
  img_arr = np.array(upload_image_obj) 
  return img_arr

model_obj = get_model(os.path.abspath(MODEL_PATH))

satellite_input_image_obj=Image.open(os.path.abspath('./Models/satellite_input_image.png'))
image_comparision_right_image_obj=Image.open(os.path.abspath('./Models/image_comparision_right_image.png'))
predicted_image_from_input_obj=Image.open(os.path.abspath('./Models/predicted_image_from_input.png'))
image_comparision_left_image_obj=Image.open(os.path.abspath('./Models/image_comparision_left_image.png'))
image_with_class_label_obj=Image.open(os.path.abspath('./Models/image_with_class_label.png'))

st.markdown(HEADER_STYLE, unsafe_allow_html=True)
st.divider()
st.sidebar.markdown("### Upload a ROI Image of Format(jpeg,jpg,png): ")
uploaded_image_file = st.sidebar.file_uploader("", type=ALLOWED_EXTENSIONS)
if uploaded_image_file is not None:

  #uploaded_image_filename=uploaded_image_file.name
  #imageobj=Image.open(uploaded_image_file)
  imageobj=satellite_input_image_obj
  #model_predict_result=modelpredict()
  col1, col2 = st.columns([6,6], gap="small")
  with col1:
    st.markdown('### **Uploaded Image**',unsafe_allow_html=True)
    st.image(imageobj,width=WIDTH)  #300 #640
  with col2:
    st.markdown('### **Predict uploaded image**',unsafe_allow_html=True)
    st.image(predicted_image_from_input_obj, width=WIDTH) 
  st.info('## The predicted model accuracy for the uploaded image is 53%')
  st.markdown("<br>", unsafe_allow_html=True)
  image_comparison(
    img1=image_comparision_left_image_obj,
    img2=image_comparision_right_image_obj,
    label1="Original Image",
    label2="Label Classes",
    width=700,
    starting_position=50,
    show_labels=True,
    make_responsive=True,
    in_memory=True,
)
  st.image(image_with_class_label_obj, width=500) 
  #st.plotly_chart(bar_chart_fig)
