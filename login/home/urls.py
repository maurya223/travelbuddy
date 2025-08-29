from django.urls import path
from . import views

urlpatterns = [
  path("", views.home_view, name="home"),
  path("login/", views.Login_view, name="login"),
  path("register/", views.Register_view, name="register"),
  path("logout/", views.logout_view, name="logout"),
  path('book/', views.book_view, name='book'), 
  path("my-bookings/", views.my_bookings_view, name="my_bookings"),
  path("cancel-booking/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
  path("contact/", views.contact_view, name="contact"),



]
