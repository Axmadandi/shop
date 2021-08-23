from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .import views

app_name = 'accounts'

urlpatterns = [
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),

	path('register/', views.RegisterView.as_view(), name='register'),
	path('customer/', views.customer, name='customer'),
]