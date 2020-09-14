# encoding: utf-8
"""
Dylan

A domain package for Sphinx.

Created by Dustin Voss on 2011-11-10.
Copyright (c) 2011-2016 Open Dylan Maintainers. All rights reserved.
"""

from .dylandomain import DylanDomain

# This setup function is called because we register dylan.domain as an
# extension in the conf.py file.
def setup (app):
    # app is described here:
    # https://www.sphinx-doc.org/en/3.x/extdev/appapi.html#sphinx.application.Sphinx
    app.add_config_value('dylan_drm_url', 'https://opendylan.org/books/drm/', 'html')
    app.add_domain(DylanDomain)
