from django.test import TestCase
from .models import Location, Category, Photographer, Image

# Create your tests here.
class LocationTestClass(TestCase):

    def setUp(self):
        self.loc = Location(location_name = 'Mombasa, Kenya')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.loc, Location))

    def test_save_location(self):
        self.loc.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.loc.save_location()
        Location.delete_location(self.loc.id)
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)

    def test_update_location(self):
        Location.update_location(self.loc.id, 'london')
        self.assertEqual(self.loc.location_name, 'london')

class CategoryTestClass(TestCase):

    def setUp(self):
        self.cat = Category(category_name = 'official')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))

    def test_save_category(self):
        self.cat.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.cat.save_category()
        Category.delete_category(self.cat.id)
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)

    def test_update_category(self):
        Category.update_category(self.cat.id, 'official')
        self.assertEqual(self.cat.category_name, 'joking')

class PhotographerTestClass(TestCase):

    def setUp(self):
        self.pho = Photographer(names = 'SAM', email = 'SAM@gmail.com', ig = 'SAM', phone_number = '07888888')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pho, Photographer))

    def test_save_photographer(self):
        self.pho.save_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0)

    def test_delete_photographer(self):
        self.pho.save_photographer()
        Photographer.delete_photographer(self.pho.id)
        photographers = Photographer.objects.all()
        self.assertEqual(len(photographers), 0)

class ImageTestClass(TestCase):

    def setUp(self):
        self.loc = Location(location_name = 'Nairobi, Kenya')
        self.loc.save_location()

        self.cat = Category(category_name = 'official')
        self.cat.save_category()

        self.pho = Photographer(names = 'SAM', email = 'SAM@gmail.com', ig = 'SAM', phone_number = '07888888')
        self.pho.save_photographer()

        self.img = Image(image_path = 'SAM.png', name = 'passport photo', description = 'photo fo passports', location = self.loc, category = self.cat, photographer = self.pho)

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Photographer.objects.all().delete()
        Image.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.img, Image))

    def test_save_image(self):
        self.img.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.img.save_image()
        Image.delete_image(self.img.id)
        images = Image.objects.all()
        self.assertEqual(len(images), 0)

    def test_get_image_by_id(self):
        self.img.save_image()
        image = Image.get_image_by_id(self.img.id)
        self.assertEqual(self.img, image)

    def test_search_image(self):
        self.img.save_image()
        image = Image.search_image(self.img.category)
        self.assertEqual(image)

    def test_filter_by_location(self):
        self.img.save_image()
        image = Image.filter_by_location(self.img.location)
        self.assertEqual(image)

    def test_update_image(self):
        Image.update_image(self.img.id, 'SAM.png')
        self.assertEqual(self.img.image_path, 'SAM.png')
