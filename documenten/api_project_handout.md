# 🌐 Python Project: Werken met een Web API (PokeAPI)

## 🎯 Doel van dit project

In dit mini-project leer je:

- wat een **API** is
- hoe je in Python een **HTTP-request** doet
- hoe je **JSON-data** inleest en gebruikt
- hoe je fouten opvangt (foute naam, geen verbinding, …)

We gebruiken de **PokeAPI**: een gratis API met gegevens over Pokémon.

---

## 1. Wat is een API?

Een **API (Application Programming Interface)** is een soort “dienst” op het internet:

- Jij stuurt een **vraag** (request) naar een server  
- De server stuurt een **antwoord** (response) terug, meestal in **JSON-formaat**

Voorbeeld van een API-adres:

```
https://pokeapi.co/api/v2/pokemon/pikachu
```

---

## 2. Voorbereiding

### Vereisten

- Python 3  
- De `requests`-bibliotheek

Installeren:

```bash
pip install requests
```

---

## 3. Eerste stappen met `requests`

Maak een nieuw bestand `pokemon_api.py`.

```python
import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)

print(response.status_code)
data = response.json()

print(data["name"])
print(data["height"])
print(data["weight"])
```

---

## 4. Opdracht A — Pokémon opzoeken

Schrijf een programma dat:

1. aan de gebruiker een Pokémonnaam vraagt  
2. de API-URL opbouwt  
3. met `requests.get()` de data ophaalt  
4. de volgende informatie toont:  
   - naam  
   - id  
   - height  
   - weight  
   - types  

---

## 5. Opdracht B — Foutafhandeling

Als de gebruiker een foute naam ingeeft:

- API geeft statuscode **404**  
- Jij toont:  
  ```
  Pokémon not found, try again.
  ```

Check bijvoorbeeld:

```python
if response.status_code != 200:
    print("Pokémon not found")
```

---

## 6. Opdracht C — Meerdere Pokémon opzoeken

Maak een loop:

```
Enter a Pokémon name (or 'quit'): pikachu
...
Enter a Pokémon name (or 'quit'): ditbestaatniet
Pokémon not found
Enter a Pokémon name (or 'quit'): quit
```

---

## 7. Extra uitdaging — Random Pokémon

Gebruik:

```python
import random
random_id = random.randint(1, 300)
```

en dan:

```
https://pokeapi.co/api/v2/pokemon/<id>
```

---

## 8. Tips

- Begin simpel (pikachu hardcoded)
- Print `data.keys()` om de structuur te ontdekken  
- Wees creatief: abilities, moves, stats…

---

## 🎉 Veel succes!

Je werkt nu met **echte webdata** — een belangrijke skill in moderne softwareontwikkeling!

