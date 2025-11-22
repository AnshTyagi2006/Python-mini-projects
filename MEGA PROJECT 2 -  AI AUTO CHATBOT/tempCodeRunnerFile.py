pyautogui.hotkey('ctrl' , 'c')
    pyautogui.click(1092 , 559)
    time.sleep(2)
    chat_history = pyperclip.paste()

    print(chat_history)
