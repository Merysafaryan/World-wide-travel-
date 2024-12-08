from django.db import models

# Create your models here.

class Fav(models.Model):

    icon = models.ImageField('Fav icon', upload_to='Logos')

    def __str__(self):
        return 'Home Favicon'
    
class Logo(models.Model):

    img = models.ImageField('Logo image', upload_to='Logos')

    def __str__(self):
        return 'Home Logo'

class HomeBgInfo(models.Model):

    static_text = models.CharField('HomeBgInfo text static', max_length=50)
    dinamic_text1 = models.CharField('HomeBgInfo text1 dinamic', max_length=50)
    dinamic_text2 = models.CharField('HomeBgInfo text2 dinamic', max_length=50)
    dinamic_text3 = models.CharField('HomeBgInfo text3 dinamic', max_length=50)
    about = models.TextField('HomeBgInfo')
    button_name = models.CharField('HomeBgInfo button name', max_length=20)

    def __str__(self):
        return f'{self.static_text}'
    

class About(models.Model):

    text1 = models.TextField('About text1')
    text2 = models.TextField('About text2')
    text3 = models.TextField('About text3')
    text4 = models.CharField('About text4', max_length=50)
    img = models.ImageField('About image', upload_to='about', blank=True)

    def __str__(self):
        return 'About section info'
    
class Project(models.Model):

    image = models.ImageField('Project image', upload_to='projects')
    name1 = models.CharField('Project name1', max_length=50)
    name2 = models.CharField('Project name2', max_length=50)
    text1 = models.TextField('Project text1')
    text2 = models.TextField('Project text2')

    def __str__(self):
        return self.name1

class Gallery(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='proj')
    name = models.CharField('Gallery name', max_length=60)
    img = models.ImageField('Gallery image', upload_to='gallery')

    def __str__(self):
        return self.name
    

class Rio(models.Model):
    name = models.CharField(max_length=60, verbose_name="Rio name")
    img = models.ImageField(upload_to='rio', verbose_name="Rio image")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='proj_rio')


    def __str__(self):
        return self.name


class Team(models.Model):
    img = models.ImageField("Person image", upload_to='person')
    name = models.CharField("Person name", max_length=50)
    position = models.CharField('Person position', max_length=60)
    fb = models.TextField('Person fb', blank=True)
    insta = models.TextField('Person insta', blank=True)


    def __str__(self):
        return self.name
    

class ContactInfo(models.Model):

    name = models.CharField('ContactInfo name', max_length=80)
    desc = models.TextField('ContactInfo text')
    address = models.TextField('ContactInfo address')
    phone1 = models.CharField('ContactInfo phone1', max_length=30)
    email = models.EmailField('ContactInfo email')

    def __str__(self):
        return 'ContactInfo'
    

class ContactUs(models.Model):

    name = models.CharField('Contact name', max_length=60)
    email = models.EmailField('Contact email')
    message = models.TextField('COntact text')

    def __str__(self):
        return self.name