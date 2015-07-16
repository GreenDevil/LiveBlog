from django.contrib import admin
from django.db import models


class Update(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ['-id']
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __unicode__(self):
        return "[%s] %s" % (
            self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            self.text
        )


admin.site.register(Update,)