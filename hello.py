import requests
from bs4 import BeautifulSoup

url = "https://www.bucataria.lidl.ro/retete/invartita-cu-mere"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

nume_reteta = soup.find('h1', class_='oRecipeHeader-title').text.strip()

timp = soup.find('div', class_='mTimer-time').text.strip()

container_dificultate = soup.find('div', class_='oRecipeHeader-meta')
dificultate = len(container_dificultate.find_all('span', class_='icon_chefsCapFilled'))

ingrediente = {ing.text.strip() for ing in soup.find_all('span', class_='oIngredientBox-ingName')}

print(f"Numele retetei: {nume_reteta}")
print(f"Timp: {timp}")
print(f"Dificultate: {dificultate}")
print("Ingrediente:")
for ing in ingrediente:
    print(f"- {ing}")