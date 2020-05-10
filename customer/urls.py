from django.urls import path
from . import views

app_name = "customer"
urlpatterns = [
    path("<int:id>/",views.CustomerView.as_view(),name = "customer_view"),
    path("signup/",views.SignUp.as_view(),name="signup"),
    path("login/", views.LogIn.as_view(),name="login")
]   