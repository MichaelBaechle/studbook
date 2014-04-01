from django.db import models
from PIL import Image

class Stud(models.Model):
    dog_name = models.TextField()
    dog_pic = models.ImageField(upload_to='orig/')
    dog_pic_thumb = models.TextField()
    owner_name = models.TextField()

    def save(self, *args, **kwargs):
        super(Stud, self).save()

        size = (150,150)

        image = Image.open(self.dog_pic.path)
        image.thumbnail(size, Image.ANTIALIAS)

        dog_pic_thumb_path = self.dog_pic.path.replace('media/orig/', 'media/thumb/')

        image.save(dog_pic_thumb_path)
        self.dog_pic_thumb = self.dog_pic_thumb_url()

        super(Stud, self).save()

    def dog_pic_thumb_url(self):
        return self.dog_pic.url.replace('orig/','thumb/')