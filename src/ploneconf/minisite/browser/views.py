from Products.Five.browser import BrowserView
from plone import api

class LogoView(BrowserView):

    def image(self):
        brains = api.content.find(self.context, portal_type='minisite')           
        for brain in brains:
            return brain.getURL() + "/@@images/logo"
