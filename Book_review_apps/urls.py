from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    path('register', views.register),
    path('profile/<int:userid>', views.profile),
    path('review/<int:bookid>edit', views.reviewEdit)
]

