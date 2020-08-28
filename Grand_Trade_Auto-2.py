import pyautogui
import time
#########################################################################
tickmax = 251
tickmin = 488
cancelX = 736
cancelY = 699
buyX1 = 826
buyY1 = 363
buyX2 = 826
buyY2 = 379
buyX3 = 826
buyY3 = 398
buyX4 = 823
buyY4 = 415
buyX5 = 827
buyY5 = 429
buyamountX = 922
buyamountY = 592
buy100x = 1036
buy100y = 631

sellX1 = 833
sellY1 = 311
sellX2 = 831
sellY2 = 297
sellX3 = 831
sellY3 = 277
sellX4 = 831
sellY4 = 264
sellX5 = 831
sellY5 = 247
sellamountX = 1198
sellamountY = 589
sell100x = 1328
sell100y  = 633
########################################################################
state = 0
input('Press enter and get ready, program starts in 5 seconds.')
time.sleep(5)
tickunit=(abs(tickmax-tickmin))//10
ticklims = [ i for i in range(tickmin,tickmax,-tickunit)]
ticklims.reverse()
print(ticklims)
start = time.time()
while True:
       tick = pyautogui.locateOnScreen('tick.png')[1]
       end = time.time()
       if abs(end-start) < 200:
              if pyautogui.locateOnScreen('filled.png') != None:
                     start =time.time()
                     if state == 0:
                            if tick > ticklims[0] and tick < ticklims[1]:
                                   pyautogui.click(buyX1,buyY1)
                                   pyautogui.click(buyamountX,buyamountY)
                                   pyautogui.press('backspace', presses=8)
                                   pyautogui.typewrite('0000')
                                   pyautogui.click(buy100x,buy100y)
                                   pyautogui.click('buy.png')
                                   pyautogui.click(sellX5,sellY5)
                                   time.sleep(3)
                            elif tick > ticklims[1] and tick < ticklims[2]:
                                   pyautogui.click(buyX1,buyY1)
                                   pyautogui.click(buyamountX,buyamountY)
                                   pyautogui.press('backspace', presses=8)
                                   pyautogui.typewrite('0000')
                                   pyautogui.click(buy100x,buy100y)
                                   pyautogui.click('buy.png')
                                   pyautogui.click(sellX4,sellY4)
                                   time.sleep(3)
                            elif tick > ticklims[2] and tick < ticklims[3]:
                                   pyautogui.click(buyX1,buyY1)
                                   pyautogui.click(buyamountX,buyamountY)
                                   pyautogui.press('backspace', presses=8)
                                   pyautogui.typewrite('0000')
                                   pyautogui.click(buy100x,buy100y)
                                   pyautogui.click('buy.png')
                                   pyautogui.click(sellX3,sellY3)
                                   time.sleep(3)
                            elif tick > ticklims[3] and tick < ticklims[4]:
                                   pyautogui.click(buyX1,buyY1)
                                   pyautogui.click(buyamountX,buyamountY)
                                   pyautogui.press('backspace', presses=8)
                                   pyautogui.typewrite('0000')
                                   pyautogui.click(buy100x,buy100y)
                                   pyautogui.click('buy.png')
                                   pyautogui.click(sellX2,sellY2)
                                   time.sleep(3)
                            elif tick > ticklims[4] and tick < ticklims[5]:
                                   pyautogui.click(buyX1,buyY1)
                                   pyautogui.click(buyamountX,buyamountY)
                                   pyautogui.press('backspace', presses=8)
                                   pyautogui.typewrite('0000')
                                   pyautogui.click(buy100x,buy100y)
                                   pyautogui.click('buy.png')
                                   pyautogui.click(sellX1,sellY1)
                                   time.sleep(3)
                            elif tick > ticklims[5] and tick < ticklims[6]:
                                   pyautogui.click(buyX1,buyY1)
                                   pyautogui.click(buyamountX,buyamountY)
                                   pyautogui.press('backspace', presses=8)
                                   pyautogui.typewrite('0000')
                                   pyautogui.click(buy100x,buy100y)
                                   pyautogui.click('buy.png')
                                   pyautogui.click(sellX1,sellY1)
                                   time.sleep(3)
                            elif tick > ticklims[6] and tick < ticklims[7]:
                                   pyautogui.click(buyX2,buyY2)
                                   pyautogui.click(buyamountX,buyamountY)
                                   pyautogui.press('backspace', presses=8)
                                   pyautogui.typewrite('0000')
                                   pyautogui.click(buy100x,buy100y)
                                   pyautogui.click('buy.png')
                                   pyautogui.click(sellX1,sellY1)
                                   time.sleep(3)
                            elif tick > ticklims[7] and tick < ticklims[8]:
                                   pyautogui.click(buyX3,buyY3)
                                   pyautogui.click(buyamountX,buyamountY)
                                   pyautogui.press('backspace', presses=8)
                                   pyautogui.typewrite('0000')
                                   pyautogui.click(buy100x,buy100y)
                                   pyautogui.click('buy.png')
                                   pyautogui.click(sellX1,sellY1)
                                   time.sleep(3)
                            elif tick > ticklims[8] and tick < ticklims[9]:
                                   pyautogui.click(buyX4,buyY4)
                                   pyautogui.click(buyamountX,buyamountY)
                                   pyautogui.press('backspace', presses=8)
                                   pyautogui.typewrite('0000')
                                   pyautogui.click(buy100x,buy100y)
                                   pyautogui.click('buy.png')
                                   pyautogui.click(sellX1,sellY1)
                                   time.sleep(3)
                            elif tick > ticklims[9] and tick < ticklims[10]:
                                   pyautogui.click(buyX5,buyY5)
                                   pyautogui.click(buyamountX,buyamountY)
                                   pyautogui.press('backspace', presses=8)
                                   pyautogui.typewrite('0000')
                                   pyautogui.click(buy100x,buy100y)
                                   pyautogui.click('buy.png')
                                   pyautogui.click(sellX1,sellY1)
                                   time.sleep(3)
                            
                            
                            state = 1
                            
                     elif state == 1:
                            
                            pyautogui.click(sellamountX,sellamountY)
                            pyautogui.press('backspace', presses=8)
                            pyautogui.typewrite('0000')
                            pyautogui.click(sell100x,sell100y)
                            pyautogui.click('sell.png')
                            time.sleep(3)

                            state = 0

              else:
                     pass
              
       else:
              try:
                     cancelX = pyautogui.locateOnScreen('cancel.png')[0]+555
                     cancelY = pyautogui.locateOnScreen('cancel.png')[1]
                     pyautogui.click(
                            pyautogui.locateOnScreen('cancel.png')[0]+555
                            ,pyautogui.locateOnScreen('cancel.png')[1])
                     pyautogui.click(
                            pyautogui.locateOnScreen('cancel.png')[0]+100
                            ,pyautogui.locateOnScreen('cancel.png')[1]-300)
                     time.sleep(1)
                     pyautogui.click(cancelX,cancelY)
                     time.sleep(1)
                     pyautogui.click(cancelX,cancelY)
                     time.sleep(1)
                     pyautogui.click(cancelX,cancelY)
                     time.sleep(1)
                     pyautogui.click(cancelX,cancelY)
                     time.sleep(1)
                     pyautogui.click(cancelX,cancelY)
                     
                     
                         
              except:
                     start=time.time()
              
              
