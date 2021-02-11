from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import getpages

username='Put Your Username'
password='Put Your Password'
driver = 0
max_likes=600
max_follows=500
accountName='mppuitmtganu'

def main():
    global driver
    print('running script..')
    driver = webdriver.Chrome('D://a1/software_installer/chromedriver_win32/chromedriver.exe')
    l=login.Login(driver, username, password)
    l.signin()
    print("login succeed...!")
    time.sleep(5)
    gp=getpages.Getpages(driver, accountName)
    print('\nTotal Followers of the Account (' + accountName +') '+ str(gp.get_num_flw()))
    time.sleep(5)
    refs=gp.get_followers()
    run_bot(refs, driver, gp)

def run_bot(refs, driver, gp):
    print('\n' + str(len(refs)) + ' accounts targeted')
    print('_____________________________________')
    t=time.time()
    L=0
    F=0

    for r in refs:
        driver.get('https://www.instagram.com'+r)
        # print(r)
        time.sleep(2)
        if gp.get_num_flw() < 3000:
            if gp.is_public():
                print('\n' + str(L+1) + ') ' + r + ' [Public Account]')
                if L<max_likes:
                    time.sleep(1)
                    try:
                        gp.like_post()
                        L += 1
                        print("Current Liked: " + str(L))
                        with open("C:/laragon/www/web_exploring/igbot/liked_post_ig.txt", "a") as txt_file:
                            time.sleep(1)
                            txt_file.write(r)
                            txt_file.write("\n")
                    except:
                        print('Sorry, could not like his/her first post, lets follow instead...')
                        try:
                            gp.follow_page()
                            F += 1
                            print('Current Followed: ' + str(F))
                            with open("C:/laragon/www/web_exploring/igbot/followed_acc_ig.txt", "a") as txt_file:
                                time.sleep(1)
                                txt_file.write(r)
                                txt_file.write("\n")
                        except:
                            print('Sorry, could not follow skip this account...')
                else:
                    time.sleep(3600) #sleep an hour
            else:
                print('\n' + str(F+1) + ') ' + r + ' [Private Account]')
                if F<max_follows:
                    time.sleep(1)
                    try:
                        gp.follow_page()
                        F += 1
                        print('current followed:' + str(F))
                        with open("C:/laragon/www/web_exploring/igbot/followed_acc_ig.txt", "a") as txt_file:
                            time.sleep(1)
                            txt_file.write(r)
                            txt_file.write("\n")
                    except:
                        print('Sorry, could not follow skip this account...')
                else:
                    time.sleep(3600) #sleep an hour

if __name__ =='__main__':
    main()