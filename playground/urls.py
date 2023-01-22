from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('<str:name>', views.index, name='index')
]

