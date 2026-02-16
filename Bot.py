from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com")

print("Scan QR Code to login...")
time.sleep(20)  # Time to scan QR

# Name of group or person
target_name = "Friends Group"   # Change this to your chat name

# Message trigger word
trigger_word = "Mordecai"

# Auto reply message
auto_reply = "Hello 👋 I detected my name!"

# Search chat
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.send_keys(target_name)
time.sleep(2)
search_box.send_keys(Keys.ENTER)

print("Bot is running...")

last_message = ""

while True:
    messages = driver.find_elements(By.XPATH, '//div[contains(@class,"message-in")]//span[@dir="ltr"]')
    
    if messages:
        latest_message = messages[-1].text
        
        if latest_message != last_message:
            print("New message:", latest_message)
            
            if trigger_word.lower() in latest_message.lower():
                message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                message_box.send_keys(auto_reply)
                message_box.send_keys(Keys.ENTER)
                
            last_message = latest_message
    
    time.sleep(5)
