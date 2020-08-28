import pyautogui
import time
#########################################################################
buyX = 849
buyY = 366
buyamountX = 902
buyamountY = 592
buy25x = 890
buy25y = 632
buy50x = 941
buy50y = 629
buy75x = 989
buy75y = 634
buy100x = 1033
buy100y = 635

sellX = 826
sellY = 309
sellamountX = 1180
sellamountY = 592
sell25x = 1173
sell25y = 635
sell50x = 1228
sell50y = 633
sell75x = 1278
sell75y = 632
sell100x = 1325
sell100y  = 632
########################################################################
state = 0
input('Press enter and get ready, program starts in 5 seconds.')
time.sleep(5)
start = time.time()
while True:
       end = time.time()
       if abs(end-start) < 120:
              if pyautogui.locateOnScreen('filled.png') != None:
                     start =time.time()
                     if state == 0:
                            pyautogui.click(buyX,buyY)
                            pyautogui.click(buyamountX,buyamountY)
                            pyautogui.press('backspace', presses=8)
                            pyautogui.typewrite('0000')
                            pyautogui.click(buy25x,buy25y)
                            pyautogui.click('buy.png')
                            time.sleep(15)
                            pyautogui.click(buyX,buyY)
                            pyautogui.click(buyamountX,buyamountY)
                            pyautogui.press('backspace', presses=8)
                            pyautogui.typewrite('0000')
                            pyautogui.click(buy50x,buy50y)
                            pyautogui.click('buy.png')
                            time.sleep(15)
                            pyautogui.click(buyX,buyY)
                            pyautogui.click(buyamountX,buyamountY)
                            pyautogui.press('backspace', presses=8)
                            pyautogui.typewrite('0000')
                            pyautogui.click(buy75x,buy75y)
                            pyautogui.click('buy.png')
                            time.sleep(15)
                            pyautogui.click(buyX,buyY)
                            pyautogui.click(buyamountX,buyamountY)
                            pyautogui.press('backspace', presses=8)
                            pyautogui.typewrite('0000')
                            pyautogui.click(buy100x,buy100y)
                            pyautogui.click('buy.png')
                            
                            state = 1
                     elif state == 1:
                            pyautogui.click(sellX,sellY)
                            pyautogui.click(sellamountX,sellamountY)
                            pyautogui.press('backspace', presses=8)
                            pyautogui.typewrite('0000')
                            pyautogui.click(sell25x,sell25y)
                            pyautogui.click('sell.png')
                            time.sleep(15)
                            pyautogui.click(sellX,sellY)
                            pyautogui.click(sellamountX,sellamountY)
                            pyautogui.press('backspace', presses=8)
                            pyautogui.typewrite('0000')
                            pyautogui.click(sell50x,sell50y)
                            pyautogui.click('sell.png')
                            time.sleep(15)
                            pyautogui.click(sellX,sellY)
                            pyautogui.click(sellamountX,sellamountY)
                            pyautogui.press('backspace', presses=8)
                            pyautogui.typewrite('0000')
                            pyautogui.click(sell75x,sell75y)
                            pyautogui.click('sell.png')
                            time.sleep(15)
                            pyautogui.click(sellX,sellY)
                            pyautogui.click(sellamountX,sellamountY)
                            pyautogui.press('backspace', presses=8)
                            pyautogui.typewrite('0000')
                            pyautogui.click(sell100x,sell100y)
                            pyautogui.click('sell.png')
                            
                            state = 0

              else:
                     pass
              
       else:
              try:
                     pyautogui.click(
                            pyautogui.locateOnScreen('cancel.png')[0]+555
                            ,pyautogui.locateOnScreen('cancel.png')[1])
                     pyautogui.click(
                            pyautogui.locateOnScreen('cancel.png')[0]+100
                            ,pyautogui.locateOnScreen('cancel.png')[1]-300)
                     
              except:
                     start=time.time()
              
              
