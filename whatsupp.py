
# whatsupp auto reply
import pyautogui
import time

# Aapko pehle WhatsApp web ya desktop application kholna hoga
# aur desired contact ya group select karna hoga.

time.sleep(15)  # 5 seconds ka wait karein taki aap prepare ho sako

for _ in range(10):  # 10 times loop chalega
    pyautogui.typewrite('Hyyy')  # Message likhega
    pyautogui.press('enter')  # Enter key press kar dega jisse message send ho jayega
    time.sleep(1)  # 1 second ka gap before sending the next message
