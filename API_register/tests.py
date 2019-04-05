from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.utils import json

from .models import Teacher

client = Client()


class NewAnnouncementTest(TestCase):

    def setUp(self):
        date_today = datetime.today()
        test_user = User.objects.create_user(username='testuser', password='12345')
        teacher = Teacher.objects.create(user=test_user)

        self.valid_announcement = {
            'text': 'testing content of announcement',
            'title': 'test title test',
            'date': str(date_today),
            'author': str(teacher.id),
            'student_class': None,
        }

        self.invalid_announcement = {
            'text': 'testing content of announcement',
            'title': '',
            'date': date_today,
            'author': teacher,
            'student_class': None,
        }

    def test_create_valid_announcement(self):
        response = client.post(
            path=reverse('announcement_list'),
            data=json.dumps(self.valid_announcement),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
