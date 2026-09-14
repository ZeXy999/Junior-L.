from django.urls import path
from . import views

app_name = 'hello_world'

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('about/', views.about, name='about'),
    path('numbers/', views.numbers, name='numbers'),
    # Catch-all for a named greeting must come last, or it would
    # swallow the literal routes above (e.g. /hello/about/).
    path('<str:name>/', views.hello_world, name='hello_world_named'),
]
