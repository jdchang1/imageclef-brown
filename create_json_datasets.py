from subprocess import check_output

import nltk
# Change this for your specific directory with NLTK 
nltk.data.path.append("/users/ipan/scratch/nltk_data") 

import pandas as pd 
import numpy as np 
import string 
import json 
import re 
import os 

imageclef = {} 
imageclef["dataset"] = "imageclef" 

captions = pd.read_table("/gpfs/data/ceickhof/imageclef/data/CaptionPredictionTraining2018-Captions.csv", header=None) 
captions.columns = ["img", "caption"] 

image_root = "/gpfs/data/ceickhof/imageclef/data/CaptionTraining2018/"
images = check_output("ls "+image_root, shell=True).split() 

# Are all images JPEG? 
for _ in images:
    if not bool(re.search("\\.jpg$", _)):
        print _ 
# Looks like they are

captions["file"] = [_+".jpg" for _ in captions["img"]]

# Some images are not in the data file 
list(set(images) - set(captions["file"]))

# This returns empty list so we're good, I think 
list(set(captions["file"]) - set(images))

np.random.seed(88) 
images_list = [] 
for row in range(captions.shape[0]):
    # This image is bugged or something, threw an error during preprocessing
    if captions["file"][row] == "1751-0147-42-107-4.jpg":
        continue
    tmp_raw_image_caption = unicode(captions["caption"][row], "utf-8") 
    tmp_image_caption_no_punct = captions["caption"][row].translate(None, string.punctuation)
    if np.random.binomial(1, 0.2): 
        split = "val"
    else:
        split = "train"
    image_dict = {}
    image_dict["filepath"] = image_root
    image_dict["filename"] = captions["file"][row]
    image_dict["imgid"] = row 
    image_dict["split"] = split 
    image_dict["sentids"] = [row] 
    sentence_dict = {} 
    sentence_dict["tokens"] = nltk.word_tokenize(unicode(tmp_image_caption_no_punct, "utf-8"))
    sentence_dict["raw"] = tmp_raw_image_caption
    sentence_dict["imgid"] = row
    sentence_dict["sentid"] = row 
    image_dict["sentences"] = [sentence_dict] 
    images_list.append(image_dict) 

imageclef["images"] = images_list 
with open("/gpfs/data/ceickhof/imageclef/data/dataset_imageclef.json", "w") as f: 
    json.dump(imageclef, f) 
