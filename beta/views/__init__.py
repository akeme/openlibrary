#!/usr/bin/env python
#-*-coding: utf-8 -*-

"""
    __init__.py
    ~~~~~~~~~~~

    :copyright: (c) 2017 by Internet Archive
    :license: see LICENSE for more details.
"""

from flask import render_template
from flask.views import MethodView

class Base(MethodView):
    def get(self, uri=None):
        template = uri or "home"
        return render_template('base.html', template=template)

class WorkEdition(MethodView):
    def get(self, id=None):
        return render_template('base.html',
                               template='book')

class Partial(MethodView):
    def get(self, partial):
        return render_template('partials/%s.html' % partial)
