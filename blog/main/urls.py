from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.BlogLoginView.as_view(), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/change', views.ChangeUserInfoView.as_view(),
         name='profile_change'),
    path('accounts/logout/', views.BlogLogoutView.as_view(), name='logout'),
    path('accounts/password/change', views.BlogPasswordChangeView.as_view(),
         name='password_change')
]
