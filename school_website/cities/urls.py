from django.urls import path

from . import views

app_name = 'cities'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('capitalcities/', views.CitiesOfTheWorldView.as_view()),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/answer/', views.answer, name='answer'),
]