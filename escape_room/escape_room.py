import textwrap

def wrap(text):
    """Netjes afbreken van tekst in de terminal."""
    print(textwrap.fill(text, width=70))

def show_help():
    wrap("Mogelijke commando's: north, south, east, west, look, "
         "take <item>, inventory, help, quit, use key.")

def look(state):
    """Toon beschrijving van de huidige kamer."""
    print("De functie 'look' moet nog uitgewerkt worden")
    pass

def move(state, direction):
    """Verplaats de speler als er een uitgang in die richting is."""
    print("Die functie 'move' moet nog uitgewerkt worden.")
    pass

def take_item(state, item_name):
    """Neem een item uit de huidige kamer op."""
    print("De functie 'take_item' is nog niet geprogrammeerd.")
    pass

def show_inventory(state):
    """Toon wat de speler bij zich heeft."""
    print("Je kan je voorraad nog niet bekijken. We moeten die functie nog programmeren.")
    pass

def check_win_condition(state):
    """Controleer of de speler al ontsnapt is."""
    pass 

def use_key_on_door(state):
    """Gebruik de sleutel (als je die hebt) op de deur."""
    pass

def create_game_state():
    """Maak de kamers en het start-state van het spel aan."""
    rooms = {
        "cell": {
            "description": "Je wordt wakker in een kleine, donkere kamer. "
                           "Er is een bed, een houten kast en een deur naar het noorden.",
            "items": ["Nota"],
            "exits": {"north": "hallway"}
        },
        "hallway": {
            "description": "Je staat in een smalle gang. Naar het zuiden is je cel, "
                           "naar het oosten zie je een magazijn, en naar het noorden "
                           "een zware deur.",
            "items": [],
            "exits": {"south": "cell", "east": "storage", "north": "door"}
        },
        "storage": {
            "description": "Een kleine opslagruimte met dozen en planken. "
                           "Er ligt iets te glimmen in de hoek.",
            "items": ["Sleutel"],
            "exits": {"west": "hallway"}
        },
        "door": {
            "description": "Je staat voor een zware metalen deur. Hij lijkt op slot. "
                           "Misschien kan je hier een sleutel gebruiken.",
            "items": [],
            "exits": {"south": "hallway"}
        }
    }

    state = {
        "rooms": rooms,
        "location": "cell",   # start in de cel
        "inventory": [],
        "escaped": False
    }
    return state

def main():
    state = create_game_state()
    wrap("Welkom bij 'Escape the Room'!")
    wrap("Je doel: ontsnap uit het gebouw. Typ 'help' voor hulp.\n")
    look(state)

    while True:
        if check_win_condition(state):
            wrap("Je loopt door de open deur en ademt de frisse buitenlucht in. "
                 "Je bent ontsnapt! Proficiat!")
            break

        command = input("> ").strip().lower()

        if not command:
            continue

        if command in ("quit", "exit"):
            wrap("Je geeft op. Het spel is afgelopen.")
            break
        elif command == "help":
            show_help()
        elif command in ("look", "l"):
            look(state)
        elif command in ("inventory", "inv", "i"):
            show_inventory(state)
        elif command in ("north", "south", "east", "west"):
            move(state, command)
        elif command.startswith("take "):
            _, item_name = command.split(" ", 1)
            take_item(state, item_name)
        elif command in ("use key", "use sleutel"):
            use_key_on_door(state)
        elif command.startswith("use "):
            wrap("Je weet niet goed hoe je dat moet gebruiken.")
        elif command in ("read note", "read nota", "lees nota"):
            if "Nota" in state["inventory"]:
                wrap("Op de nota staat: 'De sleutel ligt waar het stof het dikst is.'")
            else:
                wrap("Je hebt geen nota bij je.")
        else:
            wrap("Onbekend commando. Typ 'help' voor een overzicht.")

if __name__ == "__main__":
    main()