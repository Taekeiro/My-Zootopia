import requests

API_KEY = '8+G0fuBSpOuzmS2yHx/FQQ==xjN3x9mzczt93YbP'  # Replace with your actual API key
API_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_animal_data(search_query):
    """Fetches animal data from API Ninjas based on a search query."""
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(f"{API_URL}?name={search_query}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return []


def load_template(template_path):
    """Loads the content of the HTML template file."""
    with open(template_path, 'r') as file:
        return file.read()


def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML list item."""
    name = animal_obj.get('name', 'N/A')
    first_location = animal_obj.get('locations', ['N/A'])[0]
    animal_type = animal_obj['characteristics'].get('type', None)
    diet = animal_obj['characteristics'].get('diet', 'N/A')
    scientific_name = animal_obj['taxonomy'].get('scientific_name', 'N/A')
    lifespan = animal_obj['characteristics'].get('lifespan', 'N/A')
    distinctive_feature = animal_obj['characteristics'].get('distinctive_feature', 'N/A')
    weight = animal_obj['characteristics'].get('weight', 'N/A')
    skin_type = animal_obj['characteristics'].get('skin_type', 'Unknown')

    output = f"<li class='cards__item'>\n"
    output += f"  <div class='card__title'>{name}</div>\n"
    output += f"  <p class='card__text'>\n"
    output += f"    <ul class='card__details'>\n"
    output += f"      <li class='card__detail'><strong>Scientific Name:</strong> {scientific_name}</li>\n"
    output += f"      <li class='card__detail'><strong>Location:</strong> {first_location}</li>\n"

    if animal_type:
        output += f"      <li class='card__detail'><strong>Type:</strong> {animal_type}</li>\n"

    output += f"      <li class='card__detail'><strong>Diet:</strong> {diet}</li>\n"
    output += f"      <li class='card__detail'><strong>Lifespan:</strong> {lifespan}</li>\n"
    output += f"      <li class='card__detail'><strong>Distinctive Feature:</strong> {distinctive_feature}</li>\n"
    output += f"      <li class='card__detail'><strong>Weight:</strong> {weight}</li>\n"
    output += f"      <li class='card__detail'><strong>Skin Type:</strong> {skin_type}</li>\n"
    output += f"    </ul>\n"
    output += f"  </p>\n"
    output += f"</li>\n"

    return output


def get_available_skin_types(animals_data):
    """Extracts all unique skin_type values from the animals data."""
    skin_types = set()
    for animal in animals_data:
        skin_type = animal['characteristics'].get('skin_type', 'Unknown')
        skin_types.add(skin_type)
    return list(skin_types)


def filter_animals_by_skin_type(animals_data, selected_skin_type):
    """Filters animals by the selected skin_type."""
    return [animal for animal in animals_data if
            animal['characteristics'].get('skin_type', 'Unknown') == selected_skin_type]


# Step 1: Prompt the user for an animal name
animal_name = input("Enter a name of an animal: ")

# Step 2: Fetch the animals data from the API based on user input
animals_data = fetch_animal_data(animal_name)

# Step 3: Check if any animals were returned, else display an error message in the HTML
if not animals_data:
    html_content = f"<h2>The animal '{animal_name}' doesn't exist.</h2>"
    with open('animals_output.html', 'w') as output_file:
        output_file.write(html_content)
    print("Website was successfully generated to the file animals_output.html.")
    exit()

# Step 4: Display available skin_type values to the user, handle cases with no skin types
available_skin_types = get_available_skin_types(animals_data)
if available_skin_types:
    print("Available Skin Types:")
    for idx, skin_type in enumerate(available_skin_types, 1):
        print(f"{idx}. {skin_type}")

    # Prompt the user to select a skin_type
    selected_index = int(input(f"Select a skin type (1-{len(available_skin_types)}): ")) - 1
    selected_skin_type = available_skin_types[selected_index]
    print(f"You selected: {selected_skin_type}")

    # Filter animals by the selected skin_type
    filtered_animals = filter_animals_by_skin_type(animals_data, selected_skin_type)
else:
    print("No skin types found for this animal search. Displaying all results.")
    filtered_animals = animals_data

# Step 5: Load the HTML template
html_template = load_template('animals_template.html')

# Step 6: Generate a string with the serialized animals' data
output = ''
for animal_obj in filtered_animals:
    output += serialize_animal(animal_obj)

# Step 7: Replace the placeholder in the template with the generated animals' data
html_content = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

# Step 8: Save the final HTML to a new file
with open('animals_output.html', 'w') as output_file:
    output_file.write(html_content)

print("Website was successfully generated to the file animals_output.html.")
