import sys, os

project = 'PyTox-ng'
module = 'PyTox'
copyright = '2023, Wei-Ning Huang and Jan Malakhovski'
version = '0.2.18'
release = version
description = 'Python bindings for https://github.com/TokTok/c-toxcore of https://tox.chat/'
url='https://github.com/oxij/PyTox-ng',

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.coverage']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']

rst_prolog = f"""
.. |project| replace:: {project}
.. _project: {url}
.. |description| replace:: {description}
"""

#pygments_style = 'sphinx'
#html_theme = 'pyramid'
#html_static_path = ['_static']
#htmlhelp_basename = 'PyToxdoc'

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', f'{module}.tex', f'{project} Documentation', 'Wei-Ning Huang', 'manual'),
]

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', module, f'{project} Documentation', ['Wei-Ning Huang'], 7)
]

# If true, show URL addresses after external links.
man_show_urls = True

# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author, dir menu entry, description, category)
texinfo_documents = [
    ('index', module, f'{project} Documentation', 'Wei-Ning Huang',
     module, description, 'Miscellaneous'),
]
