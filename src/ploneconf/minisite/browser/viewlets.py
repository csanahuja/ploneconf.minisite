from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.interfaces import ISiteRoot
from plone import api

class LogoViewlet(ViewletBase):

    def image(self, parent=None):
        return api.portal.get_navigation_root(self.context).absolute_url() + "/@@images/logo"

