from django.urls import path
from .views import Register,Login,Index,LogoutUser,A,B
urlpatterns = [
    path('',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('index/',Index.as_view(),name='index'),
    path('logout/',LogoutUser.as_view(),name='logout'),
    path('a/',A.as_view(),name='a_page'),
    path('b/',B.as_view(),name='b_page'),
]