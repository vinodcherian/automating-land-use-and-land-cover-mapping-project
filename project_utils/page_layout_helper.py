from datetime import date
import os
import glob as glob
import streamlit as st
import pathlib

PROFILE_IMAGE="https://omdena.com/wp-content/uploads/2023/01/Douala-Cameroon-Chapter.png"


BACKGROUND_IMAGE="https://omdena.com/wp-content/uploads/2023/01/Automating-Land-Use-and-Land-Cover-Mapping-Using-Computer-Vision-and-Satellite-Imagery-480x251.png"


HEADER_STYLE=f"""<style>
	    [data-testid="stToolbar"]{{
	    visibility: hidden;
	    top: -50px;
	    }}
            [data-testid="stImage"]{{
            height: 300px;
            width: 300px;
            }}
            [data-testid="stImage"] > img{{
            height: 300px;
            width: 300px;
            padding-top: 40%;
            padding-bottom: 10%;
            padding-left: 15%;
            padding-right: 10%;
            }}
            #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(1) > div{{
            background-image: url("{BACKGROUND_IMAGE}");
            background-size: cover; 
            background-position: center;
            }}
            #automating-land-use-and-land-cover-mapping-using-computer-vision-and-satellite-imagery{{
            height: 250px;
            }}
            #automating-land-use-and-land-cover-mapping-using-computer-vision-and-satellite-imagery > div {{
            bottom: 1%;
            position: absolute;
            color: white;
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


PAGE_TITLE="Automating Land Use and Land Cover Mapping Using Computer Vision and Satellite Imagery"


def get_page_title():
  return PAGE_TITLE

def set_page_title():
  st.set_page_config(
    page_title=get_page_title()
)

def set_page_settings():
  st.set_page_config(
    page_title=get_page_title(),
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded", 
)

def main_header():
  with st.container():
      left_side, right_side = st.columns([1,2], gap="small")
      with left_side:
          st.image(PROFILE_IMAGE, width=300)          
      with right_side:
          st.markdown(HEADER_STYLE, unsafe_allow_html=True)
          st.title(PAGE_TITLE)
  st.markdown("<br>", unsafe_allow_html=True)
