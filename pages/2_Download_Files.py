
import streamlit as st
from project_utils.page_layout_helper import  main_header
#from project_utils.azure_blob_storage_helper import get_file_gdrive, fetch_model, gdal_uploaded_image_array, model_result, image_to_rgb, predicted_image_with_class_label


def main():
  main_header()
  with st.container():
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

    
if __name__ == "__main__":
  main()  

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