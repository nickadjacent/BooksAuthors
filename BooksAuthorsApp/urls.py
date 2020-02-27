from django.urls import path
from . import views


urlpatterns = [
    path('', views.bookPage),
    path('bookName', views.bookName),
    path('authorPage', views.authorPage),
    path('authorName', views.authorName),
    # *********Everything Below is a redirect Path**************
    path('addAuthor', views.addAuthor),
    path('addBook', views.addBook),

]
