Legends = ['Caustic','Mirage','Octane','Wattson','Crypto','Revenant','Loba','Rampart','Horizon','Fuse','Valkyrie','Seer','Ash','Mad_Maggie']
Legends_KOR = ['코스틱','미라지','옥테인','왓슨','크립토','레버넌트','로바','램파드','호라이즌','퓨즈','발키리','시어','애쉬','매드매기']

cellwidth = 95
cellheight = 77
tilt = 45

def is_legend_page(img):
    points = [(9,999,20),(9,1085,20),(7,1160,20),(39,1028,100),(33,1069,80),(40,1175,100),(74,1050,150),(74,1136,150),(73,1229,150)]
    count = 0
    for (x,y,minredness) in points:
        r,g,b = img[x][y]
        redness = int(r) - int(g) - int(b)
        if redness > minredness:
            count += 1
    if count >= 7:
        return True
    return False

def extract_legend_info(img):
    info = dict()
    infolist = []
    for legend in Legends:
        info[legend] = 'X'
        infolist.append('X')
    for i in range(6,20):
        if not isGray(img,i//5,i%5):
            info[Legends[i-6]] = 'O'
            infolist[i-6] = 'O'
    return info,infolist

def isGray(img, i,j):
    count = 0
    for dx in range(cellwidth//10):
        for dy in range(cellheight//10):
            if count >= 3:
                return False
            x,y = getpos(i,j,dx*10,dy*10)
            if max(img[y][x])-min(img[y][x]) > 20: #if not gray
                count += 1
    return True

def getpos(i,j,dx,dy):
    x,y = ij2xy(i,j)
    dx,dy = shear(dx,dy)
    x += dx
    y += dy
    return (round(x),round(y))

def ij2xy(i, j):
    x0 = 255
    y0 = 395
    totw = 833 - x0
    toth = 850 - y0
    tott = -(93 - x0)
    x = x0 + ((totw - 5 * cellwidth) / 4 + cellwidth) * j - ((tott - 4 * tilt) /3 + tilt) * i
    y = y0 + ((toth - 4 * cellheight) / 3 + cellheight) * i
    return (x, y)

def shear(dx, dy):
    dx -= tilt/cellheight * dy
    return (dx,dy)
