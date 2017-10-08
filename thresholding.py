# This Script Thresholds the Resized Image into Either Pure Black OR Pure White
from PIL import Image
import numpy as np

def threshold(imageArray):

    # Create balanceAr to Store the Mean of All the Pixel Values
    balanceAr = []
    newAr = imageArray
    from statistics import mean
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)

    # OverWrite Each Pixel Value as Either Black OR White after comparing to the mean.
    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr

def thres():
    ei = Image.open('resized.png').convert("RGBA")
    iar = np.array(ei)
    im = Image.fromarray(threshold(iar))
    im.save("./images/test.png")
    print("Image Successfully Thresholded!")