from django.db import models

DISEASE_CHOICES = [
    ('bt', 'Brain Tumor'),
    ('l', 'Lukemia'),
    ('p', 'Pneumonia'),
]

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to="img/%y")
    disease=models.CharField(max_length=2, choices=DISEASE_CHOICES, default='BT')
    def __str__(self):
        return f'{self.disease}'