# President-Image-Identifier

**Project Overview:**\
To create a convolutional neural network (CNN) that would be capable of identifying Barack Obama, Donald Trump, and Joe Biden. 

**Data Collection:**\
The data were scrapped from [Getty Images](https://www.gettyimages.com) using the ImagePipeline provided in Scrapy. Approximately 3,000 images were collected and then processed using Pillow to be resized into 224x224 images. 

**Data Analysis and Model Building:**\
The notebook used for this step could be found [here](https://nbviewer.jupyter.org/github/chihaos1/President-Image-Identifier/blob/main/President%20Image%20Identifier.ipynb). Two popular CNN models—ResNet50 and VGG16—were used and compared.

**Final Verdict:**\
VGG16 was more accurate in identifying the president in the images. 
