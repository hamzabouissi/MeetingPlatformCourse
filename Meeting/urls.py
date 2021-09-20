from Meeting.views import ListMeeting
from rest_framework.urls import path

urlpatterns = [
    path("meeting", ListMeeting.as_view(), name="list-meeting"),
]
