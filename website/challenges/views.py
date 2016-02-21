from django.shortcuts import render, get_object_or_404
from .models import Challenge
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'challenges/index.html'
    model = Challenge
    context_object_name = 'challenges_list'

class DetailView(generic.DetailView):
    model = Challenge
    template_name = 'challenges/detail.html'

@login_required
def flag(request, pk):
    if 'flag' not in request.POST:
        return HttpResponseBadRequest("Il vous manque le flag.")
    challenge = get_object_or_404(Challenge, pk=pk)
    attempt = request.POST['flag'].strip()
    if attempt != challenge.flag:
        messages.add_message(request, messages.ERROR, "Ce n'est pas le bon flag.")
    else:
        if request.user not in challenge.resolved_by.all():
            messages.add_message(request, messages.SUCCESS, "Félicitation, vous avez réussi ce challenge.")
            challenge.resolved_by.add(request.user)
        else:
            messages.add_message(request, messages.INFO, "Vous aviez déjà résolu ce challenge.")
    return HttpResponseRedirect(reverse('detail', args=[challenge.id]))

