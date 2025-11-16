# 🐍 Python Project: Tekstgebaseerd Avonturenspel — Leerlingenhand-out

## 🎮 Escape the Room — Mini-project

In dit project maak je een **klein tekstgebaseerd avonturenspel** in Python.  
Je beweegt door kamers, raapt voorwerpen op en probeert uiteindelijk te ontsnappen.

Dit project leert je:
- werken met **functions**
- **lists** en **dictionaries** gebruiken
- input verwerken
- je code opdelen in duidelijke stukjes
- een echt mini-spel bouwen

---

# 📌 1. Het idee

Je zit opgesloten in een gebouw.  
Er zijn verschillende kamers, elk met een beschrijving, voorwerpen en uitgangen.

Je doel: **vind de sleutel en ontsnap!**

Je spel moet minstens dit kunnen:
- player kan rondwandelen (`north`, `south`, …)
- player kan rondkijken (`look`)
- player kan items oprapen (`take <item>`)
- player kan zijn inventaris bekijken (`inventory`)
- player kan het spel afsluiten (`quit`)
- player kan de sleutel gebruiken (`use key`)

---

# 📌 3. Jouw opdracht


### Bestudeer de theorie over dictionary's in Python

Bekijk kort op [](https://python.arnevandenbussche.be/Nederlands/h05-collecties/#dictionaries) hoe een dictionary in Python werkt:

- Hoe selecteer je een element?
- Hoe voeg je een element toe?

Bekijk ook nog eens hoe je een element aan een List toevoegt en een element verwijdert.

### Startcode bestuderen

Samen bekijken we de code van het startersbestand. Je vindt dit bestand in de map escape_room. Download het bestand en voer het al eens uit op je computer.

We gaan deze code nu verder uitwerken.

### Functies uitwerken

Je ziet dat heel wat functies leeg zijn. 

Werk de volgende functies uit:

- `check_win_condition(state)`: deze functie test gewoon of je al ontsnapt bent. Je moet hier de waarde van een veld in `state` bekijken.
- `look(state)`: je zult hier weergeven wat de inhoud van de huidige kamer is. Je zal eerst in state de huidige room is (location). Uit rooms zal je kijken wat de gegevens van die kamer zijn en je zal de beschrijving en de items weergeven.
- `move(state, direction)`: met deze functie zullen we state aanpassen. We gaan nagaan wat de huidige ruimte is, of de aangegeven richting wel van toepassing is in deze kamer. Als dat zo is, dan passen we de locatie aan naar deze nieuwe kamer en we gebruiken de look-functie om informatie over die kamer weer te geven.
- `take_item(state, item_name)`: met deze functie zal je een item in de huidige kamer opnemen. Je zal eerste moeten nagaan of het item in die kamer voorkomt. Als dat zo is, dat verwijder je het uit de kamer en voeg je het aan je inventory toe.
- `show_inventory(state)`: toon de inhoud van je huidige voorraad (inventory).

### ✔️ Basisuitbreidingen
- Voeg minstens **één extra kamer** toe  
- Voeg minstens **één extra item** toe  
- Maak minstens **één puzzel of blokkerend element**  
  Voorbeelden:
  - een code die je moet ingeven  
  - een deur die pas opent na `use crowbar`  
  - een item dat pas zichtbaar wordt na `look` x keer

---

# 📌 4. Uitbreidingsideeën (optioneel)

### 🔹 1. Health-systeem
- vijand die af en toe schade doet  
- eten dat je health herstelt  

### 🔹 2. Inventarislimiet
- max. 3 items dragen  
- items droppen (`drop <item>`)


---

# 📌 5. Tips & Aanpak

### ✔️ 1. Werk stap voor stap  
Begin eenvoudig.

### ✔️ 2. Test na elke toevoeging  
Kleine fouten vind je zo makkelijker.

### ✔️ 3. Gebruik functies  
Maak je eigen functies bij:
- `def inspect(item):`
- `def open_chest():`
- `def solve_puzzle():`

### ✔️ 4. Maak je eigen map (kamerplan)
Teken op papier hoe alles verbonden is.

---

# ✔️ Veel succes!  
Gebruik je creativiteit — dit is jouw mini-adventure game! 😊
