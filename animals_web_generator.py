import json


def load_data(file_path):
    """Loads the content of a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def load_template(template_path):
    """Loads the content of the HTML template file."""
    with open(template_path, 'r') as file:
        return file.read()


def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML list item."""
    output = ''
    name = animal_obj.get('name', 'N/A')
    first_location = animal_obj.get('locations', ['N/A'])[0]
    animal_type = animal_obj['characteristics'].get('type', None)
    diet = animal_obj['characteristics'].get('diet', 'N/A')
    scientific_name = animal_obj['taxonomy'].get('scientific_name', 'N/A')
    lifespan = animal_obj['characteristics'].get('lifespan', 'N/A')
    distinctive_feature = animal_obj['characteristics'].get('distinctive_feature', None)
    weight = animal_obj['characteristics'].get('weight', None)

    output = f"<li class='cards__item'>\n"
    output += f"  <div class='card__title'>{name}</div>\n"
    output += f"  <p class='card__text'>\n"
    output += f"    <ul class='card__details'>\n"
    output += f"      <li class='card__detail'><strong>Scientific Name:</strong> {scientific_name}</li>\n"
    output += f"      <li class='card__detail'><strong>Location:</strong> {first_location}</li>\n"

    if animal_type:
        output += f"  <li class='card__detail'><strong>Type:</strong> {animal_type}</li>\n"

    output += f"      <li class='card__detail'><strong>Diet:</strong> {diet}</li>\n"
    output += f"      <li class='card__detail'><strong>Lifespan:</strong> {lifespan}</li>\n"
    if distinctive_feature:
        output += f"  <li class='card__detail'><strong>Distinctive Feature:</strong> {distinctive_feature}</li>\n"
    if weight:
        output += f"  <li class='card__detail'><strong>Weight:</strong> {weight}</li>\n"
    output += f"    </ul>\n"
    output += f"  </p>\n"
    output += f"</li>\n"

    return output


# Step 1: Load the animals data and HTML template
animals_data = load_data('animals_data.json')
html_template = load_template('animals_template.html')

# Step 2: Generate a string with the serialized animals' data
output = ''
for animal_obj in animals_data:
    output += serialize_animal(animal_obj)

# Step 3: Replace the placeholder in the template with the generated animals' data
html_content = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

# Step 4: Save the final HTML to a new file
with open('animals_output.html', 'w') as output_file:
    output_file.write(html_content)

print("HTML file generated successfully.")
