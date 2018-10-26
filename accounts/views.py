from __future__ import unicode_literals
from django.contrib.auth import login, logout, get_backends, authenticate
from django.template import Template, Context, RequestContext
from django.shortcuts import render
from django.contrib import messages
from django.template.loader import get_template
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, render, redirect, HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.conf import settings
from django.core.urlresolvers import resolve, reverse
from django.contrib.auth import update_session_auth_hash
from accounts.models import User,Department,Gender
from .forms import *
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth import login, logout, get_backends, authenticate

def user_login(request, template_name="accounts/login.html"):
    if request.method == 'POST':
        form =UserLoginForm(request.POST)
        if form.is_valid():
			try:
				user_profile = User.objects.get(username=form.cleaned_data['username'], is_active=True)
				if not user_profile.check_password(form.cleaned_data['password']):
					messages.warning(request, 'Invalid Login Details')
					return HttpResponseRedirect(reverse('user_login'))
			except User.DoesNotExist as e:
				messages.warning(request, 'Invalid Login Details')
				return HttpResponseRedirect(reverse('user_login'))
			backend = get_backends()[0]
			user_profile.backend = "%s.%s" % (backend.__module__, backend.__class__.__name__)
			login(request, user_profile)
			try:
				request.session.pop("prev_logged_in_user")
			except KeyError as e:
				pass
			if request.user.is_superuser:
				return HttpResponseRedirect(reverse('response'))
			# else:
			# 	return HttpResponseRedirect(reverse('home'))
        else:
			print form.errors
    else:
		form = UserLoginForm()
		logout(request)
    
    variables = {
		"page_title": "Login",
		"form" : form
	}
    return render(request,template_name,{'form':form})

def home(request,id=None,userdata=None,template_name='accounts/home.html'):
    if id:
		userdata = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST, instance=userdata)
        
        if form.is_valid():
            form_data=form.save()
            if not id:
				messages.success(request, 'User created successfully.')
            else:
				messages.success(request, 'User details updated.')
			# return HttpResponseRedirect(reverse('idproof_list'))
            return HttpResponseRedirect(reverse('response'))
        else:
            print form.errors,"hai"
    else:
        print "fdgsdfg"
        form=UserRegistrationForm(instance=userdata)
        # variables={
        #     'form':form,
        #     'userdata':userdata
        # }
    return render(request,template_name,{'form':form})

# @login_required
def responce_data(request,template_name='accounts/data.html'):
    if request.method == 'GET':
        user_data = User.objects.all().exclude(username='root')
        return render(request,template_name,{'user_data':user_data})
    else:
        return HttpResponseRedirect(reverse('user_login'))