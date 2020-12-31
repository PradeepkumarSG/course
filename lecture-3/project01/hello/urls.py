from django.urls import path
from . import views

urlpatterns= [
  path("", views.index , name="index"),
  path("<str:name>", views.greet, name="greet"),
  path("pradeep", views.pradeep, name="pradeep"),
  path("mani", views.mani, name="mani")
]