from django.conf.urls import url
from au_search import views

urlpatterns = [
    url(r'^$', views.search_view, name='search'),
]
