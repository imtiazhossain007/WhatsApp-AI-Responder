from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import google.generativeai as genai

API_key = "YOUR API KEY"
genai.configure(api_key=API_key)

model = genai.GenerativeModel("gemini-2.5-flash")
custom_text = " " #A text you can add how you want your chatbot to reply

options = Options()
options.add_argument(r"user-data-dir=C:\selenium_profile") #Creates a seperate chrome profile
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/") #Opens the watsapp website

wait = WebDriverWait(driver, 60)
search_box = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="side"]//div[@contenteditable="true"]'))
) # Waits for 60 sec untill the elements appears

print("press ctrl+c to stop")

def is_unknown_number():
    try:
        chat_title = driver.find_elements(By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span')
        if chat_title:
            title_text = chat_title[0].text
            if '+91' in title_text:
                return True
        return False
    except:
        return False

def is_valid_reply(reply):
    if not reply or not isinstance(reply, str):
        return False
    if reply.strip() == "":
        return False
    return True

while True:
    try:
        unread_chats = driver.find_elements(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span/span')
        
        if unread_chats:
            print(f"Found {len(unread_chats)} unread chat(s). Opening...")
            for chat in unread_chats:
                try:
                    chat.click()
                    time.sleep(3)
                    
                    if is_unknown_number():
                        print("Skipping unknown number with +91")
                        continue
                        
                    print("Opened a chat with unread messages.")
                    time.sleep(2)
                    
                    try:
                        messages = driver.find_elements(By.CSS_SELECTOR,"#main div.message-in div.copyable-text")
                        time.sleep(2)
                    except:
                        print("Failed to get messages, continuing...")
                        continue
                    
                    if messages:
                        latest_msg = messages[-1].text
                        print(f"Latest message: {latest_msg}")
                        
                        try:
                            response = model.generate_content(custom_text + latest_msg)
                            reply = response.text
                            print(f"Gemini reply: {reply}")
                            
                            if not is_valid_reply(reply):
                                print("Skipping invalid reply")
                                continue
                                
                            try:
                                msg_box = wait.until(EC.presence_of_element_located(( 
                                By.XPATH,
                                '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]/p'
                                )))
                                msg_box.click()
                                msg_box.send_keys(reply)
                                time.sleep(2)
                                msg_box.send_keys(Keys.ENTER)
                                print("Reply sent!")
                                time.sleep(3)
                            except:
                                print("Message box not found, continuing...")
                                continue
                                
                        except Exception as e:
                            print(f"Error generating reply: {e}")
                            continue
                except:
                    print("Stale element, continuing to next chat...")
                    continue

    except KeyboardInterrupt:
        print("program stopped by user")
        driver.quit()
        exit()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
        try:
            driver.current_url
        except:
            print("Browser window closed, exiting...")
            break
        continue