from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length =30)
    photographer = models.ForeignKey(Photographer)
    description = models.TextField(max_length =30)
    image = models.ImageField(upload_to = 'photos/', default='No image')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True, null=True) 

    class Meta:
        ordering = ('-id',)

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.title    
    classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
    
    @classmethod
    def get_image_by_id(cls, id):
        an_image = Image.objects.get(id=id)
        return an_image    


    @classmethod
    def search_by_category(cls,search_term):
        photo = cls.objects.filter(category__photo_category__icontains=search_term)
        return photo_category        
    @classmethod
    def filter_by_location(cls, id):
       images = Image.objects.filter(location_id=id)
       return images 

class Category(models.Model):
    photo_category = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.photo_category = update
        self.save()
    def get_category_id(cls,id):
        category = Category.object.get(pk = id)
        return category

    def __str__(self):
        return self.photo_category   

class Location(models.Model):
    photo_location = models.CharField(max_length =30)

    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    def update_location(self, update):
        self.photo_location = update
        self.save()  

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate
    def __str__(self):
        return self.photo_location                  