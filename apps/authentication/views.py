from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth

from django.core import serializers
#from .serializers import UserSerializer
from .models import User


# Create your views here.
def get_user(request):
    # loop through keys and values
    for key, value in request.POST.iteritems():
        print "%s => %s" %(key, value)

    data = serializers.serialize("json", [User.objects.get(pk=1)])

    return render_to_response(data, mimetype='application/json')


def authentication_view(request):
    username = request.POST.get('username', '')  # emtpy string if no username exists
    password = request.POST.get('password', '')  # empty string if no password exists

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user);
        return HttpResponseRedirect('/authentication/loggedin/')
    else:
        return HttpResponseRedirect('/authentication/invalid/')


def loggedin_view(request):
    return render_to_response('loggedin.html', {'full_name': request.user.get_username()})


def invalid_login_view(request):
    return render_to_response('invalid.html')


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')