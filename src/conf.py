# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os
import sys
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))
from conf_thyglobal import *

html_title = "Thierry"
project = "Thy's Notes"
project_copyright = '2022, Thierry Humphrey'
author = 'Thierry Humphrey'

myst_substitutions = {
    'wordcount': '{sub-ref}`wordcount-words` words | {sub-ref}`wordcount-minutes` min read',
}

favicons = ['https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.2/svgs/regular/pen-to-square.svg']

html_theme_options |= {
    # "announcement"         : "My announcement!",
}

intersphinx_mapping_enabled = (
    'py3',
    'sphinx',
)
intersphinx_mapping = {k: v for k, v in intersphinx_mapping.items() if k in intersphinx_mapping_enabled}
