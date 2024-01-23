import re
from colorama import Fore, init
import requests


web_site = "https://es.wikipedia.org/wiki/Espa%C3%B1a"

try:
    result = requests.get(web_site)
    result.raise_for_status() # Raises an exception in case of HTTP error
    content = result.text
except requests.exceptions.RequestException as e:
    print(f"Error at analyze the solution: {e}")

# print(content)
    
print("-----------------------------------------1")
# Exercise: Find how many times show the word 'España' in the page
match = re.findall(r'españa', content, re.IGNORECASE) 


print(len(match)) # 825 times

print("-----------------------------------------2")
# Exercise: Find all links

pattern = r'https?://[^\s\'"]+'

match = re.findall(pattern, content, re.IGNORECASE)

for i in match:
    print(i) 


print("-----------------------------------------3")

# Exercise: find all inside anchor tag
pattern = r'(?<=>).*(?=<\/a)'

match = re.findall(pattern, content, re.IGNORECASE)

print(match)


# Exercise: find all anchors text
pattern = r'(?<=>)[^<]*(?=<\/a)'

match = re.findall(pattern, content, re.IGNORECASE)

print(match)




