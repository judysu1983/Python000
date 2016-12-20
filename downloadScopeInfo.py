import webbrowser, sys, time, pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import fnmatch, os, csv, shutil, logging

#delete any scope_Info csv file before the downloading
os.chdir('C:\\Users\\sujudy\\Downloads')
for csv in os.listdir('.'):
    if fnmatch.fnmatch(csv,'*_scope_info_*.csv'):
        os.remove(csv)
#delete any csv in the working folder
os.chdir('C:\\csvScope')
for csv in os.listdir('.'):
    if fnmatch.fnmatch(csv,'*_scope_info_*.csv'):
        os.remove(csv)
os.chdir('C:\\Python27')

browser = webdriver.Firefox()
def downloadScopeInfo(ID):
    
    projecturl='http://worldserver9.amazon.com/ws/assignments_project_info_scope?&project='+ID
    browser.get(projecturl)

    #login, take username and password from windows+Run input
    sys.argv
    if len(sys.argv) > 2:
        name = sys.argv[1]
        pw = sys.argv[2]
    
    username=browser.find_element_by_id('username')
    username.send_keys(name)

    password=browser.find_element_by_id('password')
    password.send_keys(pw)

    login=browser.find_element_by_id('loginButton')
    login.click()
    time.sleep(1)
    
    
    savecsvButton=browser.find_element_by_css_selector('a.button:nth-child(1)')
    savecsvButton.click()
    time.sleep(3)
    pyautogui.hotkey('alt', 's')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    #browser.quit()

    #find the csv file and add project ID to the file name
    #C:\Users\sujudy\Downloads\EN-PTBR_MT_Pilot_scope_info_pt_BR.csv
    os.chdir('C:\\Users\\sujudy\\Downloads')
    for csvscope in os.listdir('.'):
        if fnmatch.fnmatch(csvscope,'*_scope_info_*.csv'):
            #move it to another folder
            shutil.move('C:\\Users\\sujudy\\Downloads\\'+csvscope,'C:\\csvScope\\'+ID+'_'+csvscope)
            print('C:\\csvScope\\'+ID+'_'+csvscope)
            import csv
            with open('C:\\csvScope\\'+ID+'_'+csvscope,'r') as f:
                r=csv.reader(f,delimiter=',')
                for row in r:
                    if row[1] ==' Total':
                        #Target Locale,Asset,Total,ICE Match,100%,100-95%,95-85%,85-75%,75-0%,Repetition,Cost Estimate (USD),MT Fuzzy Words,Multiple 100%
                        print(row[1]+','+row[2]+','+row[8])    


PJlist=open('C:\\Python27\\downloadScopeInfo.txt')
projectIDs=PJlist.readlines()
for p in projectIDs:
    p=p.strip()
    downloadScopeInfo(p)

browser.quit()

