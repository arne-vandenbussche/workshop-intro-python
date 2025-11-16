# 📊 Python Project: Gegevensanalyse met Pandas — Leerlingenhand-out

## 🧪 Mini-project: Analyseer een dataset in Python

In dit project leer je hoe je **echte data** kan inlezen, bekijken en analyseren met behulp van **Pandas**, een krachtige Python-bibliotheek voor gegevensanalyse.

Je leert:
- een CSV-bestand inladen  
- data bekijken en filteren  
- kolommen toevoegen  
- sorteren en groeperen  
- kleine analyses uitvoeren  

Dit project is ideaal als eerste kennismaking met data science.

---

# 📌 1. Wat heb je nodig?

- Python 3  
- Pandas (`pip install pandas`)  
- Een CSV-bestand (je krijgt een voorbeeldbestand)

Voorbeeldbestand: **students.csv**

```
name,age,school,math,science,english
Emma,17,North High,78,69,88
Liam,18,West High,92,81,75
Noah,17,North High,55,72,60
Olivia,16,East High,89,94,91
Ava,17,West High,61,58,70
```

---

# 📌 2. Startcode (skeleton)

Gebruik deze startcode als basis:

```python
import pandas as pd

# 1. Lees de dataset in
df = pd.read_csv("students.csv")

# 2. Bekijk de eerste rijen
print(df.head())

# 3. Toon info over de kolommen
print(df.info())

# 4. Analyse: gemiddelde scores
print(df[["math", "science", "english"]].mean())
```

---

# 📌 3. Jouw opdracht

Je voert analyses uit op de dataset `students.csv`. Je vindt deze in de map gegevensanalyse.

Je kan deze documentatie raadplagen ()[https://python.arnevandenbussche.be/Nederlands/h10-pandas/]

### ✔️ Opdracht A — Basisverkenning
1. Toon de eerste 10 rijen  
2. Toon de namen van alle kolommen  
3. Hoeveel rijen zijn er in totaal?

---

### ✔️ Opdracht B — Filteren
Maak een subset van:
- alle leerlingen ouder dan 17  
- alle leerlingen met een score > 80 voor wiskunde  
- alle leerlingen van *West High*

---

### ✔️ Opdracht C — Nieuwe kolom toevoegen
Voeg een nieuwe kolom `average` toe:

```python
df["average"] = df[["math", "science", "english"]].mean(axis=1)
```

Toon daarna:
- de 5 leerlingen met de hoogste gemiddelde score  
- alle leerlingen met gemiddelde < 60  

---

### ✔️ Opdracht D — Sorteren
Sorteer de dataset:
1. op leeftijd  
2. op gemiddelde score (hoog → laag)

---

### ✔️ Opdracht E — Groeperen
Groeperen op school:

```python
df.groupby("school")["average"].mean()
```

Beantwoord:
- Welke school heeft het hoogste gemiddelde?  
- Welke het laagste?

---

# 📌 4. Uitbreidingsopdrachten (optioneel)

### 🔹 1. Visualisatie
Maak een staafdiagram van het gemiddelde van elke school. *(Hiervoor gebruik je matplotlib)*

### 🔹 2. Beste vak
Voeg voor elke leerling een kolom toe `best_subject` met hun beste vak.

### 🔹 3. Ranking
Maak een kolom `rank` die de leerlingen rangschikt van beste naar slechtste gemiddelde.

### 🔹 4. Export
Bewaar de nieuwe dataset in een CSV-bestand:

```python
df.to_csv("students_updated.csv", index=False)
```

---

# 📌 5. Tips & strategie

✔️ Werk stap voor stap  
✔️ Print tussentijdse resultaten  
✔️ Gebruik `df.head()` om snel te controleren  
✔️ Houd je code logisch en overzichtelijk  

---

# 🎉 Veel succes!
Met deze oefening zet je je eerste stappen richting **data science**.  
Experimenteer gerust en probeer extra analyses uit!
