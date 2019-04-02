from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.widgets import RangeWidget
import django_filters

from .models import Announcement, Teacher, Classes
from .serializers import AnnouncementSerializer


class AnnouncementListFilter(django_filters.FilterSet):
    author = django_filters.ModelChoiceFilter(queryset=Teacher.objects.all())
    student_class = django_filters.ModelChoiceFilter(queryset=Classes.objects.all())
    date = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Announcement
        fields = ['author', 'student_class', 'date']


class AnnouncementListView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = AnnouncementListFilter


class AnnouncementDetailView(generics.RetrieveUpdateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
