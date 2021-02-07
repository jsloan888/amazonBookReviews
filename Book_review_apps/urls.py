from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    path('register', views.register),
    path('profile/<int:userid>', views.profile),
    path('new/review/<int:userid>', views.new),
    path('profile/<int:userid>/create', views.createReview),
    path('review/<int:bookid>/edit', views.editReview),
    # path('profile/<int:userid>/<int:bookid>/edit', views.editReview),
    path('review/<int:bookid>', views.deletereview),
    path('review/<int:bookid>reviewedit', views.reviewEdit),
    path('profile/<int:userid>/<bookid>/comment', views.comment),

    #not working yet 
    # path('profile/<int:userid>/<commentid>/deleteComment', views.deleteComment),
    #
]
