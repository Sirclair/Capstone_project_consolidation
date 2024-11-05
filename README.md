# Project Overview
Political Site is a Django-based web application that allows users to view political candidates, vote for their preferred candidate, and see the voting results. This application ensures user authentication, allowing only registered users to vote.
## Setup Instructions
1. **Virtual Environment (venv):**
    - Create a virtual environment:
        ```bash
        python -m venv venv
        ```
    - Activate the virtual environment:
        ```bash
        source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
        ```
    - Install dependencies:
        ```bash
        pip install -r requirements.txt
        ```

2. **Docker:**
    - Build the Docker image:
        ```bash
        docker build -t myapp .
        ```
    - Run the Docker container:
        ```bash
        docker run -p 8000:8000 myapp
        ```

## Dependency Management
- Install dependencies using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

