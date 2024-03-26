from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
      path('', views.home, name='myhome'),
      # path('register',views.register, name='register'),
      # path('login', views.Login, name='login'),
      # path('user-logout', views.user_logout, name='user-logout'),
      path('dashboard',views.dashboard, name='dashboard'),
      path('sendemail',views.sendemail,name='sendemail'),
      path('Videos',views.Videos,name='Videos'),
      path('articles', views.articles, name='Articles'),
      

# # Forgot Password Link

#       path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#       path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#       path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#       path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]