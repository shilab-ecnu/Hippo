# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mouse Hippocampus Analysis'
copyright = '2024, Yang Wanshuo'
author = 'Yang Wanshuo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = extensions = ['recommonmark','sphinx_markdown_tables', 'nbsphinx'] 

templates_path = ['_templates']
html_static_path = ['_static']
exclude_patterns = []

language = 'zh-CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = []
