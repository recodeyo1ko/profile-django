from django.db import models

# Create your models here.

class Question(models.Model):
    class Meta:
        db_table = 'question'

    name = models.CharField(max_length=255, verbose_name='名前', default='名無し')
    title = models.CharField(max_length=255, verbose_name='タイトル')
    content = models.TextField(verbose_name='内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')
