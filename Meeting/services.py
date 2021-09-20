from datetime import datetime, timedelta
from django.core.cache import cache
from django.db.models.query import QuerySet  # -> add this
from .models import Meeting
from Auth.models import User


def send_confirmation_email_to_user(user: User):
    pass


def get_cached_meetings() -> QuerySet:
    meetings = cache.get_or_set(
        "meetings", Meeting.objects.select_related("created_by"), 60 * 60
    )
    cache.close()
    return meetings


# @app.task #->  it's about background task, forget about it now
def check_emails():
    meetings = get_cached_meetings()
    for meeting in meetings:
        if (
            datetime.now() - meeting.created_at > timedelta(hours=1)
            and meeting.members_joined < 2
        ):
            send_confirmation_email_to_user(meeting.user)
