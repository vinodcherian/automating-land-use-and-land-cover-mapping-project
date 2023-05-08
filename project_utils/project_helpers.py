from tensorflow.keras.models import load_model
from PIL import Image
import os
import io
import numpy as np
import pandas as pd
import gdown
from osgeo import gdal
import matplotlib
import matplotlib.pyplot as plt

# Set the patch size and stride
PATCH_SIZE = 256
STRIDE = 128

def get_file_gdrive(input_url,output_filename):
  return gdown.download(input_url, output_filename, quiet=False)

def fetch_model(modelpath):
  if os.path.exists(os.path.abspath(modelpath)):
    model=load_model(modelpath, compile=False)
  else:
    input_url = 'https://drive.google.com/uc?id=1O6Cb0-_Tz9Ra4S976owgYSbWSRqvaMJy'
    #output_filename = '/content/drive/MyDrive/Omdena_Projects/Automating_Land_Use_and_Land_Cover_Mapping_StreamApp/models/TRAINED_MODEL_5.hdf5'
    os.mkdir(os.path.dirname(modelpath).replace('.','')) 
    get_file_gdrive(input_url, modelpath)
    model=load_model(modelpath, compile=False)
  return model

def gdal_uploaded_image_array(upload_image_obj):
  data_array = upload_image_obj.read()
  drv = gdal.GetDriverByName("GTiff")
  gdal_image = drv.Create("256.tif", 256, 256, 4, gdal.GDT_Byte)
  gdal_image = None
  gdal.FileFromMemBuffer("/vsimem/256.tif", data_array)
  gdal_image = gdal.Open("/vsimem/256.tif")
  gdal_image_array = np.transpose(gdal_image.ReadAsArray(), (1, 2, 0))
  gdal_image = None
  if os.path.exists(os.path.abspath("256.tif")):
    os.remove(os.path.abspath("256.tif"))
  return gdal_image_array

def model_result(model, gdal_image_array):
  num_patches_x = int(np.ceil((gdal_image_array.shape[0] - PATCH_SIZE) / STRIDE)) + 1
  num_patches_y = int(np.ceil((gdal_image_array.shape[1] - PATCH_SIZE) / STRIDE)) + 1
  num_patches = num_patches_x * num_patches_y

  predicted_patches = np.zeros((num_patches, PATCH_SIZE, PATCH_SIZE, 8))

  for i in range(num_patches_x):
      for j in range(num_patches_y):
          x1 = i * STRIDE
          y1 = j * STRIDE
          x2 = x1 + PATCH_SIZE
          y2 = y1 + PATCH_SIZE
          patch = gdal_image_array[x1:x2, y1:y2, :]
          prediction = model.predict(np.expand_dims(patch, axis=0))
          predicted_patches[i*num_patches_y+j, :, :, :] = prediction[0]
  
  predicted_image_array = np.zeros((gdal_image_array.shape[0], gdal_image_array.shape[1], 8))
  count_array = np.zeros((gdal_image_array.shape[0], gdal_image_array.shape[1]))
  for i in range(num_patches_x):
      for j in range(num_patches_y):
          x1 = i * STRIDE
          y1 = j * STRIDE
          x2 = x1 + PATCH_SIZE
          y2 = y1 + PATCH_SIZE
          predicted_image_array[x1:x2, y1:y2, :] += predicted_patches[i*num_patches_y+j, :, :, :]
          count_array[x1:x2, y1:y2] += 1

  predicted_image_array = predicted_image_array / np.expand_dims(count_array, axis=-1)
  return predicted_image_array

def image_to_rgb(predicted_image_array):
  return Image.fromarray(np.uint8(predicted_image_array.argmax(axis=-1)))

