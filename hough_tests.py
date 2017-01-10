import os
import cv2
import numpy as np


def HoughCirc(i):
    dp = 2
    minDist = 250
    minR = 100
    maxR = 150
    thresh_low = 50 #18 looked ok before
    thresh_high = 3*thresh_low
    #output = np.zeros(i.shape)#i.copy()
    edges = cv2.Canny(i, thresh_low, thresh_high)
    #lines = cv2.HoughLines()
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp, minDist, param1 = thresh_low, minRadius=minR, maxRadius=maxR)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
    return circles

def LineTest(i):
    im_array = i

    # rho =
    # theta =
    # threshold =

    thresh_low = 18
    thresh_high = 3*thresh_low

    gray = cv2.cvtColor(im_array, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, thresh_low, thresh_high)#, apertureSize=3)
    return cv2.HoughLinesP(edges, 1, np.pi/180, 200, minLineLength = 25)

def addLines(i, l = None):
    if l is None:
        return i
    else:
        i2 = i

    for j in l:
        # for rho,theta in j:
        #     h, w = i2.shape[:2]
        #     #h, w = i2.shape[0], i2.shape[1]
        #     a = np.cos(theta)
        #     b = np.sin(theta)
        #     x0 = a*rho
        #     y0 = b*rho
        #     #print('height: ' + str(h) + '\nwidth: ' + str(w) + '\na: ' + str(a) + '\nb: ' + str(b))
        #     x1 = int(x0 + w*(-b))
        #     y1 = int(x0 + h*(a))
        #     x2 = int(x0 - w*(-b))
        #     y2 = int(x0 - h*(a))
        #     cv2.line(i2, (x1, y1), (x2, y2), (255,0,0), 2)
        x1, y1, x2, y2 = j[0]

        cv2.line(i2, (x1, y1), (x2, y2), (255, 0, 0), 2)
    return i2
    # cv2.imwrite('./Hough/line_test/edges.jpg', edges)
    # cv2.imwrite('./Hough/line_test/test.jpg', gray)

def addCirc(i, circ):
    i2 = i
    for (x, y, r) in circles:
        cv2.circle(i2, (x, y), r, (255, 255, 255), 4)
        cv2.rectangle(i2, (x-5, y-5), (x+5, y+5), (255, 128, 255), -1)
    return i2

n = 0
for file in os.listdir('./train/LAG/'):
    img = cv2.imread(os.path.join('./train/LAG/', file))[50:, ::]#, 0)
    if img is not None:
        circles = HoughCirc(img)
        lines = LineTest(img)

        img = addLines(img, lines)
        img = addCirc(img, circles)

        cv2.imwrite('./Hough/edges/large_sample/' + str(n) + '.jpg', img)#cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20))
        n+=1
