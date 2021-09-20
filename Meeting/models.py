from django.db import models
from datetime import datetime
from django.conf import settings
from enum import Enum


class MeetingCategory(Enum):
    PERSONAL = "Personal"
    ENTERTAINMENT = "Entertainment"
    BUSINESS = "Business"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Meeting(models.Model):

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="meetings"
    )
    category: str = models.CharField(
        max_length=25,
        null=False,
        choices=MeetingCategory.choices(),
        default=MeetingCategory.PERSONAL,
    )
    created_at: datetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id}"
