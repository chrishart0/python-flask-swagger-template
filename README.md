markdown
Copy code
# User REST API

A simple REST API for managing User objects, built with Flask and Flask-RESTPlus for Swagger integration.

## Setup Instructions

Follow these steps to get the project up and running on your local machine:

1. **Install Python:** This application requires Python 3.9 or later. Download it from the [official Python website](https://www.python.org/downloads/) if you don't have it installed already.

2. **Clone the Repository:** Clone this repository to a location of your choice on your local machine.

3. **Create a Virtual Environment:** Navigate to the project root directory (the same one that contains `requirements.txt`) and create a Python virtual environment. This is done to avoid package dependency issues. To create a virtual environment named 'venv', use the following command:

python3 -m venv venv

mathematica
Copy code

4. **Activate the Virtual Environment:** Before installing the project dependencies, you need to activate the virtual environment. This will ensure that the packages are installed in the virtual environment, rather than your global Python environment.

On Windows:

.\venv\Scripts\activate

graphql
Copy code

On Unix or MacOS:

source venv/bin/activate

markdown
Copy code

5. **Install Project Dependencies:** Install the project dependencies by running the following command:

pip install -r requirements.txt

vbnet
Copy code

6. **Run the Application:** You're now ready to run the application! You can do so with the following command:

python app.py

arduino
Copy code

Now, you should be able to see the API running at `http://localhost:5000/`.
Ensure that you replace app.py with the actual name of your main python script.