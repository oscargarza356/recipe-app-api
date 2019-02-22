from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

#the defaultrouter automatically creates the url for all our authentication_classes
#works with the view set
#ex will generate /api/recipe/tags/1
router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns=[
    path('',include(router.urls))
]
