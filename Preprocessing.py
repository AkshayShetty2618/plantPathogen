import cv2
import os
#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Preprocessing:

    def __init__(self,path, isTrain):
        self.path = path
        if isTrain:


    def imagePreprocess(self, path):
        img = cv2.imread(path)
        gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gaus = cv2.GaussianBlur(gry, (5, 5), cv2.BORDER_DEFAULT)
        can = cv2.Canny(gaus, 3, 16)

        closing = None
        kernelSizes = [(13, 13), (15, 15), (17, 17)]
        for kernelSize in kernelSizes:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
            closing = cv2.morphologyEx(can, cv2.MORPH_CLOSE, kernel)

        ret, thresh_img = cv2.threshold(closing, 200, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        imc = img.copy()
        ind = 0
        areaMax = 0
        cind = 0
        img_contours = np.ones(img.shape) * 255
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > areaMax:
                areaMax = area
                cind = ind
            ind = ind + 1

        cv2.drawContours(img_contours, [contours[cind]], -1, (0, 0, 0), cv2.FILLED)
        rst = cv2.add(img, img_contours, dtype=cv2.CV_8UC1)
        return rst

    def trainPre(self):

        #read csv loop across the images, preprocess and save
