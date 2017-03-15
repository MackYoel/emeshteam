from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, time


def str_obj(user):
    return user.email


User.__str__ = str_obj


class Person(User):

    picture = models.CharField(max_length=255, null=True, blank=True)
    fb_id = models.CharField(max_length=255, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._score = None

    @property
    def has_score(self):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        return Score.objects.filter(person=self, generated_at__range=(today_start, today_end)).exists()

    @property
    def score(self):
        if self._score is not None:
            return self._score

        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        try:
            self._score = Score.objects.get(person=self, generated_at__range=(today_start, today_end)).score
            return self._score
        except Score.DoesNotExist:
            return None


class Score(models.Model):
    person = models.ForeignKey(Person)
    score = models.IntegerField()
    generated_at = models.DateTimeField(auto_now_add=True)
