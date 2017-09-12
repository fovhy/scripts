#!python3
# -*- coding: utf-8 -*-
# this for google tranlsate japanese to english
import webbrowser
import pyperclip
import time
import re

timer = 0.5        # a timer to avoid blocking
old_string = pyperclip.paste()
# the website(s) to search words on
jap_website_name = "https://translate.google.com/#ja/en/"
while(True):
    new_string = pyperclip.paste()
    if (new_string != old_string):
            old_string = new_string
            webbrowser.open(jap_website_name + old_string)
    time.sleep(timer)
