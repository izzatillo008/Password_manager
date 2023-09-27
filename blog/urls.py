# password_manager/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.login_view, name='login'),
#     path('passwords', views.password_list, name='passwords'),
#     path('add_password', views.add_password, name='add_password')
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('kk/', views.password_list, name='password_list'),
    path('ol', views.add_password, name='ol'),
    path('logout', views.log_out, name='logout'),
    path('signup/', views.signup, name='signup'),
    
]


