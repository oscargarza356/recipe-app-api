from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    #as_view will use the class as a function returning the class
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me')
]
