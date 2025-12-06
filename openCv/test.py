import cv2
image_path=r'gerbera.jpg'
img=cv2.imread(image_path)  
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

