import requests
import random

looping = True

print("\n Hämta Personnummer Från Skatteverket! \n")

while looping:
    randomtal = random.randint(1, 100)
    url = f"https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763/json?_offset={randomtal}&_limit=1"

    req = requests.get(url)

    jsondata = req.json()
    print(req)
    lista = jsondata['results']
    personnummer = lista[0]['testpersonnummer']
    print(personnummer)

    entill = input("\n vill du slumpa ett personnummer till? J/N \n")

    if(entill == "n" or entill == "N"):
        break