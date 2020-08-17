import cv2
import numpy as np
import argparse

def main():

	ap = argparse.ArgumentParser()

	ap.add_argument('-i', '--image', required=True, help='path to input image')
	ap.add_argument('-s', '--sigma', required=True, help='The value that will be used in center of the mask')
  
	args = vars(ap.parse_args())

	image_path = args['image']
	sigma = float(args['sigma'])
	# image_name = image_path.split('.')[0]
	
	img = cv2.imread(image_path, 0)
	
	if (sigma >= 1):
		c1 = sigma + 4
		c2 = sigma + 8

		high_boost_mask1 = np.array([[0, -1, 0],
																 [-1, c1, -1],
																 [0, -1, 0]])	
		
		high_boost_mask2 = np.array([[-1, -1, -1],
																 [-1, c2, -1],
																 [-1, -1, -1]])	
	
		#Colocando borda de zeros
		img = np.pad(img, pad_width=1, mode='constant', constant_values=0)
		
		convolved_img1 = cv2.filter2D(img, -1, high_boost_mask1) 
		convolved_img2 = cv2.filter2D(img, -1, high_boost_mask2) 

		# cv2.imwrite(image_name + '_m2.jpg', new_image)
		cv2.imshow('Original Image', img)
		cv2.imshow('HB1 mask', convolved_img1)
		cv2.imshow('HB2 mask', convolved_img2)
		
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	
	else:
		print('Invalid sigma value')

if (__name__ == '__main__'):
  main()