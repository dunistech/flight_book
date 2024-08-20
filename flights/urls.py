from django.urls import path
from . import views

# urlpatterns = [
#     # path("", views.index, name="index"),
#     path("", views.home, name="home"),
#     path("<int:flight_id>", views.flight, name="flight"),
#     path("<int:flight_id>/book", views.book, name="book"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book"),
    path("add/", views.add_flight, name="add_flight"),
    path("<int:flight_id>/edit/", views.edit_flight, name="edit_flight"),
    path("<int:flight_id>/delete/", views.delete_flight, name="delete_flight"),
]
