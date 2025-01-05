from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class Tag(models.Model):
    captions = models.CharField(max_length=50)

    def __str__(self):
        return self.captions


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name_with_email(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def __str__(self):
        return self.full_name_with_email()


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return f"{self.title} on {self.date}"

    ## This method is handled in admin.py
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, *kwargs)
