#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Flamewind'
SITENAME = "Flamewind's Library"
SITEURL = ''

PATH = 'content'
THEME = 'MinimalXY'

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = False

CACHE_CONTENT = False
WITH_FUTURE_DATES = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Keith Baker FAQ', 'http://keith-baker.com/category/gaming/eberron-faq/'),
         ('Wiki', 'https://en.wikipedia.org/wiki/Eberron'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# WARNING!
DELETE_OUTPUT_DIRECTORY = False

# Theme customizations - https://github.com/petrnohejl/MinimalXY/
MINIMALXY_START_YEAR = 2017
MINIMALXY_CURRENT_YEAR = date.today().year


# Author
AUTHOR_DESCRIPTION = 'The biggest library in Eberron'
AUTHOR_INTRO = "Flamewind's Library -" + AUTHOR_DESCRIPTION
AUTHOR_AVATAR = 'https://t00.deviantart.net/Qraeu2_jTg-RpAOa-8vUaRYXxpQ=/fit-in/150x150/filters:no_upscale():origin()/pre00/c150/th/pre/f/2011/285/a/7/black_photoshop_feather_by_fuckinsick-d4clfcb.png'
AUTHOR_WEB = '/'

# Social
SOCIAL = ()

# Menu
MENUITEMS = (
    ('Categories', '/categories'),
)
