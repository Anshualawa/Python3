def Program():
    import pyautogui as p
    from time import sleep
    et = p.press('enter')
    sleep(5)
    p.hotkey('winleft')
    sleep(3)
    # p.typewrite('Visual Studio Code',0.2)
    p.typewrite('Terminal',0.2)
    sleep(3)
    p.press('enter')
    sleep(3)
    p.write('ls')
    p.press('enter')
    p.write('cd Desktop')
    p.press('enter')
    p.typewrite('mkdir Program',0.2)
    sleep(3)
    p.press('enter')
    p.typewrite('cd Program',0.2)
    sleep(3)
    p.press('enter')
    p.typewrite('code .',0.2)
    p.press('enter')



# Call Function
# print(Program())