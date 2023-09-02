from django.db import models
from ..app_users.models import UserOwn
import uuid

class Image(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserOwn, on_delete=models.CASCADE,blank=True,null=True)
    image = models.URLField()
    def save(self,*args,**kwargs):
        self.user.add_file(is_image=True)
        return super().save(*args,**kwargs)
    def delete(self, *args,**kwargs):
        self.user.rest_file(is_image=True)
        return super().delete(*args,**kwargs)
    class Meta:
        ordering=['-created']
