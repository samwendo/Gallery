from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length = 25)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(location_id):
        Location.objects.filter(id = location_id).delete()

    def update_location(location_id, location):
        Location.objects.filter(id = location_id).update(location_name = location)

class Category(models.Model):
    category_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(category_id):
        Category.objects.filter(id = category_id).delete()

    def update_category(category_id, category):
        Category.objects.filter(id = category_id).update(category_name = category)

class Photographer(models.Model):
    names = models.CharField(max_length = 50)
    email = models.EmailField(blank = True)
    ig = models.CharField(max_length = 20, blank = True)
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.names

    def save_photographer(self):
        self.save()

    def delete_photographer(photographer_id):
        Photographer.objects.filter(id = photographer_id).delete()

class Image(models.Model):
    image_path = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 50)
    description = models.TextField(blank = True)
    location = models.ForeignKey(Location, blank=True)
    category = models.ForeignKey(Category, blank=True)
    photographer = models.ForeignKey(Photographer)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(image_id):
        Image.objects.filter(id = image_id).delete()

    def update_image(image_id, path):
        Image.objects.filter(id = image_id).update(image_path = path)

    def get_image_by_id(image_id):
        image = Image.objects.get(pk = image_id)
        return image

    @classmethod
    def search_image(cls, search_category):
        images = cls.objects.filter(category__category_name__icontains=search_category)
        return images

    @classmethod
    def filter_by_location(cls):
        images = cls.objects.order_by('location')
        return images

    class Meta:
        ordering = ['name']
