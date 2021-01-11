from django.test import TestCase
from .models import Photographer,Location,Image,Category
import datetime as dt

# Create your tests here.
class PhotographerTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.hannah= Photographer(first_name = 'Hannah', last_name ='Njeri')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.hannah,Photographer))   
    # Testing Save Method
    def test_save_method(self):
        self.hannah.save_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0) 
    def test_delete_method(self):
        self.hannah.save_photographer()
        self.hannah.delete_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) == 0) 
    def test_display_method(self):
        self.hannah.save_photographer()
        self.hannah.display_photographers()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0) 
    def test_update_method(self):
        self.hannah.save_photographer()
        new_photographer = Photographer.objects.filter(first_name="Hannah").update(first_name="mercy")
        photographers=Photographer.objects.get(first_name="mercy")
        self.assertTrue(photographers.first_name,"mercy")           

class LocationTestClass(TestCase):
    def setUp(self):
        self.nairobi = Location(photo_location='Kenya')
        self.nairobi.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
    
    def test_updating_location(self):
        location = Location.get_location_id(self.nairobi.id)
        location.update_location('Italy')
        location = Location.get_location_id(self.nairobi.id)
        self.assertTrue(location.photo_location == 'Italy')
    
    def tearDown(self):
        self.nairobi.delete_location() 
class CategoryTestClass(TestCase):
    def setUp(self):
        self.ladieswear = Category(photo_category='Menswear')
        self.ladieswear.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.ladieswear,Category))
    
    def tearDown(self):
        self.ladieswear.delete_category()
    
    
class ImageTestClass(TestCase):
   """
   Tests Image class and its functions
   """
   #Set up method
   def setUp(self):
        self.menswear = Category(photo_category='Menswear')
        self.menswear.save_category()

        self.nairobi = Location(photo_location='Nairobi')
        self.nairobi.save_location()

        self.image = Image(title='Fashion', description='menswear', location=self.nairobi, category=self.menswear)
        self.image.save_image()
   def test_instance(self):
       self.assertTrue(isinstance(self.image, Image))

   def test_save_method(self):
       """
       Function to test an image and its details is being saved
       """
       self.image.save_image()
       images = Image.objects.all()
       self.assertTrue(len(images) > 0)

   def test_delete_method(self):
       """
       Function to test if an image can be deleted
       """
       self.image.save_image()
       self.image.delete_image()

   def test_update_method(self):
       """
       Function to test that an image's details can be updates
       """
       self.image.save_image()
       new_image = Image.objects.filter(photo='image1.jpg').update(photo='download.jpg')
       images = Image.objects.get(photo='download.jpg')
       self.assertTrue(images.photo, 'download.jpg')

   def test_get_image_by_id(self):
       """
       Function to test if you can get an image by its id
       """
       self.image.save_image()
       this_img= self.image.get_image_by_id(self.image.id)
       image = Image.objects.get(id=self.image.id)
       self.assertTrue(this_img, image)

   def test_filter_by_location(self):
       """
       Function to test if you can get an image by its location
       """
       self.image.save_image()
       this_img = self.image.filter_by_location(self.image.location_id)
       image = Image.objects.filter(location=self.image.location_id)
       self.assertTrue(this_img, image)

   def test_filter_by_category_name(self):
       """
       Function to test if you can get an image by its category name
       """
       self.image.save_image()
       images = Image.search_image('this')
       self.assertTrue(len(images)>0)
          

# Create your tests here.
