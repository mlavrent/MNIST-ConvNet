from PIL import Image
import numpy as np

class ImageConverter(object):

    def __init__(self, imageSize):
        # imageSize - tuple (w,h) to normalize images to

        self.imgWidth = imageSize[0]
        self.imgHeight = imageSize[1]
        

    def imageToNPArray(self, imgPath):
        # imgPath - string path to the rgb image
        img = Image.open(imgPath)

        if img.size != (self.imgWidth, self.imgHeight):
            img.resize((self.imgWidth, self.imgHeight), Image.LANCZOS)

                
        rPix = np.array(list(img.getdata(band=0)))
        gPix = np.array(list(img.getdata(band=1)))
        bPix = np.array(list(img.getdata(band=2)))

        return [rPix, gPix, bPix]
