from selenium import webdriver

#download TD: TAM SOA/FBA TD
browser = webdriver.Firefox()
browser.get("http://worldserver9.amazon.com/ws/tools_td_export?&tdGroupId=1758&token=1016130530&openertoken=1470854050909&random=9328")
#http://worldserver9.amazon.com/ws/tools_td_export?&tdGroupId=1017&token=1016130530&openertoken=1470861537168&random=43
elem = browser.find_element_by_id('__wsDialog_button_export')
elem.click()


#Export TMX Entries from TM Database:  TAM TM_Single XPR SOA/FBA Unreviewed
browser = webdriver.Firefox()
browser.get('http://worldserver9.amazon.com/ws/tools_tm_export?&token=1700113181&openertoken=1470861815414&tmGroupId=1209&random=2851')
elem = browser.find_element_by_id('__wsDialog_button_export')
elem.click()
browser.quit()







