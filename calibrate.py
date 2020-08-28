import pyautogui

input('Hover where the maxima limit should be and hit enter')
tickmax=pyautogui.position()[1]
input('Hover where the minima limit should be and hit enter')
tickmin=pyautogui.position()[1]
input('Hover where the cancel button appears and hit enter')
cancelX=pyautogui.position()[0]
cancelY=pyautogui.position()[1]
input('Hover on buying price 1 and hit enter')
buyX1=pyautogui.position()[0]
buyY1=pyautogui.position()[1]
input('Hover on buying price 2 and hit enter')
buyX2=pyautogui.position()[0]
buyY2=pyautogui.position()[1]
input('Hover on buying price 3 and hit enter')
buyX3=pyautogui.position()[0]
buyY3=pyautogui.position()[1]
input('Hover on buying price 4 and hit enter')
buyX4=pyautogui.position()[0]
buyY4=pyautogui.position()[1]
input('Hover on buying price 5 and hit enter')
buyX5=pyautogui.position()[0]
buyY5=pyautogui.position()[1]
input('Hover on buy amount textbox and hit enter')
buyamountX=pyautogui.position()[0]
buyamountY=pyautogui.position()[1]
input('Hover on buy 100% and hit enter')
buy100x=pyautogui.position()[0]
buy100y=pyautogui.position()[1]
input('Hover on selling price 1 and hit enter')
sellX1=pyautogui.position()[0]
sellY1=pyautogui.position()[1]
input('Hover on selling price 2 and hit enter')
sellX2=pyautogui.position()[0]
sellY2=pyautogui.position()[1]
input('Hover on selling price 3 and hit enter')
sellX3=pyautogui.position()[0]
sellY3=pyautogui.position()[1]
input('Hover on selling price 4 and hit enter')
sellX4=pyautogui.position()[0]
sellY4=pyautogui.position()[1]
input('Hover on selling price 5 and hit enter')
sellX5=pyautogui.position()[0]
sellY5=pyautogui.position()[1]
input('Hover on sell amount textbox and hit enter')
sellamountX=pyautogui.position()[0]
sellamountY=pyautogui.position()[1]
input('Hover on sell 100% and hit enter')
sell100x=pyautogui.position()[0]
sell100y=pyautogui.position()[1]

print(f'''
tickmax = {tickmax}
tickmin = {tickmin}
cancelX = {cancelX}
cancelY = {cancelY}
buyX1 = {buyX1}
buyY1 = {buyY1}
buyX2 = {buyX2}
buyY2 = {buyY2}
buyX3 = {buyX3}
buyY3 = {buyY3}
buyX4 = {buyX4}
buyY4 = {buyY4}
buyX5 = {buyX5}
buyY5 = {buyY5}
buyamountX = {buyamountX}
buyamountY = {buyamountY}
buy100x = {buy100x}
buy100y = {buy100y}

sellX1 = {sellX1}
sellY1 = {sellY1}
sellX2 = {sellX2}
sellY2 = {sellY2}
sellX3 = {sellX3}
sellY3 = {sellY3}
sellX4 = {sellX4}
sellY4 = {sellY4}
sellX5 = {sellX5}
sellY5 = {sellY5}
sellamountX = {sellamountX}
sellamountY = {sellamountY}
sell100x = {sell100x}
sell100y  = {sell100y}
''')


