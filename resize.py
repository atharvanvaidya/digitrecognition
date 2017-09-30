from PIL import Image

def res():
    basewidth = 8
    img = Image.open('original.png')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save('resized.png')
    print("Image Resized!")
