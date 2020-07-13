# -*- coding: utf-8 -*-
from edi.securegistration.testing import EDI_SECUREGISTRATION_FUNCTIONAL_TESTING
from edi.securegistration.testing import EDI_SECUREGISTRATION_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = EDI_SECUREGISTRATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_validationview_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='validationview'
        )
        self.assertTrue(view.__name__ == 'validationview')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in validationview'
        # )

    def test_validationview_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='validationview'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = EDI_SECUREGISTRATION_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
