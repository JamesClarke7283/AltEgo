# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Include src folder in docs
import os
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, os.path.abspath('../../../src'))

# Dynamic project info import from pyproject.toml
root_dir = Path(__file__).parent.parent.parent.parent
pyproject_path = root_dir / "pyproject.toml"

with open(pyproject_path, "rb") as f:
    pyproject_data = tomllib.load(f)

project = pyproject_data["project"]["name"]
author = pyproject_data["project"]["authors"][0]["name"]
release = pyproject_data["project"]["version"]

copyright = f'2024, {author}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Customize footer
html_show_sphinx = False  # Optional: Removes the "Created using Sphinx" text
html_show_copyright = True  # Ensures the copyright notice is shown

html_theme_options = {
    'footer_text': 'This documentation is licensed under the <a href="https://www.gnu.org/licenses/fdl-1.3.html">GNU Free Documentation License v1.3 or later</a>.',
}

# -- License information -----------------------------------------------------
# Specify GNU FDL 1.3 or later license for the documentation
latex_elements = {
    'preamble': r'''
\usepackage{lmodern}
\usepackage[scaled=0.9]{inconsolata}
''',
    'maketitle': r'''
\begin{titlepage}
\begin{center}
\includegraphics[width=0.5\textwidth]{logo}
\par
\vspace{1cm}
{\Huge \textbf{''' + project + r'''}}
\par
\vspace{1cm}
{\Large Version ''' + release + r'''}
\par
\vspace{1cm}
{\Large ''' + author + r'''}
\par
\vspace{1cm}
{\Large \today}
\par
\vspace{2cm}
{\Large This documentation is licensed under the GNU Free Documentation License version 1.3 or any later version.}
\end{center}
\end{titlepage}
''',
}

# Add license information to HTML output
html_theme_options = {
    'extra_nav_links': {
        'License': 'https://www.gnu.org/licenses/fdl-1.3.html',
    }
}