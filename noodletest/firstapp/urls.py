from django.urls import path
from . import views

urlpatterns = [
    path('register-user/', views.RegisterUser.as_view({'post': 'post'}), name='register-user'),
    path('newsletters/<str:cat>/', views.GetNewsletters.as_view({'get': 'get'}), name='newsletters')
]
