from django.contrib.auth.models import User
from django.db import models


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
class Announcement(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)
    student_class = models.ForeignKey(Classes, on_delete=models.CASCADE, default=None, null=True, blank=True)
