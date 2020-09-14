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
    app.add_crossref_type(
        directivename = 'dylan_http',
        rolename = 'func',
    )
    app.add_config_value(
        name = 'dylan_drm_url',
        default = 'https://opendylan.org/books/drm/',
        rebuild = 'html',
    )
    app.add_domain(DylanDomain)
