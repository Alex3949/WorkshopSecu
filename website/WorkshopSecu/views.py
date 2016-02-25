from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponseBadRequest

def register(request):
    if 'username' not in request.POST:
        return HttpResponseBadRequest("Il vous manque votre nom d'utilisateur.")
    if 'password' not in request.POST:
        return HttpResponseBadRequest("Il vous manque votre password.")
    username = request.POST['username'].strip()
    passwd = request.POST['password'].strip()

    if username != '' and passwd != '':
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=passwd)

            if user is not None:
                user = auth.authenticate(username=username, password=passwd)
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            messages.add_message(request, messages.ERROR, "Cet utilisateur existe déjà.")
            return HttpResponseRedirect(reverse('login'))
    else:
        messages.add_message(request, messages.ERROR, "Il vous manque votre username ou password.")
        nextUrl = 'index'
        if 'next' in request.POST:
            nextUrl = request.POST['next']
    return HttpResponseRedirect(reverse('login'))
