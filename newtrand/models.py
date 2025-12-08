from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class NewTrandModel(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    example_sentence = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='new_trands', blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    is_category = models.BooleanField(default=False)
    alternate_spellings = models.JSONField(blank=True, null=True)
    hashtags = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word
    class Meta:
        ordering = ['-created_at', 'word']
        verbose_name = 'NewTrand'
        verbose_name_plural = 'NewTrands'


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reactions')
    new_trand = models.ForeignKey(NewTrandModel, on_delete=models.CASCADE, related_name='reactions')
    reaction_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.reaction_type} on {self.new_trand.word}"
    class Meta:
        unique_together = ('user', 'new_trand')
        ordering = ['-created_at']
    

