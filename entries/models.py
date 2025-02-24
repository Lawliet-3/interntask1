from django.db import models

class Entry(models.Model):
    content = models.TextField()
    category = models.CharField(max_length=20, choices=[
        ('text', 'Text'),
        ('image_url', 'Image URL'),
    ])
    timestamp = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'entries'
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.category}: {self.content[:50]}..."

class DataEntry(models.Model):
    CATEGORY_CHOICES = [
        ('text', 'Text'),
        ('image_url', 'Image URL'),
    ]
    
    content = models.TextField(help_text='Enter the content or URL')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='text')
    is_reviewed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Data Entries'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f'{self.category} entry from {self.timestamp.strftime("%Y-%m-%d %H:%M")}'
