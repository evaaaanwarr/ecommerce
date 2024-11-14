from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView, CustomPasswordResetConfirmView

urlpatterns = [
    # Accounts 
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.signup_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Reset Password
    path('accounts/password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('accounts/reset/password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password/reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
