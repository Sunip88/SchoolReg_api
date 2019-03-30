from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from PIL import Image


GRADES = (
    (1, "1"),
    (1.5, "1+"),
    (1.75, "2-"),
    (2, "2"),
    (2.5, "2+"),
    (2.75, "3-"),
    (3, "3"),
    (3.5, "3+"),
    (3.75, "4-"),
    (4, "4"),
    (4.5, "4+"),
    (4.75, "5-"),
    (5, "5"),
    (5.5, "5+"),
    (5.75, "6-"),
    (6, "6")
)

WEEKDAYS = [
    (1, 'Poniedziałek'),
    (2, 'Wtorek'),
    (3, 'Środa'),
    (4, 'Czwartek'),
    (5, 'Piątek'),
]


PROFILE_ROLE_CHOICES = [
    (0, "Student"),
    (1, "Parent"),
    (2, "Teacher"),
]


class Classes(models.Model):
    educator = models.ForeignKey('API_register.Teacher', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_classes(self):
        return self.classes_set.all()


# Old Adverts and AdvertsClass
class Announcements(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, default=None, null=True, blank=True)
