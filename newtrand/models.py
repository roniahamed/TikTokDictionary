from django.db import models

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

