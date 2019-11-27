from django.contrib.auth.models import User
from django.core.management import BaseCommand

from API_register.factories import UserFactory, TeacherFactory, ClassFactory, AnnouncementFactory


class Command(BaseCommand):
    help = 'It will create new announcements'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        number_of_announcements = options['poll_ids']
        for i in range(0, number_of_announcements[0]):
            last_user = User.objects.last()
            if last_user:
                last_user = last_user.username.split('_')[1]
            else:
                last_user = -1
            user = UserFactory(__sequence=int(last_user) + 1)
            teacher = TeacherFactory(user=user)
            school_class = ClassFactory(educator=teacher)
            announcement = AnnouncementFactory(author=teacher, student_class=school_class)
            print(f'Success: {i + 1}')
