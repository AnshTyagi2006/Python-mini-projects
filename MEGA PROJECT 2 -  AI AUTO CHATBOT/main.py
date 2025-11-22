import pyautogui
import pyperclip
import time
import google.generativeai as genai
import g4f
import re

import re

def is_last_message_from_sender(chat_history, sender_name="Mamma"):
    # Find all lines with this pattern: [date, time] Sender: message
    pattern = r"\[(.*?)\]\s(.*?):\s(.*)"
    messages = re.findall(pattern, chat_history)

    if not messages:
        return False  # No messages found

    last_sender = messages[-1][1].strip()  # sender name

    return last_sender.lower() == sender_name.lower()


    

# whatsapp web 
pyautogui.click(961 ,1048)
time.sleep(1)


while True:
    pyautogui.moveTo(710 , 210)
    pyautogui.dragTo (848  , 968 , duration=1.0 , button='left')
        # whatsapp chat 714 , 195 to 1848 923


    pyautogui.hotkey('ctrl' , 'c')
    pyautogui.click(1092 , 559)
    time.sleep(2)
    chat_history = pyperclip.paste()

    print(chat_history)

        # GENAI_API_KEY = "AIzaSyBe_Tb2qdtx6pF-sywDKF2w1jBmMuR4rk0"  
        # genai.configure(api_key=GENAI_API_KEY)
        # model = genai.GenerativeModel(model_name="gemini-1.5-pro")   
    if is_last_message_from_sender(chat_history):
        def aiProcess(chat_history):
                completion = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_4o,
                    messages=[
                        {"role" : "system" , "content" : "You are a human named Ansh who speaks hindi as well as english . You are  from India and you are coder. You analyse chat history and reply to the messages jlike Ansh in a short message no too long . Output should be the next chat response as Ansh (text message only)" },
                        {"role" : "user" , "content" : chat_history }
                    ]
                )
                return completion
                
        reply = aiProcess(chat_history)
        print(reply)

        pyautogui.click(790 , 979)
        time.sleep(2)

        pyperclip.copy(reply)
        time.sleep(0.5)

        pyautogui.hotkey('ctrl' , 'v')
        time.sleep(1)

        pyautogui.press('enter')
        pyautogui.click(1092 , 559)
        time.sleep(1)
