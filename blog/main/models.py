from django.db import models
from django.contrib.auth.models import AbstractUser

class BlogUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='activated?')
    class Meta(AbstractUser.Meta):
        pass
