from PIL import Image
import os

size_224 = (224,224)
old_path = 'pres_crawler//local_folder//files'
new_path = 'pres_crawler//local_folder'

for image in os.listdir(old_path):
    if image.endswith('.jpg'):
        i = Image.open(old_path + '//' + image)
        fn, fext = os.path.splitext(image)
        
        i = i.resize(size_224, Image.ANTIALIAS)
        i.save(new_path + '//224//{}_224{}'.format(fn, fext), quality=100)
    
