from django.db import models

DISEASE_CHOICES = [
    ('bt', 'Brain Tumor'),
    ('l', 'Lukemia'),
    ('p', 'Pneumonia'),
]

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    disease=models.CharField(max_length=2, choices=DISEASE_CHOICES, default='BT')
    def __str__(self):
        # return self.caption
        return f'{self.caption} - {self.disease}'