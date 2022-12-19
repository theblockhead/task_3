from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
Genders = (
    ('Male','Male'),
    ('Female', 'Female'),
    ('Non-Binary','Non-Binary'),
)
Status= (
    ('Not Committed','Not Committed'),
    ('Committed', 'Committed'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Gender = models.CharField(max_length=20, choices=Genders, default='Male')
    Status = models.CharField(max_length=50, choices=Status, default='Not Committed')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs): 
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 200 or img.width > 200:
            output_size=(200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)
