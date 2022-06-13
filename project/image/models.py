from django.db import models

DISEASE_CHOICES = [
    ('bt', 'Brain Tumor (MRI scan of brain of Patient)'),
    ('l', 'Acute Lymphoblastic Lukemia '
          '(Image of bone marrow cell of patient)'),
    ('p', 'Pneumonia (Chest x-ray of patient)'),
    ('k', 'Kidney Disease (Torso x-ray of patient)')
]


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="img/%y")
    disease = models.CharField(
        max_length=2, choices=DISEASE_CHOICES, default='BT')

    def __str__(self):
        return f'{self.disease}'
