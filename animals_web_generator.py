import json


def load_data(file_path):
    """Loads the content of a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

# Load the animals data
animals_data = load_data('animals_data.json')

# Iterate through each animal and print the required information
for animal in animals_data:
    name = animal.get('name', 'N/A')
    diet = animal['characteristics'].get('diet', 'N/A')
    first_location = animal.get('locations', ['N/A'])[0]  # Get first location
    animal_type = animal['characteristics'].get('type', None)

    print(f"Name: {name}")
    print(f"Diet: {diet}")
    print(f"First Location: {first_location}")
    if animal_type:
        print(f"Type: {animal_type}")
    print("-" * 30)
