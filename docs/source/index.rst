.. political_site documentation master file, created by
   sphinx-quickstart on Thu Nov 24 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Political Site's documentation!
==========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Introduction
------------

Welcome to the documentation for Political Site, a Django-based web application for managing political candidates and voting.

Features
--------

- User authentication (sign up, log in)
- View list of political candidates
- Vote for a candidate
- View voting results

Installation
------------

Follow these steps to install and run the application:

Using Virtual Environment (venv)
1. Create a virtual environment:
   .. code-block:: bash

      python -m venv venv
2. Activate the virtual environment:
   .. code-block:: bash

      source venv/bin/activate  # On Linux/MacOS
      .\\venv\\Scripts\\activate  # On Windows
3. Install dependencies:
   .. code-block:: bash

      pip install -r requirements.txt
4. Run the application:
   .. code-block:: bash

      python manage.py runserver

Using Docker
1. Build the Docker image:
   .. code-block:: bash

      docker build -t yourusername/political_site .
2. Run the Docker container:
   .. code-block:: bash

      docker run -p 8000:8000 yourusername/political_site

Modules
-------

.. toctree::
   :maxdepth: 2
   :caption: Modules
