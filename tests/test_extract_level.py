import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Lib.extract_level import *



def main():
    img = cv2.imread('./screenshots/level.jpg')
    nickname = extract_nickname(img)

    print(nickname)

def showimg(img):
    cv2.imshow('rgb_image', img)
    cv2.waitKey()




if __name__ == '__main__':
    main()
