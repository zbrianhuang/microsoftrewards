import pyautogui as pg
import time
import subprocess as sb

def new_tab():
    with pg.hold('ctrl'):
        pg.press('t')


def close_window():
    with pg.hold('ctrl'):
        pg.press('w')

def close_tab():
    with pg.hold('ctrl'):
        with pg.hold('shift'):
            pg.press('tab')

    with pg.hold('ctrl'):
        pg.press('w')

def write():
    pg.typewrite(phrase, 0.03)
    pg.press('enter')
    time.sleep(1)


    #Firefox Windows
sb.Popen("C://Program Files//Mozilla Firefox//firefox.exe")
    
file_windows = open("site.txt")
phrase = file_windows.readline


for phrase in file_windows:

    write()
    new_tab()
    close_tab()
  


    file_windows.close

#Edge
sb.Popen("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe")
time.sleep(5)

file_edge = open("site.txt")
phrase = file_edge.readline


for phrase in file_edge:

    write()
    new_tab()
    close_tab()


close_window()
file_edge.close
