from Meeting.serializers import MeetingSerializerOut
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Meeting

# Create your views here.


@method_decorator(cache_page(60 * 5), name="list")
class ListMeeting(generics.ListAPIView):
    serializer_class = MeetingSerializerOut
    queryset = Meeting.objects.all()
