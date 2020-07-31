import cv2
import numpy as np
import argparse

def main():
  # np.set_printoptions(threshold=sys.maxsize)
  ap = argparse.ArgumentParser()
  ap.add_argument('-i', '--image', required=True,
    help='path to input image')
  args = vars(ap.parse_args())
  img = cv2.imread(args['image'])
  
  cv2.imshow('Orginal', img)
   
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if (__name__ == '__main__'):
  main()
