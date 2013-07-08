from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


# Create your models here.
class Weight(models.Model):
    user_id = models.ForeignKey(User)
    weight = models.CharField(max_length=6)
    date_entered = models.DateTimeField('date entered')

    def get_weight(self):
        return self.weight

    def __unicode__(self):
        return self.weight


class Goal(models.Model):
    user_id = models.ForeignKey(User)
    goal_weight = models.CharField(max_length=6)
    date_entered = models.DateTimeField('date entered')

    def get_goal_weight(self):
        return self.goal_weight

    def __unicode__(self):
        return self.goal_weight
