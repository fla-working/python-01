import re
from colorama import Fore, init
import requests

# inizialize colorama after every execution
init(autoreset=True)

web_site = "https://es.wikipedia.org/wiki/Correo_electr%C3%B3nico"

try:
    result = requests.get(web_site)
    result.raise_for_status() # Raises an exception in case of HTTP error
    content = result.text
except requests.exceptions.RequestException as e:
    print(f"Error at analyze the solution: {e}")

# print(content)
    
print("-----------------------------------------1")
# Exercise: Find email addresses
match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', content) # ['ejemplo@máquina.com', 'Juan.Nadie@ejemplo.com', 'ana@a.org', 'bea@b.com']


print(match)

    
print("-----------------------------------------2")
# Exercise: Find all URLs

pattern = r'https?://[^\s\'"]+'


match = re.findall(pattern, content)


for i in match:
    print(i)


with open('link_list.txt', 'w') as file:
    for link in match:
        file.write(link + '\n')
