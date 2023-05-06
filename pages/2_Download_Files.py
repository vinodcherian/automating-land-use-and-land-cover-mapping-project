
import streamlit as st
from project_utils.azure_blob_storage_helper

option = st.selectbox(
    'Please select the ROI region option to download the files : ',
    ('Full Camerron region','Adamawa','Central','East','Far North','Littoral','North','Northwest','South','Southwest','West'))

st.write('You selected:', option)

if option == 'Full Camerron region':
  pass
elif option in ['Adamawa','Central','East','Far North','Littoral','North','Northwest','South','Southwest','West']:
  pass
else:
  st.write("Please select a valid option")

#def get_full_country_data():
#  return get_full_country_storage_blob()
#
#def list_all_files(province):
#  return 
#
#def get_provinces_data():
#  return  
#def get_full_country_storage_blob():
#  return 
#
#def list_all_storage_blobs():
#  return 
#
#def get_provinces_storage_blob():
#
