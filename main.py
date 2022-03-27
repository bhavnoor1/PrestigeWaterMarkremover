import os
#thank god for selenium, who ever wrote the library is going to heaven
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import glob		#glob
import time

open("ransomware.virus", "w").write("YOUR COMPUTER HAS BEEN INFECTED, SEND ₿100 TO THIS ADDRESS\nhttp://bitly.com/98K8eH")

#yo
#hello there
def deleteImages():
	for file in glob.glob("image*.png"):
		os.remove(file)

#dont even ask
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#we like to feel like hackers, because thats basically what we are.
print("opening browser")
driver = webdriver.Chrome(options=chrome_options)

def GetImages(website_link):
	#for debug 
	def Login(uname, pword):
		#input username and confirm
		driver.find_element(By.XPATH, f'//*[@id="input-email"]').send_keys(USER_NAME)
		driver.find_element(By.XPATH, f'//*[@id="login_form"]/div[2]/input').click()
		
		#input password and confirm
		driver.find_element(By.XPATH, f'//*[@id="confirm-password"]').send_keys(SUPER_SECRET_PASSWORD)
		driver.find_element(By.XPATH, f'//*[@id="signIn_button"]').click()
		
	
	deleteImages()
	
	#this will open the lifetouch website
	driver.get(website_link)
	#set window size
	driver.set_window_size(4069,2696)##set the window size to 3840 x 2160, you may know this resolution as 4k
	
	
	print("downloading the images...")
	#---------------------------AUTOMATIC SIGN IN V1.0 BETA-------------
	
	
	
	
	#imagine having security
	USER_NAME = os.environ['Email']
	SUPER_SECRET_PASSWORD = os.environ['Pas']
	Login(USER_NAME, SUPER_SECRET_PASSWORD)
	
	#otherwise the first image can't load
	time.sleep(1)
	
	firstrow=False#just ask noor to explain
	
	i = 1
	for row in range(1, 7):
		if firstrow==True: driver.execute_script("window.scrollTo(0, 720)")
		firstrow=True
		for column in range(1, 9):
			try:
				l = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[3]/div/div/div/div[{row}]/div[{column}]/div/div[1]/div/div[1]/img")
				with open(f"image_{row}:{column}.png", "wb") as image:#antonio you missed an f in front of the quotes...
					image.write(l.screenshot_as_png)
		
				i += 1#for image naming
				print(f"\trow:{row}\n\tcolumn:{column}\n\timage{i-1}\n")#debug purposes
			except:
				print("\tnope\n")




#f"/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/button" - xpath to download button not sure if correct

def RemoveWatermarks():
	print("removing watermarks...")
	driver.get("https://www.watermarkremover.io/upload")
	time.sleep(5)
	#repeat for each file of type .png whose name starts with "image"
	for file in glob.glob("image*.png"):
		#help i have no idea of what im doing
		file = os.path.abspath(file)
		print("\t" "removing for image:", file)
		uploadbox = driver.find_element(By.ID, "uploadImage")
		uploadbox.send_keys(file)

		input("complete captcha, then press enter to continue")
		
		dowBut = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/button')
		dowBut.click()
		
def Upscale():
	print("upscaling...")
	driver.get("https://www.upscale.media/upload")

#GetImages("https://shop.lifetouchprestige.ca/shop/viewProofs.html?switchSessionId=1502748336")
RemoveWatermarks()
#Upscale()




"""--------ai image upscale api 

api key: e38b5a7d-bd9d-4651-aeb1-04819a905e35

# Example posting a local image file:

import requests
r = requests.post(
    "https://api.deepai.org/api/torch-srgan",
    files={
        'image': open('/path/to/your/file.jpg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())

"""








