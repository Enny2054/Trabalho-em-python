from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.name

        def image_admin(self):
            if self.image:
                return mark_safe(f'<img src="{self.image.url}"
                width="80" />')
                else:
                    return "No image"

                    image_admin.short_description = 'Image'
