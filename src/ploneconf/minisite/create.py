from plone.api.content import create
from plone.api.content import transition


def createContent(minisite, event):
    
    #Create a folder named News and publish it
    news = create(container=minisite, type='Folder', id='news', title='News', safe_id=True)
    transition(obj=news, transition='publish')

    #Create a folder named Events and publish it
    events = create(container=minisite, type='Folder', id='events', title='Events', safe_id=True)
    transition(obj=events, transition='publish')
