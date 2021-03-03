from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    # path('signup/', views.SignupPageView.as_view(), name='signup'),
    # path('profile/', views.user_profile, name='profile')
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
]
