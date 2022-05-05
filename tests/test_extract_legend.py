import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Lib.extract_legend import *
import numpy as np
import cv2


def main():
    img = cv2.imread('./screenshots/legends.jpg')
    info,infolist = extract_legend_info(img)
    print(info)

def extract(img,i,j):
    img2 = np.zeros((480, 640, 3), dtype=np.uint8)
    for dx in range(cellwidth):
        for dy in range(cellheight):
            #if count >= 5:
                #return False
            x,y = getpos(i,j,dx,dy)
            img2[dy][dx] = img[y][x]
    cv2.imshow('rgb_image', img2)
    cv2.waitKey()


if __name__ == '__main__':
    main()