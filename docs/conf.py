import os
import sys
import django

# Add the project root to the system path
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../political_site'))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'political_site.settings'

# Setup Django
django.setup()

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'political site'
copyright = '2024, bright'
author = 'bright'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
