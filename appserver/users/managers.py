from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from actstream.managers import ActionManager, stream

#This_DjangoActstream_file

# Generic Django-Activity-Stream Config Code
class MyActionManager(ActionManager):
    @stream
    def mystream(self, obj, verb='posted', time=None):
        if time is None:
            time = datetime.now()
        return obj.actor_actions.filter(verb=verb, timestamp__lte=time)
