import cv2,os
import numpy as np
import csv
import glob
label = "Parasitized"
dirList = glob.glob("C:/Users/heman/OneDrive/Desktop/HACKATHON/cell_images/"+label+"/*.png")
file = open("C:/Users/heman/OneDrive/Desktop/HACKATHON/dataset.csv","a")
for img_path in dirList:

	im = cv2.imread(img_path)
	
	im = cv2.GaussianBlur(im,(5,5),2)



	im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

	ret,thresh = cv2.threshold(im_gray,127,255,0)
	contours,_ = cv2.findContours(thresh,1,2)
	'''for contour in contours:
		cv2.drawContours(im_gray, contours, -1, (0,255,0), 3)
	

	cv2.imshow("window",im_gray)'''
	file.write(label)
	file.write(",")

	for i in range(5):
		try:
			area = cv2.contourArea(contours[i])
			file.write(str(area))
		except:
			file.write("0")

		file.write(",")

	
	file.write("\n")
