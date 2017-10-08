# This Script Displays the Analyzed Result, Entered Number's Image and Graph.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

from matplotlib import style

def whatNumIsThis(filePath):

    #Read the DataSet and the Input(i.e. test.png)
    matchedAr = []
    loadExamps = open('numArEx.txt', 'r').read()
    loadExamps = loadExamps.split('\n')
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()
    inQuestion = str(iarl)

    #Algotithm to Match pixels with each figure.
    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')
            x = 0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x += 1
        except Exception as e:
            print("Exception:"+str(e))
    x = Counter(matchedAr)

    # Display the Result in Terminal
    print("The Most Likely Number Can be:" + str(x.most_common(1)[0][0]))
    print("Other Likely Numbers Can be:", end=" ")
    for i in x.most_common(3)[1:]:
        print(i[0], end=' ')
    graphX = []
    graphY = []

    # Prepare the Lists to be passed in Bar Graph
    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])

    print(" ")

    # Plotting the Image and Graph
    fig = plt.figure("Result")

    # Display the First value of the First Tuple of the Counter Object
    fig.suptitle("Most Likely Value:" + str(x.most_common(1)[0][0]))

    #Allocate the Image and Graph Position to the Grid
    ax1 = plt.subplot2grid((4, 4), (0, 0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4, 4), (2, 0), rowspan=3, colspan=4)

    #Display the Image
    ax1.imshow(iar)

    #Display the Graph
    ax2.bar(graphX, graphY, align='center')
    ax2.set_xlabel("Digits")
    ax2.set_ylabel("No. of Matched Pixels")
    plt.ylim(300)
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    #Show the Image And Graph
    plt.show()
