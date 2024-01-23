import re
from colorama import Fore, init
import requests


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


# for i in match:
#     print(i)


# with open('link_list.txt', 'w') as file:
#     for link in match:
#         file.write(link + '\n')

web_site = "https://es.wikipedia.org/wiki/N%C3%BAmero_de_tel%C3%A9fono"

try:
    result = requests.get(web_site)
    result.raise_for_status() # Raises an exception in case of HTTP error
    content = result.text
except requests.exceptions.RequestException as e:
    print(f"Error at analyze the solution: {e}")


print("-----------------------------------------3")
# Exercise: Look for all landline and mobile number, no duplicated

pattern = r"\b\d{8}\b|\b\d{9}\b"

match = re.findall(pattern, content) 

my_set_numbers = set(match)

print(my_set_numbers)

# all numbers start with number '900' and finish with '00'

espesific_number = []

for i in my_set_numbers:
    if i.startswith("900") or i.endswith("00"):
        espesific_number.append(i)
        

print(espesific_number)