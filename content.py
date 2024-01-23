import re
from colorama import Fore, init
import requests
from app import content




# print(content)
print('----------------------------1')
# this to find out match as whole word, no more letters on the sides
match = re.search(r'\bboot\b', content)

# just find this words
match = re.search(r'boot', content, re.IGNORECASE)


match = re.search(r'boot|<script.*?bootstrap.*?>', content, re.IGNORECASE)

if match:
    print ("Found")
else:
    print ("Not Found")


print("-----------------------------------------2")

match = re.search(r'boot', content, re.IGNORECASE)


if match:
    print ("Found")
else:
    print ("Not Found")



print("-----------------------------------------3")
# Exercise: Find email addresses

match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', content)


print(match)


    
    