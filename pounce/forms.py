from django.forms import ModelForm

from .models import Course, Subscription


class CourseForm(ModelForm):
     class Meta:
         model = Course
         fields = ['subject', 'number']


class SubscriptionForm(ModelForm):
     class Meta:
         model = Subscription
         fields = ['email', 'phone']
