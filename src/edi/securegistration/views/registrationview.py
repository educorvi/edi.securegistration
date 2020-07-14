# -*- coding: utf-8 -*-

from edi.securegistration import _
from Products.Five.browser import BrowserView

import datetime
import random

now = datetime.datetime.now()
hour = now.strftime("%H")
singlenumber  = random.randint(2,4)

zahl1 = int(hour)
zahl2 = int(hour) * singlenumber

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Registrationview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('registrationview.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        self.captchastring = self.generate_captcha()
        self.actionurl = self.context.absolute_url() + '/validationview'
        return self.index()
        
    def generate_captcha(self):     
        now = datetime.datetime.now()
        hour = now.strftime("%H")
        singlenumber  = random.randint(2,4)

        zahl1 = int(hour)
        zahl2 = int(hour) * singlenumber

        captchastring = str(zahl1)+" + "+str(zahl2)
        return captchastring

