from LSBSteg import *

#decoding
im = cv2.imread("Hidden_Image.png")
steg = LSBSteg(im)
print("Text value:",steg.decode_text())