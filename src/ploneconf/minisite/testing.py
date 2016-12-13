# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ploneconf.minisite


class PloneconfMinisiteLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ploneconf.minisite)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploneconf.minisite:default')


PLONECONF_MINISITE_FIXTURE = PloneconfMinisiteLayer()


PLONECONF_MINISITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONECONF_MINISITE_FIXTURE,),
    name='PloneconfMinisiteLayer:IntegrationTesting'
)


PLONECONF_MINISITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONECONF_MINISITE_FIXTURE,),
    name='PloneconfMinisiteLayer:FunctionalTesting'
)


PLONECONF_MINISITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONECONF_MINISITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PloneconfMinisiteLayer:AcceptanceTesting'
)
