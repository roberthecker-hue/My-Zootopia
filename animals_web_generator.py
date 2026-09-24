import json

from bs4 import BeautifulSoup


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_information(animals_data):
    """ Shows information about animals (animals_data) from JSON file """
    output = '' # leeren String für Ausgabe erstellen
    for i in range(len(animals_data)):
        output += '<li class="cards__item">'
        # Name zuordnen und ausgeben
        name = animals_data[i].get('name')
        if name:
            output += f"Name: {name}<br/>\n"

        # Sind Characteristics vorhanden? Dann Diet zuordnen und ausgeben
        characteristics = animals_data[i].get('characteristics')
        if characteristics:
            diet = characteristics.get('diet')
            if diet:
                output += f"Diet: {diet}<br/>\n"

        # Sind Locations vorhanden und die Liste nicht None UND nicht eine leere Liste []?
        # Dann ersten Ort aus Locations zuordnen und ausgeben
        locations = animals_data[i].get('locations')
        if locations:
            erster_ort = locations[0]
            output += f"Location: {erster_ort}<br/>\n"

        # Sind Characteristics vorhanden? Dann Type zuordnen und ausgeben
        if characteristics:
            type = characteristics.get('type')
            if type:
                output += f"Type: {type}<br/>\n"

        output += "\n"
        output += '</li>'

    return output


def load_html(file_path):
    """ Loads a HTML file """
    with open(file_path, "r") as fileobj:
        html_data = fileobj.read()
    return html_data


def replace_htmtl_template_with_animal_information(html_template, animal_information):
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_information)
    return new_html


def write_new_html(file_path, new_html):
    with open(file_path, "w") as fileobj:
        fileobj.write(new_html)


def main():
    animals_data = load_data('animals_data.json')
    animal_information = get_animal_information(animals_data)
    html_template = load_html('animals_template.html')
    new_html = replace_htmtl_template_with_animal_information(html_template, animal_information)
    write_new_html('animals.html', new_html)


if __name__ == '__main__':
    main()

"""
**********************************************************************************
Schritt 3 - Das Design anpassen
**********************************************************************************

So geht’s
Du solltest deinen bisherigen Code von:

        output = ''  # define an empty string
        for animal_data in data:
            # append information to each string
            output += f"Name: {animal_data['name']}\n"
            output += f"Diet: {animal_data['characteristics']['diet']}\n"
            ...
        print(output)

ändern zu:

        output = ''  # define an empty string
        for animal_data in data:
            # append information to each string
            output += '<li class="cards__item">'
            output += f"Name: {animal_data['name']}<br/>\n"
            output += f"Diet: {animal_data['characteristics']['diet']}<br/>\n"
            ...
            output += '</li>'
        print(output)
"""