from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from main.models import Person


class FakeSession(MiddlewareMixin):

    def process_request(self, request):
        if not request.user.is_authenticated():
            try:
                user = User.objects.get(email='yoel.zalas@gmail.com')
                login(request, user)
            except User.DoesNotExist:
                pass


class PersonMiddleware(MiddlewareMixin):

    def process_request(self, request):
        user = request.user
        if not user.is_superuser and user.is_authenticated():
            request.user = Person.objects.get(pk=user.pk)
