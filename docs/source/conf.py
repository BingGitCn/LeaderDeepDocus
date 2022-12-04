# Configuration file for the Sphinx documentation builder.
import os
import recommonmark

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# -- Project information

project = 'LeaderDeep'
copyright = '2022, Leader'
author = 'Bing'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'recommonmark',
    'sphinx_markdown_tables',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
source_suffix = ['.rst', '.md']
master_doc = 'index'
language = 'zh_CN'

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_logo = 'logoHome.png'

# -- Options for EPUB output
epub_show_urls = 'footnote'
