from django.shortcuts import render
from rest_framework import generics
from django.http import Http404

from API_register.models import Announcements
from API_register.serializers import AnnouncementSerializer


class AnnouncementListView(generics.ListAPIView):
    queryset = Announcements.objects.filter(hidden=False)
    serializer_class = AnnouncementSerializer


class AnnouncementDetailView(generics.RetrieveAPIView):
    queryset = Announcements.objects.filter(hidden=False)
    serializer_class = AnnouncementSerializer
