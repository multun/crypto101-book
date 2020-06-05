#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# camisole documentation build configuration file, created by
# sphinx-quickstart on Wed Jan 11 21:56:30 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sys
import pathlib
from sphinx.locale import _

root = pathlib.Path(__file__)
sys.path.insert(0, str(root.parent))
sys.path.insert(0, str(root.parent.parent))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinxcontrib.bibtex',
    'advanced_admonition',
]

extensions.append('sphinx.ext.imgmath')
imgmath_image_format = 'svg'
imgmath_font_size = 16

imgmath_latex_preamble = """
\\usepackage{microtype}
\\usepackage{setspace}
\\usepackage{csquotes}

\\usepackage{amsmath}
\\usepackage{amssymb}
\\newcommand{\\xor}{\\oplus}
\\newcommand{\\madd}{\\boxplus}

% Advanced command definitions
\\usepackage{xparse}

% Figures and subfigures
\\usepackage{float}
\\usepackage{rotating}
\\usepackage{subcaption}
\\usepackage{array}
\\usepackage{calc}
\\usepackage{framed}
\\usepackage{wrapfig}
\\usepackage{longtable}
\\newcolumntype{C}[1]{>{\\centering\\arraybackslash$}p{#1}<{$}}
\\usepackage[export]{adjustbox}
"""

# reference with :numref:`tag`, label with .. _tag:
numfig = True

# add page references to crossrefs
latex_show_pagerefs = True

mathjax_config = {
    'TeX': {
        'Macros': {
            "xor": "\\oplus",
        },
    },
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'crypto101'
copyright = '2020, Victor Collod, Victoria Krajcovicova'
author = 'Victor Collod, Victoria Krajcovicova'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
import subprocess
version = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode()
release = subprocess.check_output(["git", "describe"]).decode()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

locale_dirs = ['locale/']
gettext_compact = False

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
# https://alabaster.readthedocs.io/en/latest/customization.html#theme-options
html_theme_options = {
    "show_relbars": True,
    "fixed_sidebar": True,
    "github_user": "crypto101",
    "github_repo": "book",
    "github_button": True,
    "github_type": "star",
}

html_show_sourcelink = False

htmlhelp_basename = 'crypto101-fr-doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

advanced_admonition_text = str(_(
    "This is an optional, in-depth section. It almost certainly won't help you write better software, "
    "so feel free to skip it. It is only here to satisfy your inner geek's curiosity."
))
