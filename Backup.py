import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)



"""
Aufgabe
Schreibe ein einfaches Python-Skript, das den Inhalt von animals_data.json liest, 
durch die Tiere iteriert und für jedes folgende Informationen ausgibt:

Name
Ernährung
Den ersten Ort aus der Liste locations
Typ

Wenn eines dieser Felder nicht vorhanden ist, soll es nicht ausgegeben werden.

BEISPIEL
Name: American Foxhound
Diet: Omnivore
Location: North-America
Type: Hound

Name: Arctic Fox
Diet: Carnivore
Location: Eurasia
Type: Mammal

Name: Cross Fox
Diet: Carnivore
Location: North-America
Type: mammal


"""
def show_animal_information(animals_data):
    """ Shows information about animals """
    for i in range(len(animals_data)):
        # Name zuordnen und ausgeben
        name = animals_data[i].get('name')
        if name:
            print(f"Name: {name}")

        # Sind Characteristics vorhanden? Dann Diet zuordnen und ausgeben
        characteristics = animals_data[i].get('characteristics')
        if characteristics:
            diet = characteristics.get('diet')
            if diet:
                print(f"Diet: {diet}")

        # Sind Locations vorhanden und die Liste nicht None UND nicht eine leere Liste []?
        # Dann ersten Ort aus Locations zuordnen und ausgeben
        locations = animals_data[i].get('locations')
        if locations:
            erster_ort = locations[0]
            print(f"Location: {erster_ort}")

        # Sind Characteristics vorhanden? Dann Type zuordnen und ausgeben
        if characteristics:
            type = characteristics.get('type')
            if type:
                print(f"Type: {type}")

        print()


    #    MEINE TESTS - DIE MÜSSEN NOCH ENTFERNT WERDEN

    print("\n=====================\n")
    print(len(animals_data))
"""
    print(f"Animals_data:\n{animals_data[0]}")
    print()
    characteristics = animals_data[0].get("characteristics")
    print(f"Characteristics: \n{characteristics}")
"""


def main():
    animals_data = load_data('animals_data.json')
    show_animal_information(animals_data)



if __name__ == '__main__':
    main()