from django.urls import path
from . import views

app_name = 'ultra_odds'
urlpatterns = [

    # url(r'^$', views.index, name='index'),
    path('', views.UltraView.as_view(), name='ultra'),
    path('<int:pk>/', views.UltradetView.as_view(), name='ultradet'),

]
