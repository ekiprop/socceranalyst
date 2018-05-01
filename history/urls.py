from django.urls import path
from . import views

app_name = 'history'
urlpatterns = [

    # url(r'^$', views.index, name='index'),
    path('prev_daily/', views.PrevDailyView.as_view(), name='prev_daily'),
    path('prev_ultra/', views.PrevUltraView.as_view(), name='prev_ultra'),
    path('prev_weekly/', views.PrevWeeklyView.as_view(), name='prev_weekly'),

]
