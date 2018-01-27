
# coding: utf-8

# In[1]:


# manually download folder from google drive

# for each species
	# for each image
        # greyscale and process


# In[5]:


# species name : [feature vector]
features = {
	's1': ['f1', 'f2'],
	's2': ['f1', 'f2'],
	's3': ['f1', 'f2']
}


# In[31]:


import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import sys
sys.executable

from PIL import Image
import os, os.path


# In[37]:


full_path = '/Users/EmmaXu/Documents/Programming/Animal Health Hackathon/2018/'
input_dir = full_path + 'test/'
output_dir = full_path + 'test_grey/'


for species in features.keys():
    for img in os.listdir(input_dir + species):
        full_img_addr = input_dir + species + '/' + img
        
        # converts image to greyscale L with alpha
        grey_img = Image.open(full_img_addr).convert('LA')
        
        # displays image
        plt.figure()
        plt.imshow(grey_img)
        
        # saves image
        img_name, ext = img.split('.')
        try:
            grey_img.save(output_dir + species + '/' + img_name + '.png')
        except:
            try:
                os.makedirs(output_dir + species)
                grey_img.save(output_dir + species + '/' + img_name + '.png')
            except:
                print("SOMETHING IS REALLY BROKEN")
                sys.exit()

