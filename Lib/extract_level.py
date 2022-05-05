import cv2
import pytesseract
from PIL import Image

x0 = 166
y0 = 300
w = 100
h = 100

def is_profile_page(img): #PIL image
    graypoints = [(224,109),(225,118),(225,287)]
    redpoints = [(9,57),(8,161),(121,58),(69,161)]
    whitepoints = [(72,86),(74,131),(32,108)]
    count = 0
    for (x,y) in graypoints:
        r,g,b = img[x][y]
        sum = int(r) + int(g) + int(b)
        dif = max(img[x][y]) - min(img[x][y])
        if sum>600 and sum<670 and dif<20:
            count += 1
    for (x,y) in redpoints:
        r,g,b = img[x][y]
        gb = int(g) + int(b)
        if r>150 and gb<70:
            count += 1
    for (x,y) in whitepoints:
        r,g,b = img[x][y]
        sum = int(r) + int(g) + int(b)
        if sum>700:
            count += 1
    if count>=9:
        return True
    return False


def extract_lvimg(img):
    for dx in range(w):
        for dy in range(h):
            img2 = img[333:362,195:235]
    return img2

def extract_nameimg(img):
    for dx in range(w):
        for dy in range(h):
            img2 = img[248:290, 94:337]
    return img2

def extract_level(img):
    img = extract_lvimg(img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(gray)
    text = pytesseract.image_to_string(img)
    return text

def extract_nickname(img):
    img = extract_nameimg(img)
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(img)
    text = pytesseract.image_to_string(img)
    return text