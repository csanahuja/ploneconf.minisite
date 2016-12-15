from plone import api
from plone.dexterity.browser.view import DefaultView

class MinisiteView(DefaultView):
    """ View for minisite """

    """ Get news in the folder minisite_id/news """
    def news(self):
        results = []

        news_path = self.context.absolute_url() + "/news"
        brains = api.content.find(self.context, depth=2,
                                  portal_type="News Item", review_state="published")
        for brain in brains:    
            results.append({
                'title': brain.Title,
                'description': brain.Description,
                'url': brain.getURL()
                })


        return results


