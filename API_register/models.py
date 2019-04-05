from django.contrib.auth.models import User
from django.db import models


class HiddenManager(models.Manager):
    use_for_related_fields = True

    def all(self, **kwargs):
        return self.filter(hidden=False, **kwargs)


class HiddenModel(models.Model):
    hidden = models.BooleanField(default=False)
    objects = HiddenManager()
    original_objects = models.Manager()

    def delete(self, *args, **kwargs):
        self.hidden = True

    class Meta:
        abstract = True


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
class Announcement(HiddenModel):
    text = models.TextField()
    title = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Classes, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
