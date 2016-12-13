# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from ploneconf.minisite.testing import PLONECONF_MINISITE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ploneconf.minisite is properly installed."""

    layer = PLONECONF_MINISITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneconf.minisite is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ploneconf.minisite'))

    def test_browserlayer(self):
        """Test that IPloneconfMinisiteLayer is registered."""
        from ploneconf.minisite.interfaces import (
            IPloneconfMinisiteLayer)
        from plone.browserlayer import utils
        self.assertIn(IPloneconfMinisiteLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONECONF_MINISITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ploneconf.minisite'])

    def test_product_uninstalled(self):
        """Test if ploneconf.minisite is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ploneconf.minisite'))

    def test_browserlayer_removed(self):
        """Test that IPloneconfMinisiteLayer is removed."""
        from ploneconf.minisite.interfaces import \
            IPloneconfMinisiteLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPloneconfMinisiteLayer, utils.registered_layers())
