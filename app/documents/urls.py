from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from documents import views


urlpatterns = [
    url(r'^document/upload$',views.upload_book, name='upload_book'),
    url(r'^document/$', views.book_list, name='book_list'),
    url(r'^home/$', views.homePage, name='homePage'),
]
