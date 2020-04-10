import appium
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pprint import pprint
import time
import base64
from PIL import Image
from io import BytesIO


# *******************Setting Desired Capabilities****************************

caps = {}
caps['platformName'] = 'Android'
caps['deviceName'] = 'Pixel_2_API_29'
caps['appPackage'] = 'com.google.android.apps.photos'
caps['osVersion'] = '10'
caps['automationName'] = 'UiAutomator2'
caps['project'] = 'Appium-Challenge'
caps['build'] = 'Headspin'
caps['name'] = 'Google-Photos-Image-Appium-Challenge'
caps['autoGrantPermissions'] = True
caps['appActivity'] = '.home.HomeActivity'
caps['appPath'] = '/Users/elizabethbland/Desktop/apk/02-03-20/com.google.android.apps.photos-google_pixel_2-29/base.apk'

#*****************************************************************************


#****************************************************************************

#Set up conncection to AndroidDriver via Appium
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", caps)
actions = TouchAction(driver)

#*****************************************************************************

# Image File Path
img = 'image-appium-challenge.jpg'
# Location on phone pushing image to 
ANDROID_PHOTO_PATH = '/sdcard/Pictures/image-appium-challenge.jpg'
# image_uploaded_path = 'mt/sdcard/Pictures/storage/emulated/0/DCIM/Restored/image-appium-challenge.jpg'
img_path = 'Users/elizabethbland/Desktop/image-appium-challenge.jpg'

#*************************** Begin Test Script ******************************************

# Slide up
# TouchAction(driver)   .press(x=546, y=1614)   .move_to(x=542, y=670)   .release()   .perform()

# Click backup switch to turn off and avoid having to login
# backupSwitch = driver.find_element_by_id("com.google.android.apps.photos:id/auto_backup_switch")
# backupSwitch.click()
# driver.implicitly_wait(10)

el2 = driver.find_element_by_id("com.google.android.apps.photos:id/done_button")
el2.click()

# Touch outside to avoid login 
touchOutside = TouchAction(driver).tap(x=585, y=434).perform()
driver.implicitly_wait(10)

# Click keepOff button after touching to avoid login
keepOff = driver.find_element_by_id("android:id/button2")
keepOff.click()
driver.implicitly_wait(10)

# Push Image to device
with open(img,"rb") as f:
    image_data = f.read()
    base64_data = base64.b64encode(image_data,altchars=None)
    
    finaldata = str(base64_data,encoding='utf-8')
    #print(finaldata)
    driver.push_file("/sdcard/Pictures",finaldata)
    driver.push_file(ANDROID_PHOTO_PATH,finaldata)

# Moving this outside code to push made it work in emulator
driver.push_file(ANDROID_PHOTO_PATH,finaldata)

driver.push_file(ANDROID_PHOTO_PATH,'Users/elizabethbland/Desktop/image-appium-challenge.jpg')
# driver.push_file(ANDROID_PHOTO_PATH + "/" + 'Users/elizabethbland/Desktop/', img)
driver.implicitly_wait(1000)

# Pull Folder
getFolder = driver.pull_folder(ANDROID_PHOTO_PATH);
print("getFolder")
pprint(getFolder)

el3 = driver.find_element_by_id("com.google.android.apps.photos:id/done_button")
el3.click()
el4 = driver.find_element_by_id("com.google.android.apps.photos:id/welcomescreens_skip_button")
el4.click()
el5 = driver.find_element_by_accessibility_id("Photo taken on Feb 24, 2020 8:38:48 PM")
el5.click()
el6 = driver.find_element_by_accessibility_id("More options")
el6.click()
el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[5]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.RecyclerView/android.widget.TextView[3]")
el7.click()
el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[5]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView[1]")
el8.click()



Find uploaded image on device and click
driver.update_settings({"getMatchedImageResult": True})
el9 = driver.find_element_by_image('storage/emulated/0/DCIM/Restored/image-appium-challenge.jpg')
el9.click()
el9.get_attribute('visual')

# TouchAction(driver).tap(x=151, y=836).perform()
# Click More Options on top right of screen to get info about photo
# el2 = driver.find_element_by_id("com.google.android.apps.photos:id/More Options")
# el2.click()

# Debug
TouchAction(driver).tap(x=139, y=472).perform()
driver.implicitly_wait(1000)
# driver.implicitly_wait(30)

# Change orientation
el10 = driver.orientation = "LANDSCAPE"
driver.implicitly_wait(10)









# el5 = driver.find_element_by_xpath("mt/sdcard/Pictures/storage/emulated/0/DCIM/Restored/image-appium-challenge.jpg")
# el5.click()



driver.quit()

#****************************************************************************

# #Set up conncection to AndroidDriver via Appium
# driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# # driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", caps)
# actions = TouchAction(driver)

# #*****************************************************************************

# # Image File Path
# img = 'image-appium-challenge.jpg'
# # Location on phone pushing image to 
# device_photo_path = 'mt/sdcard/Pictures'
# # image_uploaded_path = 'mt/sdcard/Pictures/storage/emulated/0/DCIM/Restored/image-appium-challenge.jpg'
# source_path = 'Users/elizabethbland/Desktop/image-appium-challenge.jpg'

# #*************************** Begin Test Script ******************************************


# # Slide up
# # TouchAction(driver)   .press(x=546, y=1614)   .move_to(x=542, y=670)   .release()   .perform()

# # Click backup switch to turn off and avoid having to login
# # backupSwitch = driver.find_element_by_id("com.google.android.apps.photos:id/auto_backup_switch")
# # backupSwitch.click()
# # driver.implicitly_wait(10)

# # Touch outside to avoid login 
# touchOutside = TouchAction(driver).tap(x=585, y=434).perform()
# driver.implicitly_wait(10)
# # screenshotBase64 = driver.get_screenshot_as_base64()

# # Click keepOff button after touching to avoid login
# keepOff = driver.find_element_by_id("android:id/button2")
# keepOff.click()
# driver.implicitly_wait(10)
# # screenshotBase64 = driver.get_screenshot_as_base64()

# # Push Image to device
# def convert_image_to_base64(image_filename):
#     with open("image-appium-challenge.jpg", 'rb') as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()
#     return encoded_string
#     print(convert_image_to_base64(img))

# driver.push_file(device_photo_path, convert_image_to_base64(img))
# driver.implicitly_wait(80)
# # screenshotBase64 = driver.get_screenshot_as_base64()

# # Click on uploaded Photo
# # wait = WebDriverWait(driver, 10)
# # driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[5]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView[1][contains(.,'Photo Taken')]")
# # element.click()
# # driver.implicitly_wait(30)
# # screenshotBase64 = driver.get_screenshot_as_base64()
# TouchAction(driver).tap(x=151, y=836).perform()
# # Click More Options on top right of screen to get info about photo
# el1 = driver.find_element_by_accessibility_id("com.google.android.apps.photos:id/More Options")
# el1.click()

# # Click on uploaded Photo
# TouchAction(driver).tap(x=170, y=499).perform()
# driver.implicitly_wait(30)
# # screenshotBase64 = driver.get_screenshot_as_base64()

# # Change orientation
# el2 = driver.orientation = "LANDSCAPE"
# driver.implicitly_wait(10)
# # screenshotBase64 = driver.get_screenshot_as_base64()







# # el5 = driver.find_element_by_xpath("mt/sdcard/Pictures/storage/emulated/0/DCIM/Restored/image-appium-challenge.jpg")
# # el5.click()



# driver.quit()