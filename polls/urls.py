from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path('dash/', views.dash, name="dash"),
   # path('stats/',views.leaderboard, name="stats"),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('resp/', views.resp, name="resp"),
    path('addemp/', views.addemp, name="addemp"),
    path('update/<str:pk>', views.pointsform, name="update"),
    path('delete/<str:pk>/', views.deleteEmp, name="delete"),
    path('addcrit/<str:pk>/', views.newCriteria, name="newcrit"),
    path('search/', views.searchbar, name="search"),
        
    
]