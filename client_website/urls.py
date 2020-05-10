from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("product/", include("product.urls")),
    path("customer/",include("customer.urls")),
    path('admin/', admin.site.urls),
]
