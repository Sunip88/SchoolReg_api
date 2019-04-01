from rest_framework import serializers

from API_register.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = ['id', 'title', 'date', 'author', 'text', 'hidden', 'student_class']
