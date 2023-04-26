
import streamlit as st
from datetime import date
import os
import glob as glob

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

HOMEPAGE_CONTENT='''
#####  This project is initiated by the Omdena Cameroon Chapter to solve Real World Problems.

### The problem
Mapping the extent of land use and land cover categories over time is essential for better environmental monitoring, urban planning, nature protection, conflict prevention, disaster reduction, rescue planning as well as long-term climate adaptation efforts.

This initiative’s goal is to build a Machine Learning model that accurately classifies Land Use and Land Cover (LULC) in satellite imagery. Then use the trained model to automatically generate the LULC map for a region of interest. Finally, create a Web GIS dashboard containing the LULC Map of the region of interest.

The project results will be made open source. The aim is to help connect local organizations and communities to use AI tools and Earth Observations data as an action to cope with local challenges such as land use monitoring and the world’s most critical challenges like climate change. We also hope to encourage citizen science by open-source the dataset and code.

### The goals
The goals of this project are: 
+ The Web GIS dashboard containing LULC Map of the region of interest.
+ The ML models(s) with best performance.
+ The datasets collected during the project on Google Drive for open access.
+ GitHub Repo with Well-documented open source code.
+ Documentation of the work and approach.
''' 

st.set_page_config(
    page_title="Automating Land Use and Land Cover Mapping Using Computer Vision and Satellite Imagery",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)


with st.container():
    col1, col2 = st.columns([1,2], gap="small")
    with col1:
        st.image(PROFILE_IMAGE, width=300)
    with col2:
        st.markdown(HEADER_STYLE, unsafe_allow_html=True)
        st.title(PAGE_TITLE)
with st.container():
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(HOMEPAGE_CONTENT, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
