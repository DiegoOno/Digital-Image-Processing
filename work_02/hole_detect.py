import cv2
import numpy as np
import math
import sys
import os

def main():
  image_path = sys.argv[1]
  img = cv2.imread(image_path)
  grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  cv2.imshow('Image', grayImage)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if (__name__ == '__main__'):
  main()