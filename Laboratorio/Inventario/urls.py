from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('registrarInv/', views.registrarInv),
    path('deleteInv/<codigo>', views.deleteInv),
    path('editEntry/', views.editEntry),
    path('editInventory/<codigo>', views.editInventory)

]