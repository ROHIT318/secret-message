from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from .models import message
from datetime import date
import random
import math

unique_id=""

# Create your views here.
def home(request):
	return render(request, 'newHome.html')

def signup(request):
	return render(request, 'newSignup.html')

def createAccount(request):
	if request.method == 'POST':
		name = request.POST['name']
		pswd = request.POST['pswd']

		## storing strings in a list
		digits = [i for i in range(0, 10)]
		random_str = ""
		## we can generate any length of string we want
		for i in range(6):
			index = math.floor(random.random() * 10)
			random_str += str(digits[index])
		## displaying the random string
		name += random_str
		user = User.objects.create_user(username=name, password=pswd)
		user.save()
		context = {'name': name}
	else:
		context = {'name': "Some error happened, please try again."}
	return render(request, 'GetId.html', context)


def login(request):
	if request.method == 'POST':
		global unique_id
		username = request.POST['unique_id']
		pswd = request.POST['pswd']
		unique_id = username
		# print(unique_id)
		# print(username)
		user = auth.authenticate(username=username, password=pswd)
		if user is not None:
			auth.login(request, user)
			return outputMessage(request)
		else:
			context = {'message': "Invalid username or password given."}
			return render(request, 'newLogin.html', context)
	else:
		return render(request, 'newLogin.html')

# Shows received messages or act accordingly
def outputMessage(request):
	global unique_id
	# print(unique_id)
	mess = message.objects.filter(username=unique_id)
	if mess is not None:
		context = {'messages': mess, 'username': unique_id}
	else:
		context = {'messages': "No messages found", 'username': unique_id}
	# print(unique_id)
	return render(request, 'receivedMessages.html', context)

def findUser(request):
	if request.method=='POST':
		global uname
		uname = request.POST['uname']
		if User.objects.filter(username=uname).exists():
			return render(request, 'sendMessage.html')
		else:
			context = {'name': 'User is not present.'}
	return render(request, 'GetId.html', context)

def sendMsg(request):
	if request.method=='POST':
		today = date.today()
		d1 = today.strftime("%Y-%m-%d")
		msg = request.POST['msg']
		unique_id = request.POST['unique_id']
		mess = message.objects.create(username=unique_id, msg=msg, time=d1)
		mess.save()
		context = {'mess': "Message sent successfully."}
		return render(request, 'newHome.html', context)
	else:
		return render(request, 'sendMessage.html')

def sendToId(request, unique_id):
	context = {'unique_id': unique_id}
	return render(request, 'sendMessage.html', context)

def logout(request):
	auth.logout(request)
	return render(request, 'newHome.html')

def msgPage(request):
 	return render(request, 'sendMessage.html')


def aboutCreator(request):
	pass