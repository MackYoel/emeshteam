from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from .forms import PersonForm
from django.http import HttpResponse
from django.contrib.auth import login, logout
from project.settings import APP_NAME
from .models import Person, Score
from main.utils import sort_by_score
import json
# import time
from random import randint


@login_required
def home(req):
    # file_version = time.time()
    app_name = APP_NAME
    users = Person.objects.all()
    return render(req, 'main/home.html', locals())


class LoginHandler(View):
    template_name = 'main/login.html'

    def get(self, request, *args, **kwargs):
        is_authenticated = request.user.is_authenticated()
        app_name = APP_NAME
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):

        form = PersonForm(data=request.POST)
        if form.is_valid():
            user = form.get_or_create_user()
            login(request, user)
            if request.is_ajax():
                return HttpResponse()
            return redirect(reverse('main:home'))
        return HttpResponse(json.dumps(form.errors), content_type='application/json', status=400)  # NOQA


def logout_handler(request):
    logout(request)
    return redirect(reverse('main:LoginHandler'))


@login_required
def lunch(request):
    app_name = APP_NAME
    users = Person.objects.all()
    users = sorted(users, key=sort_by_score, reverse=True)
    return render(request, 'main/lunch.html', locals())


@login_required
def generate_score(request):
    user = request.user
    if not user.has_score:
        score = Score(person=user, score=randint(1, 100))
        score.save()
    return redirect(reverse('main:lunch'))
