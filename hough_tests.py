import os
import cv2
import numpy as np


def HoughPrac(i):
    dp = 2
    minDist = 250
    minR = 100
    maxR = 150
    output = i.copy()
    edges = cv2.Canny(i, 18, 54)
    lines = cv2.HoughLines()
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp, minDist, minRadius=minR, maxRadius=maxR)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x-5, y-5), (x+5, y+5), (0, 128, 255), -1)
        #cv2.imwrite('./Hough/edges/test_'+str(dp)+'_'+str(minDist)+'_'+str(minR)+'_'+str(maxR)+'.jpg', output)
        #return output
    if lines is not None:

im_array = cv2.imread('./img_00091.jpg')#[50:, ::]
gray = cv2.cvtColor(im_array, cv2.COLOR_BGR2GRAY)
cv2.imwrite('./Hough/line_test/grey.jpg', gray)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
for i in lines:
    for rho,theta in i:
        h, w = gray.shape
        h, w = 1000, 1000
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        #print('height: ' + str(h) + '\nwidth: ' + str(w) + '\na: ' + str(a) + '\nb: ' + str(b))
        x1 = int(x0 + w*(-b))
        y1 = int(x0 + h*(a))
        x2 = int(x0 - w*(-b))
        y2 = int(x0 - h*(a))

        cv2.line(gray, (x1, y1), (x2, y2), (0,0,255), 2)
cv2.imwrite('./Hough/line_test/edges.jpg', edges)
cv2.imwrite('./Hough/line_test/test.jpg', gray)


# n = 0
# for file in os.listdir('./train/LAG/'):
#     img = cv2.imread(os.path.join('./train/LAG/', file), 0)
#     if img is not None:
#         cv2.imwrite('./Hough/edges/large_sample/' + str(n) + '.jpg', HoughPrac(img))#cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20))
#         n+=1

here are some changes that I want to make
