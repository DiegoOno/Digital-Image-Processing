import numpy as np
import cv2
import argparse
import sys

def histogram_equalization(image):
 
  hist,bins = np.histogram(image.ravel(),256,[0,255])

  # comultative_frequency = np.cumsum(hist)
  # total_pixels = image.shape[0] * image.shape[1]
  
  # LUT = np.uint8((comultative_frequency / total_pixels))

  # equalized = LUT[np.uint8(image[::])] 
  # return equalized

def join_equalized_with_otsu(equalized, otsu_image):
  otsu_image = np.clip(np.floor(otsu_image - 254), 0, 255)
  final_image = equalized * otsu_image
  final_image = np.uint8(final_image)
  return final_image

def main():
  np.set_printoptions(threshold=sys.maxsize)
  ap = argparse.ArgumentParser()
  
  ap.add_argument('-i', '--image', required=True,
    help='path to input image')

  args = vars(ap.parse_args())
  
  img = cv2.imread(args['image'], 0)

  # imgf is original image with Otsu
  ret, imgf = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
  equalized = histogram_equalization(img)
  result = join_equalized_with_otsu(equalized, imgf)

  cv2.imshow('Original', img)
  cv2.imshow('Otsu', imgf)
  cv2.imshow('Equalized', equalized)
  cv2.imshow('Otsu + Equalization', result)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

if (__name__ == '__main__'):
  main()