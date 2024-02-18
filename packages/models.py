from django.db import models

# Create your models here.
class Destination(models.Model):
  spotname=models.CharField(max_length=100)
  spotdistrict=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  landscape=models.CharField(max_length=100)
  cafespot=models.CharField(max_length=100,blank=True, null=True, default=None)
  description=models.CharField(max_length=250)
  img=models.ImageField(upload_to='destination')

  def __str__(self):
        return self.spotname
  class Meta:
        ordering = ['id']


class Onedaypackage(models.Model):
  MORNING = 'Morning'
  AFTERNOON = 'Afternoon'
  EVENING = 'Evening'

  TIME_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (EVENING, 'Evening'),
    ]
  id=models.AutoField(primary_key=True)
  district=models.CharField(max_length=100)
  packagenumber=models.PositiveIntegerField()
  daynumber=models.PositiveIntegerField()
  spottime=models.CharField(max_length=20, choices=TIME_CHOICES)
  spotname=models.ForeignKey(Destination, on_delete=models.CASCADE,default=None)
  
  def __str__(self):
        objectname=self.district+str(self.packagenumber)+'->'+str(self.daynumber)+'->'+self.spottime
        return objectname
  
  class Meta:
        #db_table = "1daypackage" for db name
        db_table_comment = "packages for 1day tour selection"  #for comments
        ordering = ['id']

class Twodaypackage(models.Model):
  MORNING = 'Morning'
  AFTERNOON = 'Afternoon'
  EVENING = 'Evening'

  TIME_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (EVENING, 'Evening'),
    ]
  id=models.AutoField(primary_key=True)
  district=models.CharField(max_length=100)
  packagenumber=models.PositiveIntegerField()
  daynumber=models.PositiveIntegerField()
  spottime=models.CharField(max_length=20, choices=TIME_CHOICES)
  spotname=models.ForeignKey(Destination, on_delete=models.CASCADE,default=None)
  
  def __str__(self):
        objectname=self.district+str(self.packagenumber)+'->'+str(self.daynumber)+'->'+self.spottime
        return objectname
  
  class Meta:
        #db_table = "2daypackage" for db name
        db_table_comment = "packages for 2day tour selection"  #for comments
        ordering = ['id']

class Threedaypackage(models.Model):
  MORNING = 'Morning'
  AFTERNOON = 'Afternoon'
  EVENING = 'Evening'

  TIME_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (EVENING, 'Evening'),
    ]
  id=models.AutoField(primary_key=True)
  district=models.CharField(max_length=100)
  packagenumber=models.PositiveIntegerField()
  daynumber=models.PositiveIntegerField()
  spottime=models.CharField(max_length=20, choices=TIME_CHOICES)
  spotname=models.ForeignKey(Destination, on_delete=models.CASCADE,default=None)

  def __str__(self):
        objectname=self.district+str(self.packagenumber)+'->'+str(self.daynumber)+'->'+self.spottime
        return objectname
  
  class Meta:
        #db_table = "3daypackage" for db name
        db_table_comment = "packages for 3day tour selection"  #for comments
        ordering = ['id']

class Fourdaypackage(models.Model):
  MORNING = 'Morning'
  AFTERNOON = 'Afternoon'
  EVENING = 'Evening'

  TIME_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (EVENING, 'Evening'),
    ]
  id=models.AutoField(primary_key=True)
  district=models.CharField(max_length=100)
  packagenumber=models.PositiveIntegerField()
  daynumber=models.PositiveIntegerField()
  spottime=models.CharField(max_length=20, choices=TIME_CHOICES)
  spotname=models.ForeignKey(Destination, on_delete=models.CASCADE,default=None)
  
  def __str__(self):
        objectname=self.district+str(self.packagenumber)+'->'+str(self.daynumber)+'->'+self.spottime
        return objectname
  
  class Meta:
        #db_table = "4daypackage" for db name
        db_table_comment = "packages for 4day tour selection"  #for comments
        ordering = ['id']

