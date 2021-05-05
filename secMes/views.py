from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, auth
from .models import message
from datetime import date
import random
import math

uname=""

# Create your views here.
def home(request):
	return render(request, 'home.html')

def signup(request):
	return render(request, 'signup.html')

def createAccount(request):
	if request.method == 'POST':
		pname = request.POST['cname']
		pswd = request.POST['cpswd']

		## storing strings in a list
		digits = [i for i in range(0, 10)]
		random_str = ""
		## we can generate any lenght of string we want
		for i in range(6):
			index = math.floor(random.random() * 10)
			random_str += str(digits[index])
		## displaying the random string
		pname += random_str

		user = User.objects.create_user(username=pname, password=pswd,
					email=pname, first_name=pname, last_name=pname)
		user.save()

		context = {'name': pname}
	else:
		context = {'name': 'no name'}
	return render(request, 'message.html', context)


def login(request):
	if request.method == 'POST':
		username = request.POST['lname']
		pswd = request.POST['lpswd']
		user = auth.authenticate(username=username, password=pswd)
		if user is not None:
			auth.login(request, user)
			return HttpResponse("Logged in successfully!!")
		else:
			pass
	else:
		return render(request, 'login.html')

def findUser(request):
	if request.method=='POST':
		global uname
		uname = request.POST['uname']
		if User.objects.filter(username=uname).exists():
			return render(request, 'iMes.html')
		else:
			context = {'name': 'User is not present.'}
	return render(request, 'message.html', context)


def sendMsg(request):
	if request.method=='POST':
		today = date.today()
		d1 = today.strftime("%Y-%m-%d")
		msg = request.POST['msg']
		uname = request.POST['uname']
		mess = message.objects.create(username=uname, msg=msg, time=d1)
		mess.save()
		return render(request, 'home.html')
	else:
		return render(request, 'message.html')


def outputMessage(request):
	if request.method == 'POST':
		username = request.POST['lname']
		pswd = request.POST['lpswd']
		user = auth.authenticate(username=username, password=pswd)
		if user is not None:
			auth.login(request, user)
			mess = message.objects.filter(username=username)
			context = {'messages': mess}
			return render(request, 'showMessage.html', context)
		else:
			context = {'message': "Invalid username or password given."}
			return render(request, 'login.html', context)
	else:
		pass
		# Nothing needs to be done

def logout(request):
	auth.logout(request)
	return render(request, 'home.html')

def msgPage(request):
 	return render(request, 'iMes.html')