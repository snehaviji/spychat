
from LSBSteg import *

#encoding
image = input("Provide the name of the image to hide the message : ")
steg = LSBSteg(cv2.imread(image))
text = input('Enter the message you want to send:\n')
img_encoded = steg.encode_text(text)
cv2.imwrite("Hidden_Image.png", img_encoded)