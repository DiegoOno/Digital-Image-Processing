import numpy as np
import cv2
import argparse

import skimage.io as io
from skimage.filters import threshold_otsu
from skimage.morphology import closing, square
from skimage.measure import label, regionprops

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument('-i', '--image', required=True,
    help='path to input image')
  args = vars(ap.parse_args())
  
  cv_gray_img = cv2.imread(args['image'], 0)
  cv2.imshow('Original', cv_gray_img)

  cv_rgb_img = cv2.cvtColor(cv_gray_img,cv2.COLOR_GRAY2RGB)

  img = io.imread(args['image'], as_gray=True)

  thresh = threshold_otsu(img)
  bw = closing(img > thresh, square(3))

  # label components
  labeled_img, num = label(bw, return_num=True)
  print(num)

  # For each component founded we need check if the component has one hole or more.
  quantity_components_with_hole = 0
  for region in regionprops(labeled_img):
    if region.euler_number < 1:
      minr, minc, maxr, maxc = region.bbox
      cv2.rectangle(cv_rgb_img, (minc, minr), (maxc, maxr), (85, 98, 38), 2)
      quantity_components_with_hole += 1
  print(quantity_components_with_hole)

  
  cv2.imshow('Labeled', cv_rgb_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if (__name__ == '__main__'):
  main()
