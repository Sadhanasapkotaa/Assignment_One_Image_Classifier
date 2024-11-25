#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model within classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
from torchvision import models, transforms
from PIL import Image
import torch

def classify_images(images_dir, results, model_name):
    # Load the pre-trained model
    if model_name == 'vgg':
        model = models.vgg16(pretrained=True)
    elif model_name == 'alexnet':
        model = models.alexnet(pretrained=True)
    elif model_name == 'resnet':
        model = models.resnet18(pretrained=True)
    else:
        raise ValueError("Unsupported model architecture: {}".format(model_name))
    
    model.eval()  # Set model to evaluation mode
    
    # Define image transformations
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    for filename, label_data in results.items():
        image_path = os.path.join(images_dir, filename)
        try:
            img = Image.open(image_path).convert('RGB')
            img_tensor = preprocess(img).unsqueeze(0)
            
            with torch.no_grad():
                output = model(img_tensor)
            
            # Get the predicted class
            predicted_idx = output.argmax().item()
            # Map index to class name (pre-trained model classes)
            # Assuming `imagenet_classes` is a dictionary with index-to-class mappings
            predicted_label = imagenet_classes[predicted_idx]  # You need to define `imagenet_classes`
            results[filename].extend([predicted_label, int(predicted_label == label_data[0])])
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            results[filename].extend(['Error', 0])
