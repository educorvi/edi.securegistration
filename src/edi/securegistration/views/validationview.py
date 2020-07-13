# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView

import datetime
import random

class Validationview(BrowserView):
    def __call__(self):
        template = '''<li class="heading" i18n:translate="">
          Sample View
        </li>'''
        return template

    def validatesolution(usersolution):
        usersolution = int(usersolution)
        now = datetime.datetime.now()
        hour = now.strftime("%H")

        if usersolution == (int(hour) + (2 * int(hour))):
            validationresult = 1
        elif usersolution == (int(hour) + (3 * int(hour))):
            validationresult = 0

        return validationresult
