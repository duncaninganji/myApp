from django.conf.urls import url
from .views import AppletView
urlpatterns = [
                  url(r'^30de0af2b3e62c4d6b3e2a09a1e39e73bfa2977da91e1682df/?$', AppletView.as_view())
               ]