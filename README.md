# IPL-data-API

This project provides an API for accessing detailed information about cricket matches from the Indian Premier League (IPL). It includes data on matches from various years, detailing outcomes, scores, venues, and more, and is built using Streamlit.

## Project Structure

The project is structured as follows:

- `__pycache__/`: Compiled Python files.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `app.py`: The main Python file that runs the Streamlit application.
- `overall.py`: Contains overall data processing or utility functions.
- `player.py`: Handles player-specific data processing or utility functions.
- `README.md`: This file, providing project documentation.
- `static/`: Contains static files like CSVs.
    - `balls.csv`: Data about individual ball deliveries.
    - `matches.csv`: Detailed match data across various seasons.

## Setup and Installation

To set up this project locally, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory and install the required dependencies:

```sh
pip install -r requirements.txt