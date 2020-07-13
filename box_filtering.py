import cv2
import numpy as np
import math
import sys
import os

def main():
  image_path = sys.argv[1]
  img = cv2.imread(image_path)

  cv2.imshow('Image', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if (__name__ == '__main__'):
  main()