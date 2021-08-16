from django.urls import path
from .views import CakeVariety, DisplayCakes, CakeOrder

urlpatterns = [
    path('displaycakes',DisplayCakes.as_view()),
    path('cakeorder',CakeOrder.as_view()),
    path('cakeorder/<int:pk>/',CakeOrder.as_view()),
    path('cakevariety',CakeVariety.as_view())
]