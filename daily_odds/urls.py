from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'daily_odds'
urlpatterns = [
    # path('', views.index, name='index'),
    # url(r'^$', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DailydetView.as_view(), name='dailydet'),

]
