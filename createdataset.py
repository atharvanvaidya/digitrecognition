from PIL import Image
import numpy as np
def createExamples():
    numberArrayExamples = open('numArEx.txt', 'a')
    numbersWeHave = range(0, 10)
    for eachNum in numbersWeHave:
        print (eachNum)
        for furtherNum in range(1, 10):
            print(str(eachNum)+'.'+str(furtherNum))
            imgFilePath = '/home/atharva/PycharmProjects/digitrecognition/images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)

createExamples()