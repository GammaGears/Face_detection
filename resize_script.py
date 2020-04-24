#GAMMAGEARS_CODE
#RESIZEING THE IMAGES USING OPENCV
import cv2
img=cv2.imread("Lighthouse.jpg",0)#0=GREYSCALE,1=RGB,-1=ALPHA CHANNELS
# print(type(img))
# print(img)
# print(img.shape)
# print(img.ndim)
resize_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("gammagears",resize_img)
#To write an image {save image}
cv2.imwrite("gammagears_resized.jpg",resize_img)
#GAMMAGEARS is an title
cv2.waitKey(0)
#5000 milisec is 5 sec,to close window after 5 sec
cv2.destroyAllWindows()
