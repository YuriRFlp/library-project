from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

routers = DefaultRouter()

routers.register(
    "book",
    views.BookViewSet,
    basename="core_book",
)
routers.register(
    "client",
    views.ClientViewSet,
    basename="core_client",
)
routers.register(
    "allocation",
    views.AllocationViewSet,
    basename="core_allocation",
)

urlpatterns = [path("", include(routers.urls))]