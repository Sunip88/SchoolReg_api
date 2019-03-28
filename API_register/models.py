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

    def get_educator(self):
        return self.classes_set.all()


# Old Adverts and AdvertsClass
class Announcements(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=64)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, default=None)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     role = models.IntegerField(choices=PROFILE_ROLE_CHOICES, default=0)
#     temp_password = models.CharField(max_length=32)
#     phone = models.CharField(max_length=12, default='')
#
#     def __str__(self):
#         return f'{self.user.first_name}, {self.user.last_name} Profile'
#
#     def save(self, force_insert=False, force_update=False, using=None,
#              update_fields=None):
#         super().save()
#         img = Image.open(self.image.path)
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)
# class Subject(models.Model):
#     name = models.CharField(max_length=128)
#     classes = models.ManyToManyField(Classes)
#
#     def __str__(self):
#         return f'{self.name}'
# class Student(models.Model):
#     year_of_birth = models.PositiveIntegerField(validators=[MinValueValidator(1000), MaxValueValidator(3000)],
#                                                 null=True)
#     classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name}"
#
#
# class Parent(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     students = models.ManyToManyField(Student)
#
#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}'
# class GradeCategory(models.Model):
#     name = models.CharField(max_length=16)
#
#     def __str__(self):
#         return self.name
#
#
# class Grades(models.Model):
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     category = models.ForeignKey(GradeCategory, on_delete=models.CASCADE)
#     grade = models.FloatField(choices=GRADES)
#
#     def __str__(self):
#         return f'{self.subject} - {self.student} - {self.grade}'
# class PresenceList(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     day = models.DateField()
#     present = models.NullBooleanField()
#     schedule = models.ForeignKey('API_register.Schedule', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.student} - {self.day} - {self.present}'
#
#
# class ClassRoom(models.Model):
#     name = models.CharField(max_length=16)
#
#     def __str__(self):
#         return self.name
#
#
# class WorkingHours(models.Model):
#     nr = models.IntegerField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#
#     def __str__(self):
#         return f"{self.start_time} - {self.end_time}"
# class Lessons(models.Model):
#     classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.classes.name} - {self.subject.name} - {self.teacher.user.last_name}"
#
#
# class Schedule(models.Model):
#     lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
#     room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
#     hours = models.ForeignKey(WorkingHours, on_delete=models.CASCADE)
#     weekday = models.IntegerField(choices=WEEKDAYS)
#
#     def __str__(self):
#         return f"{self.lesson} - {self.room}"
# class Notice(models.Model):
#     text = models.CharField(max_length=256)
#     from_user = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     to_user = models.ForeignKey(Student, on_delete=models.CASCADE)
#     accepted = models.NullBooleanField()
#     re_text = models.CharField(max_length=256, default='')
#     date = models.DateField(auto_now_add=True)
#     deleted = models.BooleanField(default=False)
#
#
# class Announcements(models.Model):
#     text = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     read = models.BooleanField(default=False)
#     deleted = models.BooleanField(default=False)
#
#
# class Event(models.Model):
#     lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
#     date_set = models.DateField(auto_now_add=True)
#     date_of_event = models.DateField()
#     title = models.CharField(max_length=64)
#     text = models.TextField()
#     deleted = models.BooleanField(default=False)
