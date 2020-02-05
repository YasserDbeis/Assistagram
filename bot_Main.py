from selenium import webdriver
import os
import time 

class InstagramBot: 

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('chromedriver.exe')
        
        self.login()
    
    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))

        time.sleep(1)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

        time.sleep(1)

    def findPage(self, user):

        self.driver.get('{}/{}/'.format(self.base_url, user))

    def followAction(self, user, follow):
        try:
            self.findPage(user)
        except:
            print("Page not found")
            return "Page not found"


        time.sleep(1)

        if(follow == True):
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()
            except:
                try:
                    self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/button').click()
                except:
                    print("Page not found")
                    return "Page not found"


        else:
            try:
                unfollow_Button = self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]").click()
                unfollow_Button.click()

            except:
                try:
                    unfollow_Button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/button/div').click()
                    unfollow_Button.click()
                except: 
                    print("Page not found")
                    return "Page not found"

            finally:
                time.sleep(1)
                unfollow_Button = self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()


    def searchHashtag(self, hashtag):

        self.driver.get('{}/explore/tags/{}'.format(self.base_url, hashtag))

    def followTags(self, amount, hashtag):
        
        try:
            self.searchHashtag(hashtag)
        except: 
            return "Hashtag not found"

        time.sleep(1)

        self.driver.find_element_by_class_name('v1Nh3').click()  

        i = 0
        amount = int(amount)
        while(i < amount):
            time.sleep(1)
            try: 
                if(self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]")):
                    self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            except:
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                time.sleep(1)
                self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            
            time.sleep(1)
            
            i+=1
        
        self.driver.get('{}/{}'.format(self.base_url, self.username))

    def likeRecentPost(self, user, amount):
        
        try:
            self.findPage(user)
        except: 
            return "User not found"

        time.sleep(1)

        self.driver.find_element_by_class_name('v1Nh3').click()  
        time.sleep(1)

        i = 0
        amount = int(amount)
        while(i < amount):
            time.sleep(1)
            self.driver.find_element_by_class_name('wpO6b').click() 

            try:
                self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            except:
                print("Done with liking.")
                self.driver.get('{}/{}'.format(self.base_url, self.username))
                return "Done"


            time.sleep(1)
            
            i+=1
        
        self.driver.get('{}/{}'.format(self.base_url, self.username))

    def watchStories(self, amount, storyTime):
        
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/button/div[1]').click() 
        time.sleep(1)

        i = 0
        amount = int(amount)
        storyTime = int(storyTime)
        while(i < amount):
            time.sleep(storyTime)
            self.driver.find_element_by_class_name('coreSpriteRightChevron').click()            
            i+=1
        
        self.driver.get('{}/{}'.format(self.base_url, self.username))

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")




if __name__ == '__main__':
    
    ig_bot = InstagramBot('username', 'password')

    choice = ""

    ig_bot.scroll()

    while(choice != "exit"):

        choice = input("Enter a bot operation: ")
        if(choice == "find page"):  
            userChoice = input("Who's page would you like to find? ")
            ig_bot.findPage(userChoice)
        elif(choice == "follow action"):
            followChoice = input("Would you like to follow or unfollow a user? ")
            followUser = input("Who would you like to do this action to? ")

            if(followChoice == "follow"):
                ig_bot.followAction(followUser, True)
            else:
                ig_bot.followAction(followUser, False)
        elif(choice == "follow tags"):
            hashtagChoice = input("What hashtag would you like to pursue? ")
            numUsers = input("How many hashtag accounts would you like to follow? ")
            ig_bot.followTags(numUsers, hashtagChoice)
        elif(choice == "search hashtags"):
            hashtagChoice = input("What hashtag would you like to pursue? ")
            ig_bot.searchHashtag(hashtagChoice)
        elif(choice == "like recent"):
            userChoice = input("Who's account would you like to like their most recent posts? ")
            numLikes = input("How many of the last recent posts would you like to like? ")
            ig_bot.likeRecentPost(userChoice, numLikes)
        elif(choice == "watch stories"):
            numStories = input("How many stories would you like to watch? ")
            storyLength = input("How long would you like each story to last? ")

            ig_bot.watchStories(numStories, storyLength)

