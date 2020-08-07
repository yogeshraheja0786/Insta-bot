# IG-BOT 
# Automation of Instagram
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
import sys


class InstagramBot:
    def __init__(self, username, password):
        # takes the entered username and password from user and puts them into the instance variables
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com/'
        self.driver = webdriver.Chrome('./chromedriver.exe')
        




    # function for login into the instagram
    def login(self):
        self.driver.get('{}'.format(self.base_url))
        # directs to instagram official webpage
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        # username and password are entered
        # Login button is clicked
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click()
        # don't save the login credentials button is clicked
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button").click()
        # Turn off notifications button is clicked
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm").click()





    # function for opening the page of a new user
    def nav_user(self, user):
        self.driver.get('{}{}/'.format(self.base_url, user))


    # function for following a user
    def auto_follow(self, user):
        self.nav_user(user)
        x = self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button").click()
        time.sleep(10)
    
        




    # function for opening the first picture 
    def first_picture(self):
        pic = self.driver.find_element_by_class_name("_9AhH0")
        pic.click()




    # function for liking an opened pic 
    def like_pic(self):
        time.sleep(4)
        like = self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg").click()





    # function for opening the next picture 
    def next_picture(self):
        time.sleep(2)
        nex = 0
        nex = self.driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow")
        time.sleep(1)
        return nex




        
    # function for continuing to like all phots of the follower
    def continue_liking(self):
        while(True):
            
            next_el = self.next_picture()
            # if next button is there then click it
            # No next button is present for the last pic
            if next_el != 0:
                # click the next button
                next_el.click()
                time.sleep(2)
                # like the picture
                self.like_pic()
                time.sleep(2)
            else:
                self.driver.close()
                sys.exit()
                    


                
            
    


if __name__ == "__main__":
    # username and password are entered by the user
    username = input("enter the username and password : ")
    password = input("")
    
    # Ig_bot is the object created for Instagrambot class
    followusername = input("enter the name of the user to be followed : ")
    likeprofilersusername = input("enter the name of the user whose profile pics to be liked : ")
    
    Ig_bot = InstagramBot(username,password)

    # Login function is called and the given user is followed
    Ig_bot.login()
    Ig_bot.auto_follow(followusername)

    #All the pics of the given user are liked
    Ig_bot.nav_user(likeprofilersusername)
    Ig_bot.first_picture()
    Ig_bot.like_pic()
    Ig_bot.continue_liking()