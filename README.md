# cat-dog-detection-yolov8

This project aims to create a yolov8 model to detect cat and dogs.

## Introduction

The images that are used in this project as dataset belong to the dataset which is called [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html). In order to download those images from dataset, the OIDv4_ToolKit has been used, you can access the link from [here](https://github.com/EscVM/OIDv4_ToolKit). And in order to make them convert to the yolov8 annotation format, the website which is called [Roboflow](https://roboflow.com/annotate) has been used.


## Summary

Approximately 1800 images are used as training data. 300 epochs has been aimed but the training stoped at around 70 epochs. The model is ok but it needs more data to train in order to become better. But training the model with 1800 images for around 70 epochs took almost 24 hours, which is a long time working with macbook.