import cv2
import numpy as np
import argparse

def calculate_box_size(img_shape, reduction_percent):
  box_height = int(img_shape[0] / (img_shape[0] * (reduction_percent / 100)))
  box_width = int(img_shape[1] / (img_shape[1] * (reduction_percent / 100)))
  box = np.ones((box_height, box_width)) * (1 / 9)
  return box

def box_filtering(img, reduction_percent):
  box = calculate_box_size(img.shape, reduction_percent)

  new_image_h = int(img.shape[0] * (reduction_percent / 100))
  new_image_w = int(img.shape[1] * (reduction_percent / 100))
  new_image = np.zeros((new_image_h, new_image_w))
  
  line = 0
  col = 0

  for i in range(0, new_image.shape[0]):
    for j in range(0, new_image.shape[1] - 1):
      crop = img[line:line + box.shape[0], col: col + box.shape[1]]
      col = col + box.shape[1]
      
      new_image[i][j] = np.sum(np.multiply(crop, box))
    
    col = 0
    line = line + box.shape[0]
  
  return np.uint8(new_image)

def main():
  ap = argparse.ArgumentParser()
  
  ap.add_argument('-i', '--image', required=True,
    help='path to input image')
  ap.add_argument('-r', '--reduction', required=True,
    help='Percentage of reduction')
  
  args = vars(ap.parse_args())
  
  img = cv2.imread(args['image'], 0)
  
  cv2.imshow('Original', img)

  new_image = box_filtering(img, int(args['reduction']))
  cv2.imshow('Box filter image', new_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if (__name__ == '__main__'):
  main()