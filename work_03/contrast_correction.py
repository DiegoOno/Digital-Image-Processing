import numpy as np
import cv2
import argparse
import sys

def gamma_correction(image, value):
  LUT = np.arange(256)
  LUT = np.power(LUT, value)
  amax = LUT.max()
  LUT = 256 * LUT / amax
  LUT = np.uint8(LUT)
  out = np.zeros(image.shape, dtype=np.uint8)
  out = LUT[image]
  return out

def join_gamma_corrected_with_otsu(gamma_corrected_image, otsu_image):
  otsu_image = np.clip(np.floor(otsu_image - 254), 0, 255)
  final_image = gamma_corrected_image * otsu_image
  final_image = np.uint8(final_image)
  return final_image


def main():
  np.set_printoptions(threshold=sys.maxsize)
  ap = argparse.ArgumentParser()
  
  ap.add_argument('-i', '--image', required=True,
    help='path to input image')

  args = vars(ap.parse_args())
  
  img = cv2.imread(args['image'], 0)
  
  ret, imgf = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
  gamma_corrected_image = gamma_correction(img, 0.5)
  final_image = join_gamma_corrected_with_otsu(gamma_corrected_image, imgf)

  cv2.imshow('Original', img)
  cv2.imshow('Otsu', imgf)
  cv2.imshow('Gamma correction', gamma_corrected_image)
  cv2.imshow('Gamma + Otsu', final_image)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

if (__name__ == '__main__'):
  main()