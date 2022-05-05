from Lib.extract_level import is_profile_page, extract_nickname, extract_level
from Lib.extract_legend import is_legend_page, extract_legend_info, Legends
import time
import pyautogui as pag
import numpy as np

path = './data/account_data.csv'
header = ["Steam ID","Nickname","Level","Rank"] + Legends

def get_account_info():
    print("Enter Steam ID: ",end='')
    steamid = input()
    nickname = get_nickname()[0:-1]
    level = ''
    rank = ''
    legend_info,legend_info_list = get_legend()
    info = [steamid, nickname, level, rank]+ legend_info_list
    print(info)
    return info

def get_nickname():
    def remove_punctuation(string):
        res = ''
        for letter in string:
            if letter.isdigit() or letter.isalpha():
                res += letter
        return res
    print('Please open your profile page in fullscreen',end='')
    while True:
        time.sleep(0.1)
        img = np.array(pag.screenshot())
        if is_profile_page(img):
            print(' (Success)')
            return remove_punctuation(extract_nickname(img))

def get_legend():
    print('Please open your legend page in fullscreen',end='')
    while True:
        time.sleep(0.1)
        img = np.array(pag.screenshot())
        if is_legend_page(img):
            print(' (Success)')
            return extract_legend_info(img)

def load_account_data():
    account_data = []
    try:
        file = open(path,'r')
        firstline = True
        for line in file.readlines():
            if firstline:
                firstline = False
                continue
            account_data.append(line.split(','))
        file.close()
    except FileNotFoundError:
        pass
    return account_data


def save_account_data(account_data):
    file = open(path,'w')
    file.write(','.join(header))
    for line in account_data:
        file.write('\n' + ','.join(str(item) for item in line))
    file.close()
    print('Successfully saved the account data.')

def update(account_data, info):
    for account in account_data:
        if account[0] == info[0]:
            account = info
            return account_data
    account_data.append(info)
    return account_data

def getYorN(msg):
    print(msg + '(y or n) ',end='')
    inp = input()
    if inp.lower() == 'y' or inp.lower() == 'yes':
        return True
    if inp.lower() == 'n' or inp.lower() == 'no':
        return False
    while True:
        print('Please answer with \"y\" or \"n\". ' + msg + ' ', end='')
        inp = input()
        if inp.lower() == 'y' or inp.lower() == 'yes':
            return True
        if inp.lower() == 'n' or inp.lower() == 'no':
            return False

def main():
    account_data = load_account_data()
    info = get_account_info()
    update(account_data, info)
    if getYorN('Do you want to save this account\'s information?'):
        save_account_data(account_data)

if __name__=='__main__':
    main()