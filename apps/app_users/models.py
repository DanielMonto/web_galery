from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class UserOwn(AbstractUser):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    files=models.IntegerField(default=0)
    images=models.IntegerField(default=0)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        related_name='userown_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        related_name='userown_user_permissions'
    )
    def rest_file(self,is_image:bool):
        if is_image:
            if self.files>0:
                self.files-=1
                self.save()
        else:
            if self.images>0:
                self.images-=1
                self.save()
    def add_file(self,is_image:bool):
        if is_image:
            self.images+=1
            self.save()
        else:
            self.files+=1
            self.save()