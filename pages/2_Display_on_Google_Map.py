#import streamlit as st
#import json
#import geojson
#import geopandas as gpd
#import ee
#import geemap
#import src.gee as gee

#import streamlit as st
#from streamlit_folium import folium_static
#import folium
#import ee
#import geemap.eefolium as geemap

# Data from the downloaded JSON file
#json_data = '''
#{
#   "type":"service_account",
#   "project_id":"...",
#   "private_key_id":"...",
#   "private_key":"...",
#   "client_email":"...",
#   "client_id":"...",
#   "auth_uri":"...",
#   "token_uri":"...",
#   "auth_provider_x509_cert_url":"...",
#   "client_x509_cert_url":"..."
#}
#''
#service_account= '@'
#predicted_image_asset="users/roygeoai/OMDENACMRLC2021"
#
#
#AOI_GEOJSON= st.secrets["cameroon_aoi_bbx"] #'./dla_aoi_bbx_200_m.geojson'
#predicted_image_asset_path=st.secrets("predicted_image_asset")
#json_data = st.secrets["json_data"]
#service_account = st.secrets["service_account"]
#
#
#json_object = json.loads(json_data, strict=False)
#json_object = json.dumps(json_object)
#credentials = ee.ServiceAccountCredentials(service_account, key_data=json_object)
##ee.Initialize(credentials)
#geemap.ee_initialize()
#image=ee.Image()
##image=ee.Image("https://code.earthengine.google.com/?asset=users/roygeoai/OMDENACMRLC2021")
#databox = gpd.read_file(AOI_GEOJSON)
#aoi = geemap.geopandas_to_ee(databox).geometry()
#m = geemap.Map()
#m.centerObject(aoi,7)
#m.addLayer(image)
#m.addLayerControl()
## call to render Folium map in Streamlit
#folium_static(m)

import ee
import os
#import geemap
import json
import streamlit as st
import geemap.foliumap as geemap
import geopandas as gpd
from project_utils.page_layout_helper import  main_header
main_header()
AOI_GEOJSON = st.secrets["cameroon_aoi_bbx"] 
PREDICTED_IMAGE_ASSET_PATH = st.secrets["predicted_image_asset"]
JSON_DATA = st.secrets["google_map_auth_json_data"]

json_object = json.loads(JSON_DATA, strict=False)
json_object = json.dumps(json_object)
os.environ['EARTHENGINE_TOKEN']=json_object
geemap.ee_initialize(token_name='EARTHENGINE_TOKEN', auth_mode='notebook', service_account=True)
m = geemap.Map(center=(7.3696, 12.3446), zoom=6)
image=ee.Image(PREDICTED_IMAGE_ASSET_PATH)
#image=ee.Image("https://code.earthengine.google.com/?asset=users/roygeoai/OMDENACMRLC2021")
databox = gpd.read_file(os.path.abspath(AOI_GEOJSON))
aoi = geemap.geopandas_to_ee(databox).geometry()
m.centerObject(aoi,6)
m.addLayer(image)
m.addLayerControl()
m.to_streamlit()


