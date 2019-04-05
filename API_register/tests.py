from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.utils import json

from API_register.serializers import AnnouncementSerializer
from .models import Teacher, Announcement

client = Client()


class NewAnnouncementTest(TestCase):

    def setUp(self):
        self.date_today = datetime.today()
        test_user = User.objects.create_user(username='testuser', password='12345')
        self.teacher = Teacher.objects.create(user=test_user)

        self.valid_announcement = {
            'text': 'testing content of announcement',
            'title': 'test title test',
            'date': str(self.date_today),
            'author': str(self.teacher.id),
            'student_class': None,
        }

        self.invalid_announcement = {
            'text': 'testing content of announcement',
            'title': '',
            'date': self.date_today,
            'author': self.teacher,
            'student_class': None,
        }

    def test_create_valid_announcement(self):
        response = client.post(
            path=reverse('announcement_list'),
            data=json.dumps(self.valid_announcement),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_announcement(self):
        test_sub = Announcement.objects.create(title='aaa', text='bbb', date=self.date_today, author=self.teacher)
        response = client.get(
            path=reverse('announcement_list')
        )
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        self.assertDictEqual(response.data, serializer.data[0])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
