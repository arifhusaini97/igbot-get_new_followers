from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Getpages:
    def __init__(self, driver, accountName):
        self.driver=driver
        self.driver.get('https://www.instagram.com/'+accountName)
        self.hrefs=[]
             # 12 pages/loading
    
    def get_num_flw(self):
        flw = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
        sflw=b(flw.get_attribute('innerHTML'), 'html.parser')
        followers = sflw.findAll('span', {'class':'g47SY'})
        f= followers[1].getText().replace(',', '')
        if 'k' in f:
            f=float(f[:-1]) * 10**3
            return f
        elif 'm' in f:
            f=float(f[:-1]) * 10**6
            return f
        else:
            return float(f)

    def get_followers(self):
        flw_btn=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#react-root > section > main > div > header > section > ul > li:nth-child(2) > a >span')))
        flw_btn.click()
        time.sleep(2)
        self.popup=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div[2]')))
        # self.driver.execute_script('arguments[0].scrollTop=arguments[0].scrollHeight', popup)
        for h in range(11):
            time.sleep(1)
            # print('scrolling')
            # print(h)
            self.driver.execute_script('arguments[0].scrollTop=arguments[0].scrollHeight/{}'.format(str(11-h)), self.popup)
            if h==5:
                break
        for i in range(100):
            time.sleep(2)
            self.driver.execute_script('arguments[0].scrollTop=arguments[0].scrollHeight', self.popup)

        self.popup=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div[2]')))
        b_popup=b(self.popup.get_attribute('innerHTML'), 'html.parser')

        for p in b_popup.findAll('li', {'class': 'wo9IH'}):
            # print(p.findALL('a',{'class': 'FPmhX notranslate_0imsa '})[0])
            try:
                hlink=p.findAll('a')[0]['href']
                # print(hlink)
                if 'div' in hlink:
                    return self.hrefs
                else:
                    self.hrefs.append(hlink)
            except:
                # print(p.findALL('a')[0]['href'])
                pass
        return self.hrefs
        
    def is_public(self):
        try:
            astate= WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.CLASS_NAME, 'rkEop')))
            if astate.text == 'This Account is Private':
                return False
            else:
                return True
        except:
            return True

    def like_post(self):
        post = self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1)')
        html = post.get_attribute('innerHTML')
        h=b(html, 'html.parser')
        href = h.a['href']
        self.driver.get('https://www.instagram.com'+href)
        like_btn=WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')))
        like_btn.click()
        print("Post LIKED successfully")

    def follow_page(self):
        # time.sleep(2)
        follow=WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.sqdOP:nth-child(1)')))
        f_text = follow.text
        if f_text.lower()=='follow':
            follow.click()
            print('Account FOLLOWED successfully')
        elif f_text.lower()=='follow back':
            print('This account is already follow you. Ignore the account.')
        elif f_text =='Requested':
            print('Already requested. Ignore the account.')
        else:
            print('Already followed. Try to unfollow the account.')
            try:
                unfollow_popup=WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._6VtSN')))
                unfollow_popup.click()
                unfollow=WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.aOOlW:nth-child(1)')))
                unfollow_popup.click()
                print('Account UNFOLLOWED successfully')
            except:
                print("CAN'T UNFOLLOW the account")