#!python3
# -*- coding: utf-8 -*-
# This is a simple script to search strings in the clipboard to a JP-CN online dict, and
# 	it is best to use with something like python, might add ability search other langauge
#   if I were to learn some new language in the future
import webbrowser
import pyperclip
import time
import re

timer = 0.5        # a timer to avoid blocking
max_words_length = 20  # default max limit for length of a word
old_string = pyperclip.paste()
# the website(s) to search words on
jap_website_name = "http://dict.hjenglish.com/jp/jc/"
# check if it is the same or not
# if it is not the same search the phrase in the dictionary
string_to_remove = '点击发音'
while(True):
    new_string = pyperclip.paste()
    if (new_string != old_string):
        if len(new_string) < max_words_length:
            old_string = new_string
            webbrowser.open(jap_website_name + old_string)
        else:
            pyperclip.copy(new_string.replace(string_to_remove,''))
    time.sleep(timer)
