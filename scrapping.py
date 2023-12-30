import json
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen 

url = 'https://news.ycombinator.com/'  

noticias_dict = {}

try:
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    # Encuentra todos los elementos tr con la clase "athing"
    elementos_athing = soup.find_all('td', class_='title')

    # Itera sobre los elementos y almacena en el diccionario
    for elemento in elementos_athing:
        enlace = elemento.find('span', class_='titleline')
        if enlace:
            titulo = enlace.a.get_text()
            link = enlace.a['href']
            noticias_dict[link] = titulo
            print(f"{link}: {titulo}")

except Exception as e:
    print(f"Error: {e}")

# Guarda el diccionario en un archivo JSON
with open('noticias.json', 'w', encoding='utf-8') as json_file:
    json.dump(noticias_dict, json_file, ensure_ascii=False, indent=2)

print("\nDiccionario completo:")
print(noticias_dict)
print("Diccionario guardado en 'noticias.json'")
