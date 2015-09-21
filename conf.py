# -*- coding: utf-8 -*-
#
# sphinx-quickstart on Fri Nov 28 22:10:09 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import subprocess

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.append(os.path.abspath('sphinxext'))

# Try to override the matplotlib configuration as early as possible
try:
    import gen_rst
except:
    pass


# General configuration
# ---------------------

needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
        'gen_rst',
        'sphinx.ext.autodoc',
        'sphinx.ext.doctest',
        #'matplotlib.sphinxext.plot_directive',
        'plot_directive',
        'only_directives',
        'ipython_console_highlighting',
        #'matplotlib.sphinxext.only_directives',
        'sphinx.ext.pngmath',
        'sphinx.ext.intersphinx',
        'sphinx.ext.extlinks',
]

doctest_test_doctest_blocks = 'true'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u"Scipy lecture notes"
copyright = u'2012,2013'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The short X.Y version.
# we get this from git
# this WILL break if we are not in a git-repository
p = subprocess.Popen(['git', 'describe', '--tags'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
p.wait()
version = p.stdout.read().strip()

# The full version, including alpha/beta/rc tags.
release = '2013.2 beta (euroscipy 2013)'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'
today_fmt = '%B %d, %Y'
if version:
    today_fmt += ' ({%s})' % version

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['intro/image_processing']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Monkey-patch sphinx to set the lineseparator option of pygment, to
# have indented line wrapping
from pygments import formatters

class MyHtmlFormatter(formatters.HtmlFormatter):
    def __init__(self, **options):
        options['lineseparator'] = '\n<div class="newline"></div>'
        formatters.HtmlFormatter.__init__(self, **options)

from sphinx import highlighting
highlighting.PygmentsBridge.html_formatter = MyHtmlFormatter

# Our substitutions
rst_epilog = """

.. |clear-floats| raw:: html

    <div style="clear: both"></div>

.. always clear floats at the bottom to avoid having stick out in the footer

|clear-floats|

"""

# Options for HTML output
# -----------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'scipy_lectures'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['themes']

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
#html_style = 'default.css'

html_theme_options = {
                'nosidebar': 'true',
                'footerbgcolor': '#000000',
                'relbarbgcolor': '#000000',
                }


# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Scipy lecture notes"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = "Scipy"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['themes/scipy_lectures/static', "_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'PythonScientic'

# Options for epub output
# ------------------------

epub_theme = 'epub'
epub_theme_options = {'relbar1': False, 'footer': False}

# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Latex references with page numbers (only Sphinx 1.0)
latex_show_pagerefs = True

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index', 'PythonScientific.tex', ur'Python Scientific lecture notes',
   ur"""EuroScipy tutorial team \\\relax\normalfont Editors: Valentin Haenel, Emmanuelle Gouillart, Gaël Varoquaux"""
   + r"\\\relax ~\\\relax http://scipy-lectures.github.com",
   'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'euroscipy_back.pdf'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_use_modindex = False


# Additional stuff for the LaTeX preamble.
latex_preamble = """
\definecolor{VerbatimColor}{rgb}{0.95,1,0.833}
\definecolor{VerbatimBorderColor}{rgb}{0.6,0.6,0.6}
\setcounter{tocdepth}{1}
\usepackage{amssymb}
\usepackage{pifont}
\DeclareUnicodeCharacter{2460}{\ding{182}}
\DeclareUnicodeCharacter{2461}{\ding{183}}
\DeclareUnicodeCharacter{2462}{\ding{184}}
\DeclareUnicodeCharacter{2794}{\ding{229}}
"""

latex_elements = {
    'classoptions': ',oneside,openany',
    'babel': '\usepackage[english]{babel}',
    #'tableofcontents': '\\pagestyle{normal}\\pagenumbering{arabic} %\\tableofcontents',
}

_python_doc_base = 'http://docs.python.org/2.7'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    _python_doc_base: None,
    'http://docs.scipy.org/doc/numpy': None,
    'http://docs.scipy.org/doc/scipy/reference': None,
    'http://matplotlib.org/': None,
    'http://scikit-learn.org/stable': None,
    'http://scikit-image.org/docs/stable/': None,
    'http://docs.enthought.com/mayavi/mayavi/': None,
    'http://statsmodels.sourceforge.net/': None,
    'http://pandas.pydata.org/pandas-docs/stable/': None,
    'http://stanford.edu/~mwaskom/software/seaborn/': None,
}

extlinks = {
    'simple': (_python_doc_base + '/reference/simple_stmts.html#%s', ''),
    'compound': (_python_doc_base + '/reference/compound_stmts.html#%s', ''),
}

# -- Options for pngmath ------------------------------------------------

pngmath_dvipng_args = ['-gamma 1.5', '-D 180', '-bg', 'Transparent']
pngmath_use_preview = True



# Add the 'copybutton' javascript, to hide/show the prompt in code
# examples
def setup(app):
    app.add_javascript('copybutton.js')
