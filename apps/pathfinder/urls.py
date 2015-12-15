from django.conf.urls import url

from .views import PathfinderView


urlpatterns = [
    url(r'^$', PathfinderView.as_view(), name='pathfinder'),
]
