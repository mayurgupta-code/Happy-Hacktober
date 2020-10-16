import pytesseract
import cv2

img = cv2.imread('image.png')

# preprocessing
# gray scale
def gray(img):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(r"./preprocess/img_gray.png",img)
    return img

# blur
def blur(img) :
    img_blur = cv2.GaussianBlur(img,(5,5),0)
    cv2.imwrite(r"./preprocess/img_blur.png",img)    
    return img_blur

# threshold
def threshold(img):
    #pixels with value below 100 are turned black (0) and those with higher value are turned white (255)
    img = cv2.threshold(img, 100, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)[1]    
    cv2.imwrite(r"./preprocess/img_threshold.png",img)
    return img

im_gray = gray(im)
im_blur = blur(im_gray)
im_thresh = threshold(im_blur)

text = pytesseract.image_to_string(im_thresh)
# print text
#text = text.split('\n')
print(text)
