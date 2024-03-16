from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import pyautogui


def Upload(username, password, image_path,caption='',retry=5):
    # Configuration
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.41")

    while range(retry):
        driver = webdriver.Edge(options=options)
        try:
            driver.get("https://www.instagram.com/")
            time.sleep(2)
        except:
            print("Can't reach Website!!!")
            driver.quit()
            continue

        # Login
        try:
            driver.find_element(By.XPATH, '''//*[@id="loginForm"]/div/div[1]/div/label/input''').send_keys(username)
            driver.find_element(By.XPATH, '''//*[@id="loginForm"]/div/div[2]/div/label/input''').send_keys(password)
            driver.find_element(By.XPATH, '''//*[@id="loginForm"]/div/div[3]''').click()
            time.sleep(8)
        except:
            print("Login Failed")
            driver.quit()
            continue

        # Process
        try:
            driver.find_element(By.CLASS_NAME, 'x1n2onr6').click()

            time.sleep(2)
            driver.find_element(By.XPATH,
                                '''/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]''').click()
            time.sleep(2)
            driver.find_element(By.XPATH,
                                '''/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div''').click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR,
                                '''body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div > div > div > div.xdl72j9.x1iyjqo2.xs83m0k.x15wfb8v.x3aagtl.xqbdwvv.x6ql1ns.x1cwzgcd > div.x6s0dn4.x78zum5.x5yr21d.xl56j7k.x1n2onr6.xh8yej3 > div > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1 > div > button''').click()
            time.sleep(1)
        except:
            print("Login fail")
            driver.quit()
            continue

        # Provide Image
        try:
            pyautogui.write(image_path)
            pyautogui.press("enter")
            time.sleep(2)
        except:
            print(f"File Not Found!!! {image_path}")
            driver.quit()
            continue

        # Share Post
        try:
            driver.find_element(By.XPATH,
                                '''/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button''').click()
            time.sleep(2)
            driver.find_element(By.XPATH,
                                '''/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]''').click()
            time.sleep(2)
            driver.find_element(By.XPATH,
                                '''/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div''').click()
            time.sleep(2)
            driver.find_element(By.XPATH,
                                '''/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div''').click()
            time.sleep(2)
            driver.find_element(By.XPATH,
                                '''/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div[1]/p''').send_keys(caption)
            time.sleep(2)
            driver.find_element(By.XPATH,
                                '''//html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]''').click()
            time.sleep(5)
            driver.quit()
            print("Post Shared Successfully!!!")
            break
        except:
            print("Unable to Share Post!!!")
            driver.quit()
            continue


# Upload("everydaynewscommunity","e1v2e3r4",r"C:\Users\ravis\Downloads\Dark Aesthetic Minimalist Relaxing Music YouTube Thumbnail .png")