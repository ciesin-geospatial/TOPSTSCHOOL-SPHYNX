"""\
TOPSTSCHOOL Sphinx (Documentation) Configuration
===============================================

Author: Akshay Mestry <xa@mes3.dev>
Created on: Sunday, October 27 2024
Last updated on: Friday, November 22 2024

This file contains the configuration settings for building the TOPSTSCHOOL
documentation using Sphinx, a popular Python documentation tool. Sphinx
is a powerful documentation generator that makes it easy to create high
quality technical documentation for technical projects.
"""

from __future__ import annotations

import subprocess
import typing as t
from datetime import datetime as dt

# -- General configurations ---------------------------------------------------
extensions: list[str] = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
]
exclude_patterns: list[str] = ["_build"]
templates_path: list[str] = ["_templates"]

# -- Miscellaneous ------------------------------------------------------------
nitpicky: bool = True
locale_dirs: list[str] = ["../locale/"]
gettext_compact: bool = False
intersphinx_mapping: dict[str, tuple[str, t.Any]] = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

rst_epilog = ""
with open("_static/urls.txt") as f:
    rst_epilog += f.read()

try:
    last_updated_cmd = (
        "git",
        "log",
        "--pretty=format:%cd",
        "--date=format:%B %d, %Y",
        "-n1",
    )
    last_updated = subprocess.check_output(last_updated_cmd).decode()
except Exception:
    last_updated = None

# -- Meta information ---------------------------------------------------------
project: t.Final[str] = "TOPSTSCHOOL"
author: t.Final[str] = "TOPSTSCHOOL Development Team"
author_email: t.Final[str] = "TOPSTSCHOOL@gmail.com"
baseurl: t.Final[str] = "https://ciesin-geospatial.github.io"
homepage: str = f"{baseurl}/TOPSTSCHOOL-SPHINX/"
source: t.Final[str] = (
    "https://github.com/ciesin-geospatial/TOPSTSCHOOL-SPHINX"
)

# -- Project information ------------------------------------------------------
html_coeus_author: t.Final[str] = author
html_coeus_copyright: t.Final[str] = f"{dt.now().year}, {html_coeus_author}."
html_coeus_email: t.Final[str] = author_email
html_coeus_github: str = source
html_coeus_license: str = f"{source}/blob/main/LICENSE"
html_coeus_repository: str = source
html_coeus_title: t.Final[str] = project
html_coeus_version: t.Final[str] = "2024.11.30"
html_coeus_favicon: t.Final[str] = "_static/img/favicon.png"
html_coeus_logo: t.Final[str] = "_static/img/logo.png"
html_coeus_hide_index_toctree: bool = True
html_coeus_homepage: str = homepage
html_coeus_documentation: str = html_coeus_homepage
html_coeus_socials: dict[str, str] = {
    "youtube": ["https://www.youtube.com/@TOPSTSCHOOL"]
}
html_coeus_theme_options: dict[str, t.Any] = {
    "last_updated": last_updated,
    "show_previous_next_pages": True,
    "supported_languages": {"en": "English"},
}

# -- Options for HTML output --------------------------------------------------
html_theme: t.Final[str] = "coeus_sphinx_theme"
html_static_path: list[str] = ["_static"]
html_context: dict[str, str] = {
    "feedback_link": source
    + "/discussions/new?category=thoughts-and-feedbacks"
}

# -- Options for Open Graph protocol ------------------------------------------
ogp_site_name: t.Final[str] = project
ogp_site_url: str = homepage
ogp_social_cards: dict[str, str] = {"site_url": homepage}
ogp_enable_meta_description: bool = True
