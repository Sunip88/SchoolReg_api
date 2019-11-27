import factory.fuzzy
from django.contrib.auth.models import User

from API_register.models import Teacher, Classes, Announcement


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user_{}'.format(n))
    email = factory.Sequence(lambda n: "user_{}@example.com".format(n))
    password = 'pass'

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)


class TeacherFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Teacher


class ClassFactory(factory.django.DjangoModelFactory):
    educator = factory.SubFactory(TeacherFactory)
    name = factory.Sequence(lambda n: '%01d class' % n)

    class Meta:
        model = Classes


class AnnouncementFactory(factory.django.DjangoModelFactory):
    text = factory.Faker('text', max_nb_chars=200, ext_word_list=None)
    title = factory.Faker('sentence', nb_words=6, variable_nb_words=True, ext_word_list=None)
    date = factory.Faker('date_between', start_date="-30d", end_date="today")
    author = factory.SubFactory(TeacherFactory)
    student_class = factory.SubFactory(ClassFactory)

    class Meta:
        model = Announcement
