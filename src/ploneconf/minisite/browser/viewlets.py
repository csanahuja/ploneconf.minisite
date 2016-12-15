from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.interfaces import ISiteRoot
from plone import api

class LogoViewlet(ViewletBase):

    def image(self, parent=None):

        chain = list(self.getAcquisitionChain(self.context))
        for item in chain:
            if (item.portal_type == 'minisite'):
                return item.absolute_url() + "/@@images/logo"
        return None


    def getAcquisitionChain(self, object):

        inner = object.aq_inner

        iter = inner

        while iter is not None:
            yield iter

            if ISiteRoot.providedBy(iter):
               break

            if not hasattr(iter, "aq_parent"):
                raise RuntimeError("Parent traversing interrupted by object: " + str(parent))

            iter = iter.aq_parent

