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

    def save(self, *args, **kwargs): 
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 200 or img.width > 200:
            output_size=(200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)

# class Matchedlist(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) 
#     matched = models.ManyToManyField(User, blank=True, related_name="matched") # matched = friends

#     def __str__(self):
#         return self.user.username

#     def add_to_chat(self, account):
#         if not account in self.matched.all():
#             self.matched.add(account)
#             self.save()

#     def remove_from_chat(self, account):
#         if account in self.matched.all():
#             self.matched.remove(account)

#     def remove_from_chat_logic(self, removee):
#         remover_matched_list = self

#         remover_matched_list.remove_from_chat(removee)

#         matched_list = Matchedlist.objects.get(user=removee)
#         matched_list.remove_from_chat(self.user)

#     def is_mutually_matched(self, match):


#         if match in self.matched.all():
#             return True
#         return False


# class Request(models.Model):

#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
#     is_active = models.BooleanField(blank=True, null=False, default=True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.sender.username

#     def accept(self):
#         receiver_matched_list = Matchedlist.objects.get(user=self.receiver)
#         if receiver_matched_list:
#             receiver_matched_list.add_to_chat(self.sender)
#             sender_matched_list = Matchedlist.objects.get(user=self.sender)
#             if sender_matched_list:
#                 sender_matched_list.add_to_chat(self.receiver)
#                 self.is_active = False
#                 self.save()

#     def decline(self):
#         self.is_active = False
#         self.save()

#     def cancel(self):
#         self.is_active = False
#         self.save()

         


