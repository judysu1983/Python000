from selenium import webdriver

url1="http://worldserver9.amazon.com/ws/assignments_tasks?&token=1724436503&project=509613"

#download TD: TAM SOA/FBA TD
browser = webdriver.Firefox()
browser.get(url1)
#http://worldserver9.amazon.com/ws/tools_td_export?&tdGroupId=1017&token=1016130530&openertoken=1470861537168&random=43
elem = browser.find_element_by_css_selector('td.paged_table_content:nth-child(2) > a:nth-child(1)')
elem.click()