def predicted_image_with_class_label(predicted_image_array):
  # Get predicted class indices from one-hot encoded array
  predicted_class_indices = np.argmax(predicted_image_array, axis=-1)
  # Map predicted class indices to original values
  mapping_reverse = {0: 10, 1: 20, 2: 30, 3: 40, 4: 50, 5: 60, 6: 80, 7: 90}
  map_predicted = np.vectorize(mapping_reverse.get)
  predicted_class_indices_mapped = map_predicted(predicted_class_indices)
  # Flatenning both the Ground Truth Labels and the Predictions 
  predicted_class_indices_mapped_flat = predicted_class_indices_mapped.flatten()

  # Create a dictionary to map class numbers to labels
  class_labels = {
    10: "Tree Cover",
    20: "Shrubland",
    30: "Grassland",
    40: "Cropland",
    50: "Built-Up",
    60: "Bare / Sparse Vegetation",
    80: "Permanent Water Bodies",
    90: "Herbaceous Wetland",
}

  for i in np.unique(predicted_class_indices_mapped_flat): 
    print(f"{class_labels[i]}")




  # Define the custom colors for the color map
  colors = [ '#1f77b4','#006400', '#ffbb22ff', '#ffff4c', '#f096ff', '#fa0000', '#b4b4b4', '#f0f0f0', '#0064c8', '#0096a0', '#00cf75', '#fae6a0']

  values = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 100]
  # Create a ListedColormap object with the custom colors
  cmap_esa = matplotlib.colors.ListedColormap(colors)

  # Or we can use a dic
  label_dic = {0:'nodata', 10:'Tree cover', 20:'Shrubland', 30:'Grassland', 40:'Cropland',50: 'Built-up', 60:'Bare / sparse vegetation', 70: 'Snow and ice', 
             80:'Permanent water bodies',90:'Herbaceous wetland', 95:'Mangroves', 100: 'Moss and lichen'}

  
#  return 


  # Open image and label
#def vis_patch(image, mask, add_legend=True):
#    """Plotting function of an image along with the corresponding label"""
#    
#    f, ax = plt.subplots(1, 2, figsize=(8, 8))
#
#    rgb_nir = scale_img(image)
#    ax[0].imshow(rgb_nir)
#   
#    im = ax[1].imshow(np.transpose(mask, (1,2,0)), cmap=cmap_esa)
#    
#    if add_legend:
#        # Add the colorbar to the plot
#        #im = ax[1].imshow(np.transpose(mask, (1,2,0)), cmap=cmap_esa)
#
#        # Add a color bar with the class labels
#        colorbar = f.colorbar(im, ax=ax[1], ticks=values)
#        colorbar.ax.set_yticklabels(class_names, fontsize=8)
#        colorbar.ax.tick_params(labelsize=8)
#        colorbar.ax.set_ylabel('Class', fontsize=10)
#
#        # Adjust the size of the colorbar
#        colorbar.ax.set_position([0.95, 0.25, 0.02, 0.5])
#
#
## Show the plot
#plt.show()
#
#vis_patch(img, lab)
#
# DEFINING A FUNCTION TO VISUALIZE THE LABELS PREPARED FROM THE REFERENCE IMAGES
#def visualize_labels(labels, fig_width = 5, fig_height = 5):
#    fig = plt.figure(figsize = (fig_width, fig_height))
#    a = fig.add_subplot(1, 1, 1)
#    values = np.unique(labels.ravel())
#    im = plt.imshow(labels[:, :, 0])
#    a.set_title("GROUND TRUTH")
#    # get the colors of the values, according to the 
#    # colormap used by imshow
#    colors = [im.cmap(im.norm(value)) for value in values]
#    # create a patch (proxy artist) for every color 
#    # labels = ["ROAD", "PARKING", "BUILDING", "GREEN AREAS", "OTHER AREAS"]
#    labels = ["CLASS 1", "CLASS 2", "CLASS 3", "CLASS 4", "CLASS 5", "CLASS 6", "CLASS 7", "CLASS 8"]
#    patches = [mpatches.Patch(color = colors[i], label = j) for i, j in zip(range(len(values)), labels)]
#    # put those patched as legend-handles into the legend
#    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#
#  # DEFINING A FUNCTION TO VISUALIZE THE SATELLITE IMAGE DATA
#def visualize_data(data, title, fig_width = 5, fig_height = 5):
#  %matplotlib inline
#%pylab inline
#pylab.rcParams['figure.figsize'] = (10, 10)
#import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
#from skimage import exposure
#    # Visualize only RGB Bands
#    data = data[:, :, 0:-1]
#    # data = data[:, :, 0]
#    _ = data[:, :, 0].copy()
#    data[:, :, 0] = data[:, :, 2]
#    data[:, :, 2] = _
#    data = data.astype(np.float)
#    
#    # Perform Stretching for Better Visualization
#    for i in range(data.shape[2]):
#        p2, p98 = np.percentile(data[:, :, i], (2, 98))
#        data[:, :, i] = exposure.rescale_intensity(data[:, :, i],
#                                                      in_range=(p2, p98))
#    fig = plt.figure(figsize = (fig_width, fig_height))
#    a = fig.add_subplot(1,1,1)
#    a.set_title(title)
#    plt.imshow(data)
#
