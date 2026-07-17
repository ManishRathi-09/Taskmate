from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User

print([field.name for field in User._meta.fields])