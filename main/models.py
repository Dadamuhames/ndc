from django.db import models
from admins.models import json_field_validate, MetaTags, Services, Languages, unique_slug_generator
import cyrtranslit
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.text import slugify
# Create your models here.



# short applications
class ShortApplications(models.Model):
    STATUS = [('На расмотрении', 'На расмотрении'),
              ('Рассмотрено', 'Рассмотрено'), ("Отклонено", "Отклонено")]

    full_name = models.CharField('Name', max_length=255)
    nbm = models.CharField('Nbm', max_length=255)
    email = models.EmailField('Email', blank=True, null=True)
    status = models.CharField('Status', max_length=255, choices=STATUS, default='На расмотрении')


# project applications
class ProjectApplications(models.Model):
    STATUS = [('На расмотрении', 'На расмотрении'),
              ('Рассмотрено', 'Рассмотрено'), ("Отклонено", "Отклонено")]

    full_name = models.CharField('Full name', max_length=255)
    nbm = models.CharField('Nbm', max_length=255)
    email = models.EmailField('Email', blank=True, null=True)
    status = models.CharField('Status', max_length=255, choices=STATUS, default='На расмотрении')


# projects
class Projects(models.Model):
    TYPES = [('Локальные проэкты', 'Локальные проэкты'),
              ('Международные проэкты', 'Международные проэкты')]

    title = models.JSONField('Title', validators=[json_field_validate])
    image_first = ThumbnailerImageField('First image', upload_to='project_images', blank=True, null=True)
    image_second = ThumbnailerImageField('Second image', upload_to='project_images', blank=True, null=True)
    link = models.URLField('Link', blank=True, null=True)
    description = models.JSONField("Descr", blank=True, null=True)
    type = models.CharField('Type', max_length=255, choices=TYPES)
    position = models.PositiveIntegerField('Position')
    meta = models.ForeignKey(MetaTags, on_delete=models.SET_NULL, blank=True, null=True)
    active = models.BooleanField(default=False)
    services = models.ManyToManyField(Services, blank=True, null=True)
    slug = models.SlugField('Slug', editable=False, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            lng = Languages.objects.filter(active=True).filter(default=True).first()
            str = cyrtranslit.to_latin(self.title.get(lng.code, '')[:50])
            print(str)
            slug = slugify(str)
            self.slug = unique_slug_generator(self, slug)

        return super().save(*args, **kwargs)
