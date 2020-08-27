import cv2
import numpy as np
import argparse
import sys

def gaussian_filter(shape=(3,3),sigma=0.5):
  m,n = [(ss-1.)/2. for ss in shape]
  y,x = np.ogrid[-m:m+1,-n:n+1]
  h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
  h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
  sumh = h.sum()
  if sumh != 0:
    h /= sumh
  return h

def main():
  np.set_printoptions(threshold=sys.maxsize)
  ap = argparse.ArgumentParser()

  ap.add_argument('-i', '--image', required=True, help='Caminho da imagem')  
  ap.add_argument('-w', '--weight', required=True, help='Peso de generalização') # Need change   
  args = vars(ap.parse_args())

  image_path = args['image']
  weight = float(args['weight'])
  # image_name = image_path.split('.')[0]
  img = cv2.imread(image_path, 0)

  # Convolution with gaussian mask
  gauss_mask = gaussian_filter()
  gauss_convolved = cv2.filter2D(img, -1, gauss_mask)

  high_boost_mask = cv2.absdiff(img, gauss_convolved)
  high_boost_mask = np.uint8(high_boost_mask * weight)

  # g(x, y) = f(x, y) + k * Gmask(x, y)
  high_boost_image = cv2.add(img, high_boost_mask)
  high_boost_image = np.uint8(high_boost_image)

  # cv2.imwrite(image_name + '_m2.jpg', new_image)
  cv2.imshow('Original Image', img)
  cv2.imshow('Gaussian mask', gauss_convolved)
  cv2.imshow('High Boost Mask', high_boost_mask)
  cv2.imshow('High boost image', high_boost_image)

  cv2.waitKey(0)
  cv2.destroyAllWindows()
	
if (__name__ == '__main__'):
  main()