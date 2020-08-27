import cv2
import numpy as np
import argparse
import sys

def label_image(img):
  f = open('pixes.txt', 'w')
  equivalences = []
  count = 0
  for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
      # Checking if the current pixel is on the edge and it's greater than 0
      if img[i][j] > 0 and i - 1 > 0 and j - 1 > 0:
        # Checking if found a new component
        if img[i-1][j] == img[i][j-1] and img[i-1][j] == 0:
          count += 1
          img[i][j] = count
        # Cheking if the top neighbor is the same as the one on the right
        if img[i-1][j] == img[i][j-1] and img[i-1][j] != 0:
          img[i][j] = img[i-1][j]

        if img[i-1][j] != img[i][j-1] and img[i-1][j] != 0 and img[i][j-1] != 0:
          img[i][j] = min(img[i-1][j], img[i][j-1])
          equivalences.append([max(img[i-1][j], img[i][j-1]), min(img[i-1][j], img[i][j-1])])
  f.write(np.array_str(img))
  f.close()
        
def main():
  np.set_printoptions(threshold=sys.maxsize)
  np.set_printoptions(threshold=sys.maxsize)
  ap = argparse.ArgumentParser()
  ap.add_argument('-i', '--image', required=True,
    help='path to input image')
  args = vars(ap.parse_args())
  img = cv2.imread(args['image'], 0)
  img = np.clip(img, 0, 1)
  label_image(img)
  cv2.imshow('Orginal', img)
   
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if (__name__ == '__main__'):
  main()
