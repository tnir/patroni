#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Patroni documentation build configuration file, created by
# sphinx-quickstart on Mon Dec 19 16:54:09 2016.
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
import os

import sys

from sphinx.application import ENV_PICKLE_FILENAME

sys.path.insert(0, os.path.abspath('..'))

from patroni.version import __version__

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
module_dir = os.path.abspath(os.path.join(project_root, 'patroni'))
excludes = ['tests', 'setup.py', 'conf']

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    # 'sphinx.ext.viewcode',
    'sphinx_github_style',  # Generate "View on GitHub" for source code
    'sphinxcontrib.apidoc',  # For generating module docs from code
    'sphinx.ext.autodoc',  # For generating module docs from docstrings
    'sphinx.ext.napoleon',  # For Google and Numpy formatted docstrings
]
apidoc_module_dir = module_dir
apidoc_output_dir = 'modules'
apidoc_excluded_paths = excludes
apidoc_separate_modules = True

# Include autodoc for all members, including private ones and the ones that are missing a docstring.
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": True,
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
project = 'Patroni'
copyright = '2024 Compose, Zalando SE, Patroni Contributors'
author = 'Patroni Contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__[:__version__.rfind('.')]
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'sphinx_rtd_theme'
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Replace "source" links with "edit on GitHub" when using rtd theme
html_context = {
    'display_github': True,
    'github_user': 'patroni',
    'github_repo': 'patroni',
    'github_version': 'master',
    'conf_py_path': '/docs/',
}

# sphinx-github-style options, https://sphinx-github-style.readthedocs.io/en/latest/index.html

# The name of the top-level package.
top_level = "patroni"

# The blob to link to on GitHub - any of "head", "last_tag", or "{blob}"
# linkcode_blob = 'head'

# The link to your GitHub repository formatted as https://github.com/user/repo
# If not provided, will attempt to create the link from the html_context dict
# linkcode_url = f"https://github.com/{html_context['github_user']}/" \
#                f"{html_context['github_repo']}/{html_context['github_version']}"

# The text to use for the linkcode link
# linkcode_link_text: str = "View on GitHub"

# A linkcode_resolve() function to use for resolving the link target
# linkcode_resolve: types.FunctionType


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Patronidoc'


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

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Patroni.tex', 'Patroni Documentation',
     'Patroni Contributors', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'patroni', 'Patroni Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Patroni', 'Patroni Documentation',
     author, 'Patroni', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/', None)}


# Remove these pages from index, references, toc trees, etc.
# If the builder is not 'html' then add the API docs modules index to pages to be removed.
exclude_from_builder = {
    'latex': ['modules/'],
    'epub': ['modules/'],
}
# Internal holding list, anything added here will always be excluded
_docs_to_remove = []


def config_inited(app, config):
    """Run during Sphinx `config-inited` phase.

    rtd reuses the environment, and there is no way to customize this behavior.
    Thus we remove the saved env.
    """
    pickle_file = os.path.join(app.doctreedir, ENV_PICKLE_FILENAME)
    if on_rtd and os.path.exists(pickle_file):
        os.remove(pickle_file)


def builder_inited(app):
    """Run during Sphinx `builder-inited` phase.

    Set a config value to builder name and add module docs to `docs_to_remove`.
    """
    print(f'The builder is: {app.builder.name}')
    app.add_config_value('builder', app.builder.name, 'env')

    # Remove pages when builder matches any referenced in exclude_from_builder
    if exclude_from_builder.get(app.builder.name):
        _docs_to_remove.extend(exclude_from_builder[app.builder.name])


def _to_be_removed(doc):
    for remove in _docs_to_remove:
        if doc.startswith(remove):
            return True
    return False


def env_get_outdated(app, env, added, changed, removed):
    """Run during Sphinx `env-get-outdated` phase.

    Remove the items listed in `docs_to_remove` from known pages.
    """
    to_remove = set()
    if hasattr(env, 'found_docs'):
        for doc in env.found_docs:
            if _to_be_removed(doc):
                to_remove.add(doc)
    added.difference_update(to_remove)
    changed.difference_update(to_remove)
    removed.update(to_remove)
    if hasattr(env, 'project'):
        env.project.docnames.difference_update(to_remove)
    return []


def doctree_read(app, doctree):
    """Run during Sphinx `doctree-read` phase.

    Remove the items listed in `docs_to_remove` from the table of contents.
    """
    from sphinx import addnodes
    for toc_tree_node in doctree.traverse(addnodes.toctree):
        for e in toc_tree_node['entries']:
            if _to_be_removed(str(e[1])):
                toc_tree_node['entries'].remove(e)


def autodoc_skip(app, what, name, obj, would_skip, options):
    """Include autodoc of ``__init__`` methods, which are skipped by default."""
    if name == "__init__":
        return False
    return would_skip



# A possibility to have an own stylesheet, to add new rules or override existing ones
# For the latter case, the CSS specificity of the rules should be higher than the default ones
def setup(app):
    if hasattr(app, 'add_css_file'):
        app.add_css_file('custom.css')
    else:
        app.add_stylesheet('custom.css')

    # Run extra steps to remove module docs when running with a non-html builder
    app.connect('config-inited', config_inited)
    app.connect('builder-inited', builder_inited)
    app.connect('env-get-outdated', env_get_outdated)
    app.connect('doctree-read', doctree_read)
    app.connect("autodoc-skip-member", autodoc_skip)
