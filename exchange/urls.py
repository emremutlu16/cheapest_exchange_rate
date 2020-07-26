from django.urls import path

from exchange import views

urlpatterns = [
    path('get_currencies/', views.get_currencies_view, name='get_currencies')
]
