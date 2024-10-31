import requests
import dotenv

API_KEY = dotenv.get_key('.env', 'API_KEY')
API_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches the animal data for the animal 'animal_name'.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        list: A list of animal dictionaries, each containing animal details.
    """
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(f"{API_URL}?name={animal_name}", headers=headers)

    if response.status_code == 200:
        return response.json()  # Returns a list of animals
    else:
        print(f"Error fetching data: {response.status_code}")
        return []
