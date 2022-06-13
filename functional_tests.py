"""
Functional Testing script

1) check that we’ve got Django installed, and that it’s ready for us to work with.

   Method/way to check is by confirming that we can spin up Django’s development server and 
   actually see it serving up a web page, in our web browser.
   We will use Selenium Browser tool for this.

driver.get("https://www.google.ca/")
driver.implicitly_wait(5)
my_search_element_name = driver.find_element_by_name('q')
#my_search_element_name = driver.find_element(by=driver.name, value='q')
my_search_element_name.send_keys("India TV")
#find_element(by=By.NAME, value=name)
my_search_btn_name = driver.find_element_by_name('btnK')
#my_search_btn_name = driver.find_element(by=driver.name, value='tnk')
my_search_btn_name.click()

django commands:
django-admin startproject tdd_django_selenium_pytest

# using manage.py we can run development server

cd tdd_django_selenium_pytest  # [Where manage.py is accessible]

python manage.py runserver

# Django version 4.0.2, using settings 'tdd_django_selenium_pytest.settings'
# Starting development server at http://127.0.0.1:8000/    to QUIT   CTRL+BREAK
"""
import os

from selenium import webdriver

# adding path for geckodriver.exe  for Firefox web driver

os.environ['PATH'] += r";C:/Users/SUNDAY/Desktop/Sunday_Download/Firefox/geckodriver-v0.31.0-win64/"
#print(os.environ['PATH'])

browser = webdriver.Firefox()
browser.get('http://localhost:8000')


#successful assert  #Django Server is running and displaying page

assert 'The install worked successfully! Congratulations!' in browser.title

# initial failing test - to check we have Django installed and configured to serve web page
assert 'Django' in browser.title
# raise exception_class(message, screen, stacktrace)
# selenium.common.exceptions.TimeoutException: Message: Failed to read marionette port


