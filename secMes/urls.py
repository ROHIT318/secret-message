from django.urls import path
from . import views

app_name = 'secMes'

urlpatterns = [
	path('', views.home, name='home'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('signup/', views.signup, name='signup'),
	path('sendMsg/', views.sendMsg, name='sendMsg'),
	path('msgPage/', views.msgPage, name='msgPage'),
	path('findUser/', views.findUser, name='findUser'),
	path('outputMessage/', views.outputMessage, name='outputMessage'),
	path('createAccount/', views.createAccount, name='createAccount'),
]