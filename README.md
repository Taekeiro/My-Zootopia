Animal Info Website Generator
This project generates a website displaying detailed information about animals based on user input. The website can be customized to show animals from different species and filter them by characteristics, such as skin type. Data is fetched dynamically from the API Ninjas Animals API and displayed in a well-organized HTML format.

Project Structure
The project is organized into two main parts:

Data Fetcher (data_fetcher.py):

Responsible for fetching animal data from an external API.
Retrieves information on animals based on the name input provided by the user.
Returns data in a structured format (a list of dictionaries), which is then used by the website generator.
The fetch_data function in this file abstracts data-fetching logic, making it easy to change the data source if needed in the future.
Website Generator (animals_web_generator.py):

Generates an HTML website based on the fetched data.
Prompts the user for an animal name, then uses the data_fetcher to retrieve information about that animal.
Filters the results by skin_type if available, allowing the user to view animals with specific characteristics.
Outputs a user-friendly HTML file, animals_output.html, displaying either the animal information or a message if the animal does not exist.
File Descriptions
data_fetcher.py: Contains the fetch_data function to interact with the API and retrieve data.
animals_web_generator.py: Manages user interaction, data filtering, and HTML generation based on data from data_fetcher.
animals_template.html: The HTML template used for the website structure, which dynamically inserts animal data into a placeholder.
animals_output.html: The final generated HTML file containing either the animal information or an error message if no data is found.
Getting Started
Prerequisites
Python 3.x
requests library (install with pip install requests)
API Key Setup
This project uses the API Ninjas Animals API. Sign up to get an API key, then place your key in data_fetcher.py under API_KEY.

Running the Project
Clone the repository and navigate to the project directory.

Run the animals_web_generator.py script:

bash
Копировать код
python3 animals_web_generator.py
Enter an animal name (e.g., "Fox") when prompted.

Choose a skin type from the list if available.

View the generated animals_output.html file in your browser.