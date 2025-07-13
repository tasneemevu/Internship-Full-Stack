i=input("Enter the name of the character: "
        ).strip().lower()

import requests

url = f"https://pokeapi.co/api/v2/pokemon/{i}"

response = requests.get(url)

data = response.json()

print(data["abilities"])
print(data["base_experience"])