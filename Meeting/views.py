from Meeting.services import get_cached_meetings
from Meeting.serializers import MeetingSerializerOut
from rest_framework import generics
from .models import Meeting

# Create your views here.


class ListMeeting(generics.ListAPIView):
    serializer_class = MeetingSerializerOut
    queryset = Meeting.objects.all()

    def get_queryset(self):
        queryset = get_cached_meetings()
        return queryset
