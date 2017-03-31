from django.conf.urls import url
from au_search import views

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
]
