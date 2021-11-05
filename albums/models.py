from django.db import models
from django.utils import timezone

MEDIUM_CHOICES = (
  ('physical', 'PHYSICAL'),
  ('digital', 'DIGITAL')
  )

class Album(models.Model):
  album_art_url: models.URLField()
  title: models.CharField()
  artist: models.CharField(max_length=300)
  medium: models.CharField(max_length=8, choices=MEDIUM_CHOICES, default='digital')

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title
