from Lib.extract_level import is_profile_page, extract_nickname, extract_level
from Lib.extract_legend import is_legend_page, extract_legend_info, Legends
import time
import pyautogui as pag
import numpy as np
import os
import sys

path = './data/account_data.csv'
header = ["Steam ID","Nickname","Level","Rank"] + Legends

def get_account_info(account_data):
    def getlevel(account_data,steamid):
        print('\nPlease enter LEVEL (leave it empty if unchanged): ',end='')
        lv = input()
        if lv == '' or lv == ' ':
            for acc in account_data:
                if acc[0] == steamid:
                    print(acc[2])
                    return acc[2]
        return lv
    def getrank(account_data,steamid):
        print('\nPlease enter RANK (leave it empty if unchanged): ',end='')
        rank = input()
        if rank == '' or rank == ' ':
            for acc in account_data:
                if acc[0] == steamid:
                    print(acc[3])
                    return acc[3]
        return rank
    def showinfo(info):
        print("===== account info =====")
        for i in range(4):
            print(header[i] + ': ' + info[i])
        print(info[4:])
    print('Please enter Steam ID: ',end='')
    steamid = input()
    for acc in account_data:
        if acc[0] == steamid:
            print('\nThis account already exists. The information you will enter will be used to update this account.')
    nickname = get_nickname()
    legend_info,legend_info_list = get_legend()
    level = getlevel(account_data,steamid)
    rank = getrank(account_data,steamid)
    info = [steamid, nickname, level, rank] + legend_info_list
    info[-1] += '\n'
    showinfo(info)
    return info

def get_nickname():
    def remove_punctuation(string):
        res = string
        if res[-1] == '\n':
            res = res[0:-1]
        return res
    print('\nPlease open your profile page in fullscreen.',end='',flush=True)
    while True:
        time.sleep(0.1)
        img = np.array(pag.screenshot())
        if is_profile_page(img):
            res = remove_punctuation(extract_nickname(img))
            print(' (' + res + ')')
            return res

def get_legend():
    print('Please open your legend page in fullscreen.',end='',flush=True)
    while True:
        time.sleep(0.1)
        img = np.array(pag.screenshot())
        if is_legend_page(img):
            res = extract_legend_info(img)
            print(' (success)')
            return res

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
        print('\nSuccessfully loaded the account data.')
    except FileNotFoundError:
        print('\nAccount data does not exist. A new csv file will be created.')
    return account_data


def save_account_data(account_data):
    file = open(path,'w')
    file.write(','.join(header) + '\n')
    for line in account_data:
        file.write(','.join(str(item) for item in line))
    file.close()
    print('\nSuccessfully saved the account data.')

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
        print('\nPlease answer with \"y\" or \"n\". ' + msg + ' ', end='')
        inp = input()
        if inp.lower() == 'y' or inp.lower() == 'yes':
            return True
        if inp.lower() == 'n' or inp.lower() == 'no':
            return False

def main():
    os.system('cls')
    account_data = load_account_data()
    info = get_account_info(account_data)
    account_data = update(account_data, info)
    if getYorN('\nDo you want to save this account\'s information?'):
        save_account_data(account_data)
    while getYorN('\nDo you want to add another account?'):
        os.system('cls')
        account_data = load_account_data()
        info = get_account_info(account_data)
        update(account_data, info)
        if getYorN('\nDo you want to save this account\'s information?'):
            save_account_data(account_data)

if __name__=='__main__':
    main()