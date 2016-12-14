from plone.app.layout.viewlets.common import ViewletBase
from plone import api

class LogoViewlet(ViewletBase):

    def image(self):
        brains = api.content.find(self.context, portal_type='minisite')  
        for brain in brains:      
            return brain.getURL() + "/@@images/logo"
