from rest_framework import serializers

from API_register.models import Announcements


class AnnouncementGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcements
        fields = ['id', 'title', 'date', 'author', 'text', 'deleted', 'classes']
