
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from yt_trend import get_yt_trend
import time
import argparse
#
# Based off:
# https://github.com/JeffHenry/Bing-Search-Bot/blob/master/Bing.py
# https://stackoverflow.com/a/35641449
#

class bing_auto_browser:
    def __init__(self):
        self.browser = None

    def open_url(self, url='https://www.bing.com'):
        self.browser.get(url)

    def get_searchbar(self):
        return self.browser.find_element_by_id('sb_form_q')

    def clear_searchbar(self, searchbar=None):
        if searchbar is None:
            searchbar = self.get_searchbar()

        searchbar.send_keys(Keys.CONTROL,'a')
        searchbar.send_keys(Keys.DELETE)

    def search_term(self, search_term, searchbar=None):
        if searchbar is None:
            searchbar = self.get_searchbar()
        self.clear_searchbar(searchbar)
        searchbar.send_keys(str(search_term), Keys.ENTER)


    def login(self, username, password):
        #
        # https://medium.com/@prateekrm/earn-500-daily-microsoft-rewards-points-automatically-with-a-simple-python-program-38fe648ff2a9
        #
        try:
            #self.open_url(url='https://login.live.com')
            self.open_url(url='https://www.bing.com/')
            signin_button = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_l"]')))
            time.sleep(2)
            signin_button.click()
           
            time.sleep(3)
            username_ent = self.browser.find_element_by_name('loginfmt')
            username_ent.clear()
            username_ent.send_keys(username)
            username_ent.send_keys(Keys.RETURN)
            
            time.sleep(3)
            password_ent = self.browser.find_element_by_name('passwd')
            password_ent.clear()
            password_ent.send_keys(password)
            password_ent.send_keys(Keys.ENTER)
            
            time.sleep(3)
            try:
                remember_account_butt = self.browser.find_element_by_xpath('//*[@id="idSIButton9"]')
                remember_account_butt.click()
            except:
                pass
            

        except Exception as e:
            print(e)
            exit()

    # def new_tab(self, switch=True):
    #     # self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    #     self.browser.execute_script("window.open('');")
    #     if switch is True:
    #         print(self.browser.switch_to_window(self.browser.current_window_handle))

    def quit(self):
        self.browser.quit()

class bing_auto_ff(bing_auto_browser):
    ''' Bing Auto Driver for FireFox '''
    def __init__(self):
        super(bing_auto_browser, self)
        self.browser = webdriver.Firefox()

class bing_auto_ch(bing_auto_browser):
    ''' Bing Auto Driver for Chrome '''
    def __init__(self):
        super(bing_auto_browser, self)
        self.browser = webdriver.Chrome()
    
class bing_auto_ff_edge(bing_auto_browser):
    ''' Bing Auto Driver for FireFox with Edge User Agent '''
    def __init__(self):
        super(bing_auto_browser, self)

        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4080.0 Safari/537.36 Edg/82.0.453.0"

        profile = webdriver.FirefoxProfile() 
        profile.set_preference("general.useragent.override", user_agent)
        self.browser = webdriver.Firefox(profile)

class bing_auto_ch_edge(bing_auto_browser):
    def __init__(self):
        super(bing_auto_browser, self)

        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4080.0 Safari/537.36 Edg/82.0.453.0"
        
        profile = webdriver.ChromeOptions()
        profile.add_argument('--user-agent="{0}"'.format(user_agent))
        self.browser = webdriver.Chrome(chrome_options=profile)


# Not functional at this moment in time (bing requires the use of the bing app to gain points on mobile :( )
# class bing_auto_ff_mobile(bing_auto_browser):
#     ''' Bing Auto Driver for FireFox on Mobile '''
#     def __init__(self):
#         super(bing_auto_browser, self)

#         # user_agent = 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
#         user_agent = 'Mozilla/5.0 (Linux; Android 8.1.0; Lenovo TB-8504F Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36'
#         profile = webdriver.FirefoxProfile() 
#         profile.set_preference("general.useragent.override", user_agent)
#         self.browser = webdriver.Firefox(profile)
#         self.browser.set_window_size(1280, 768)

class bing_auto:
    def __init__(self, username, password, driver):
        self.driver = driver()
        self.driver.login(username, password)
        time.sleep(10)
        self.driver.open_url(url='https://www.bing.com')
        trending_video_titles = get_yt_trend()
        for video_title in trending_video_titles:
            # self.driver.new_tab()
            self.driver.open_url(url='https://www.bing.com')
            self.driver.search_term(str(video_title))
            time.sleep(0.5)

            
def get_args():           
    parser = argparse.ArgumentParser(description='Arguments', formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u', '--username',
                        required=True,
                        action='store',
                        help='Your microsoft account username (generally an email adress)')
    parser.add_argument('-p', '--password',
                        required=True,
                        action='store',
                        help='Your microsoft account password')              
    parser.add_argument('-b', '--browser',
                        required=False,
                        action='store',
                        default='Firefox',
                        help='''Your choice of browser, any of these options: 
                                Chrome
                                Firefox''')
    parser.add_argument('-a', '--agent',
                        required=False,
                        action='store',
                        default='Default',
                        help='''Your choice of user-agent (allows you to mimic Edge), any of these options: 
                                Edge
                                Default''')

    args = parser.parse_args()
    return args

def main():
    args = get_args()
    if args.browser.casefold() == 'firefox':
        if args.agent.casefold() == 'edge':
            driver = bing_auto_ff_edge
        else:
            driver = bing_auto_ff
    elif args.browser.casefold() == 'chrome':
        if args.agent.casefold() == 'edge':
            driver = bing_auto_ch_edge
        else:
            driver = bing_auto_ch
    else:
        raise ValueError("browser must be equal to firefox or chrome")
    auto = bing_auto(args.username, args.password, driver=driver)

if __name__ == '__main__':
    main()
