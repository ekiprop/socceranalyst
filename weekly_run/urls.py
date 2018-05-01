from django.urls import path
from . import views

app_name = 'weekly_run'
urlpatterns = [

    # url(r'^$', views.index, name='index'),
    path('', views.WeeklyView.as_view(), name='weekly'),
    path('<int:pk>/', views.WeekdetView.as_view(), name='weekdet'),

]
