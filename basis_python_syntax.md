# 🐍 Basis Python-syntax — Hand-out

### Voor leerlingen (inleidende workshop Python)

---

## 🎯 Doelen
Na dit hoofdstuk kan je:
- variabelen gebruiken zonder types te moeten declareren  
- input lezen en resultaten tonen  
- strings combineren met f-strings  
- lists gebruiken om data te bewaren  
- if/elif/else gebruiken  
- loops schrijven (for/while)

---

# 1. Variabelen en types

Python gebruikt **dynamische types**. Je moet dus geen `int`, `string`, … schrijven.

```python
age = 17
name = "Emma"
pi = 3.14
is_student = True
```

Geen puntkomma nodig.

---

# 2. Strings & f-strings

```python
name = "Liam"
print("Hello " + name)
print(f"Hello {name}, welcome to Python!")
```

**f-strings** zijn de handigste manier om tekst en variabelen te combineren.

---

# 3. Input & print

`input()` leest altijd een **string**.  
Soms moet je omzetten naar `int`.

```python
name = input("What's your name? ")
age = int(input("How old are you? "))

print(f"Hi {name}, you are {age} years old.")
```

---

# 4. Lists

Een list is vergelijkbaar met een `List<>` in C#.

```python
numbers = [4, 7, 12, 9]

print(numbers[0])     # eerste element
numbers.append(20)    # element toevoegen
print(numbers)
```

Handige functies:

```python
len(numbers)
sum(numbers)
max(numbers)
min(numbers)
```

---

# 5. Conditions (if / elif / else)

Belangrijk: **inspringing (4 spaties)** bepaalt de codeblokken.

```python
age = int(input("Age? "))

if age < 12:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

---

# 6. Loops

### For-loop over een lijst
```python
fruits = ["apple", "banana", "pear"]

for f in fruits:
    print(f)
```

### For-loop met range()
```python
for i in range(1, 6):  # 1 t.e.m. 5
    print(i)
```

### While-loop
```python
n = 5
while n > 0:
    print(n)
    n -= 1
```

---

# 7. Oefeningen (korte opdrachten)

### Oefening 1  
Vraag de naam van de gebruiker en toon een zin met een f-string.

### Oefening 2  
Maak een lijst met 5 getallen.  
Print:
- grootste  
- kleinste  
- som  
- gemiddelde  

### Oefening 3  
Vraag één getal.  
Print `"even"` of `"odd"`.

### Oefening 4  
Print alle getallen van 1 t.e.m. 20.  
Extra: print alleen even getallen.

---

# 8. Grote Jan

Schrijf een kort script dat het volgende doet:

- Je vraagt de naam van iemand.
- Je vraagt de lengte van iemand in cm.
- Als die persoon groter is dan 180 cm, dan antwoord je "Dag <naam>, wat ben je groot!".
- Als hij/zij 160cm of groter is, maar kleiner dan of gelijk aan 180 cm, dan antwoord jé gewoon: "Dag <naam>".
- Als die persoon kleiner is dan 160 cm, dan antwoord je: "Dag <naam>, je bent ook niet van de grootste."

# 9. Oefening op lijsten

Schrijf een programma dat:

1. de gebruiker 3 getallen laat ingeven  
2. ze bewaart in een list  
3. grootste, kleinste en gemiddelde print  
4. als het gemiddelde > 10 is → `"That's a big average!"`  
   anders → `"That's a small average."`

---

# 10. Nog een oefening op lijsten

Maak een lijst van willekeurige getallen. 

Ga door de lijst en druk de even getallen af.