class Fivedaypackage(models.Model):
  MORNING = 'Morning'
  AFTERNOON = 'Afternoon'
  EVENING = 'Evening'

  TIME_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (EVENING, 'Evening'),
    ]
  id=models.AutoField(primary_key=True)
  district=models.CharField(max_length=100)
  packagenumber=models.PositiveIntegerField()
  daynumber=models.PositiveIntegerField()
  spottime=models.CharField(max_length=20, choices=TIME_CHOICES)
  spotname=models.ForeignKey(Destination, on_delete=models.CASCADE,default=None)
  
  def __str__(self):
        objectname=self.district+str(self.packagenumber)+'->'+str(self.daynumber)+'->'+self.spottime
        return objectname
  
  class Meta:
        #db_table = "5daypackage" for db name
        db_table_comment = "packages for 5day tour selection"  #for comments
        ordering = ['id']

class Sixdaypackage(models.Model):
  MORNING = 'Morning'
  AFTERNOON = 'Afternoon'
  EVENING = 'Evening'

  TIME_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (EVENING, 'Evening'),
    ]
  id=models.AutoField(primary_key=True)
  district=models.CharField(max_length=100)
  packagenumber=models.PositiveIntegerField()
  daynumber=models.PositiveIntegerField()
  spottime=models.CharField(max_length=20, choices=TIME_CHOICES)
  spotname=models.ForeignKey(Destination, on_delete=models.CASCADE,default=None)
  
  def __str__(self):
        objectname=self.district+str(self.packagenumber)+'->'+str(self.daynumber)+'->'+self.spottime
        return objectname
  
  class Meta:
        #db_table = "6daypackage" for db name
        db_table_comment = "packages for 6day tour selection"  #for comments
        ordering = ['id']

class Sevendaypackage(models.Model):
  MORNING = 'Morning'
  AFTERNOON = 'Afternoon'
  EVENING = 'Evening'

  TIME_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (EVENING, 'Evening'),
    ]
  id=models.AutoField(primary_key=True)
  district=models.CharField(max_length=100)
  packagenumber=models.PositiveIntegerField()
  daynumber=models.PositiveIntegerField()
  spottime=models.CharField(max_length=20, choices=TIME_CHOICES)
  spotname=models.ForeignKey(Destination, on_delete=models.CASCADE,default=None)
  
  def __str__(self):
        objectname=self.district+str(self.packagenumber)+'->'+str(self.daynumber)+'->'+self.spottime
        return objectname
  
  class Meta:
        #db_table = "7daypackage" for db name
        db_table_comment = "packages for 7day tour selection"  #for comments
        ordering = ['id']
  

class Tourpackage(models.Model):
  MORNING = 'Morning'
  AFTERNOON = 'Afternoon'
  EVENING = 'Evening'

  TIME_CHOICES = [
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (EVENING, 'Evening'),
    ]
  
  ONEDAYPACKAGE='1daypackage'
  TWODAYPACKAGE='2daypackage'
  THREEDAYPACKAGE='3daypackage'
  FOURDAYPACKAGE='4daypackage'
  FIVEDAYPACKAGE='5daypackage'
  SIXDAYPACKAGE='6daypackage'   
  SEVENDAYPACKAGE='7daypackage'

  CATEGORY_CHOICES=[
       (ONEDAYPACKAGE, '1daypackage'),
       (TWODAYPACKAGE, '2daypackage'),
       (THREEDAYPACKAGE, '3daypackage'),
       (FOURDAYPACKAGE, '4daypackage'),
       (FIVEDAYPACKAGE, '5daypackage'),
       (SIXDAYPACKAGE, '6daypackage'),
       (SEVENDAYPACKAGE, '7daypackage'),

  ]


  id=models.AutoField(primary_key=True)
  packagecategory=models.CharField(max_length=20, choices=CATEGORY_CHOICES)
  district=models.CharField(max_length=100)
  packagenumber=models.PositiveIntegerField()
  daynumber=models.PositiveIntegerField()
  spottime=models.CharField(max_length=20, choices=TIME_CHOICES)
  spotname=models.ForeignKey(Destination, on_delete=models.CASCADE,default=None)
  
  def __str__(self):
        objectname=self.packagecategory+'->'+self.district+str(self.packagenumber)+'->Day '+str(self.daynumber)+'->'+self.spottime+'->'+str(self.spotname)
        return objectname
  
  class Meta:
        db_table_comment = "packages for 7day tour selection"  #for comments
        ordering = ['id']