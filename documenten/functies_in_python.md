# 🐍 Functies in Python — Hand-out

### Voor leerlingen (inleidende workshop Python)

---

## 🎯 Doelen
Na dit hoofdststuk kan je:
- begrijpen waarom functies nuttig zijn  
- zelf functies definiëren  
- functies met parameters en return-waarden schrijven  
- functies oproepen vanuit andere code  
- eenvoudige problemen opdelen in kleinere stukken  

---

# 1. Wat is een functie?

Een **functie** is een herbruikbaar stukje code dat een naam krijgt.  
Je gebruikt functies om:
- code overzichtelijker te maken  
- herhaling te vermijden  
- logica op te splitsen in kleine stukken  

In Python definieer je een functie met `def`.

---

# 2. Een eenvoudige functie

```python
def greet():
    print("Hello!")
```

Functie **oproepen**:

```python
greet()
```

---

# 3. Functies met parameters

Functies kunnen informatie (argumenten) ontvangen.

```python
def greet(name):
    print(f"Hello, {name}!")
```

Gebruik:

```python
greet("Emma")
greet("Liam")
```

---

# 4. Functies met return-waarde

Soms wil je dat een functie een resultaat teruggeeft.

```python
def add(a, b):
    return a + b
```

Gebruik:

```python
result = add(5, 3)
print(result)
```

---

# 5. Meerdere functies samen gebruiken

```python
def is_even(n):
    return n % 2 == 0

def show_even_message(n):
    if is_even(n):
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

show_even_message(12)
show_even_message(7)
```

---

# 6. Waarom functies?

- Je vermijdt dubbele code  
- Je programma wordt duidelijker  
- Je kan makkelijker fouten opsporen  
- Je kan complexe taken opdelen  

# 7. Functies in modules

Python bevat zelf heel wat ingebouwde functies. Een voorbeeld is de functie `max()`

```python
maximum = max(1, 3, 5, 6) # 6
```

Soms zitten die functies in module. Dan moet je eerst de module importeren:

```python
import math
vierkantswortel = math.sqrt(2)
```

Je kan ook één specifieke functie uit een module importeren en die dan een naam geven.

```python
from math import sqrt as vierkantswortel

print(f"De vierkantswortel van 16 is {vierkantswortel(16)}.")
```

# 8. Functies in eigen modules

Elk Pythonbestand dat je bouwt, beschouwen we als een module. Je kan dus functies uit Pythonmodules die je zelf geschreven hebt, importeren.

We kunnen dit illusteren met een voorbeeld. Stel dat je een Pythonbestand `mijnfuncties.py` geschreven hebt.

```python
# mijnfuncties.py
def welkom(naam):
  print(f"Welkom {naam}")

def goedemorgen(naam):
    print(f"Goedemorgen {naam}")
```

Dan kunnen we in dezelfde map een ander bestand `begroeting.py` ontwikkelen die er dan zo uitziet:

```python
# begroeting.py
from mijnfuncties import welkom, goedemorgen

naam = input("Geef je naam: ")
welkom(naam)
goedemorgen(naam)
```

# 9. if \_\_name\_\_ == " \_\_main\_\_" 

Wanneer we een script schrijven dat functies bevatten, moeten we er rekening mee houden dat er een moment kan komen dat andere stukken code dit script als module kunnen importeren om gebruik te kunnen maken van die functie. In dat geval is het de bedoeling dat de functies gebruikt worden, maar niet dat het script bij het importeren onmiddellijk uitgevoerd wordt. 

We moeten dus in ons script een onderscheid maken tussen top-level code, dat is code die direct in het aangeroepen script staat en daar uitgevoerd wordt, en code die in functies verpakt zit. Wanneer we Pythonbestand met functies én met top-level code hebben, dan zullen we de top-level code laten voorafgaan door `if __name__ == '__main__':`. 

De variabele `__name__` bevat de naam van de actieve module. Als het script direct aangeroepen wordt (en niet vanuit een import), dan krijgt dia variabele de waarde `"__main__"`. Het bovenstaade statement betekent dus: voer deze code enkel uit wanneer dit bestand rechtstreeks aangeroepen wordt en voer dit niet uit bij een import. Je kan om die manier een script definiëren dat op zichzelf kan uitgevoerd worden, maar waarvan de functies ook bij een import gebruikt kunnen worden.

```python 
def greet(name):
    return f"Hello, {name}!"

def main():
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)

if __name__ == '__main__':
    main()
```

Als het script op zichzelf (stand-alone) uitgevoerd wordt, dan wordt de functie `main()` aangroepen, maar je kan ook in een ander script een import doen. `main()` wordt dan niet automatisch aangeroepen bij het uitvoeren van het import-statement, maar je kan de functie `greet()` en `main()` in dat andere script aangroepen op een moment dat je dat zelf wil.

---

# 10. Oefening schoenmaat

Schrijf een functie die een gegeven Europese schoenmaat omzet naar  voetlengte. Definieer ook de inverse functie, d.w.z. de functie die een  gegeven voetlengte omzet naar een schoenmaat. Deze inverse functie mag  enkel een geheel getal als schoenmaat retourneren! Gebruik de formule  die je vindt op de volgende wikipedia pagina: https://nl.wikipedia.org/wiki/Schoenmaat. Neem dan je eigen schoenmaat en bereken je voetlengte. Print het  resultaat uit. Als test pas je de inverse functie toe en check je of de  berekende voetlengte jouw schoenmaat retourneert. Print ook dat  resultaat uit.

---

# 11. Functies importeren

Schrijf twee functies en bewaar die in het bestand `btw_functies.py`. De eerste functie `korting(prijs, korting)` heeft een bedrag en een kortingspercentageals argument, en geeft het bedrag met korting terug. De tweede functie `bedrag_met_btw(prijs)` heeft een bedrag als argument en geeft hetbedrag met terug met 21% BTW.

Schrijf een script `btw_berekenen.py` waarin je een bedrag opvraagt, en het kortingspercentageopvraagt en het bedrag met korting en BTW toont. Importeer hiervoor de functies uit `btw_functies.py`.
