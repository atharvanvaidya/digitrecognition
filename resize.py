# This Script Resizes the 256 * 256 Image to 8 * 8
from PIL import Image

def res():
    # Number of Horizontal Pixels
    basewidth = 8
    img = Image.open('original.png')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save('resized.png')
    print("Image Resized!")
