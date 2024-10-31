"# Capstone_project_consolidation" 
# Political Site

## Project Overview
Political Site is a Django-based web application that allows users to view political candidates, vote for their preferred candidate, and see the voting results. This application ensures user authentication, allowing only registered users to vote.

## Features
- User authentication (sign up, log in)
- View list of political candidates
- Vote for a candidate
- View voting results

## Prerequisites
- Python 3.x
- Django 3.2
- Docker (if using Docker setup)

## Getting Started

### Using Virtual Environment (venv)
1. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

2. **Activate the virtual environment**:
    - On Windows:
      ```sh
      .\venv\Scripts\activate
      ```
    - On Linux/MacOS:
      ```sh
      source venv/bin/activate
      ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```sh
    python manage.py runserver
    ```

### Using Docker
1. **Build the Docker image**:
    ```sh
    docker build -t yourusername/political_site .
    ```

2. **Run the Docker container**:
    ```sh
    docker run -p 8000:8000 yourusername/political_site
    ```

## Usage
- **Home Page**: Displays a list of political candidates.
- **Candidate Details Page**: Shows detailed information about a specific candidate.
- **Vote**: Allows authenticated users to vote for a candidate.
- **Results**: Displays the vote count for each candidate.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or issues, please contact chimuka.b@yahoo.com.
