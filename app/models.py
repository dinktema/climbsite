from django.db import models


class Climber(models.Model):

    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, primary_key=True)
    image = models.ImageField(upload_to='uploads')

    def __str__(self):
        return self.name


class Post(models.Model):

    POST_TYPES = {('t', 'training'), ('d', 'diary'), ('tr', 'trips'), ('o', 'organisation'),
                  ('c', 'community'), ('m', 'misc'), ('s', 'sales'), ('k', 'knowledge')}

    title = models.CharField(blank=False, max_length=50)
    subtitle = models.CharField(max_length=200)
    issues = models.DateTimeField()
    content = models.TextField(blank=False, max_length=5000)
    image = models.ImageField(upload_to='uploads')
    post_type = models.CharField(choices=POST_TYPES, max_length=2, blank=False)
    location = models.CharField(default='inHead', blank=False, max_length=100)

    climber = models.ForeignKey('Climber', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
