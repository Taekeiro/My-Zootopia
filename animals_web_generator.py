import json


def load_data(file_path):
    """Loads the content of a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def load_template(template_path):
    with open(template_path, 'r') as file:
        return file.read()

# Load the animals data
animals_data = load_data('animals_data.json')
html_template = load_template('animals_template.html')

# Iterate through each animal and print the required information
output = ''
for animal in animals_data:
    name = animal.get('name', 'N/A')
    diet = animal['characteristics'].get('diet', 'N/A')
    first_location = animal.get('locations', ['N/A'])[0]  # Get first location
    animal_type = animal['characteristics'].get('type', None)

    output += f"<li class='cards__item'>\n"
    output += f"  <div class='card__title'>{name}</div>\n"
    output += f"  <p class='card__text'>\n"
    output += f"      <strong>Location:</strong> {first_location}<br/>\n"

    if animal_type:  # Only include 'Type' if it exists
        output += f"      <strong>Type:</strong> {animal_type}<br/>\n"

    output += f"      <strong>Diet:</strong> {diet}<br/>\n"
    output += f"  </p>\n"
    output += f"</li>\n"

html_content = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

with open('animals_output.html', 'w') as output_file:
    output_file.write(html_content)

print("HTML file generated successfully.")