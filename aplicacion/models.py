from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seinen(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)  
    title = models.CharField(max_length=100)
    japanese_title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    authors = models.CharField(max_length=100)
    publication_date = models.CharField(max_length=100)
    chapter = models.IntegerField(default=0)
    volume = models.IntegerField(default=0)  
    READING = "Reading"
    PTR = "Plan to read"
    COMPLETED = "Completed"
    ESTADO = [
        (READING, "Reading"),
        (PTR, "Plan to read"),
        (COMPLETED, "Completed"),
    ]
    current_estado = models.CharField(
        max_length=50,
        choices=ESTADO,
        default=PTR,
    )

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Seinen"
        verbose_name_plural = "Seinen"
        ordering = ['title']


class Shounen(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)  
    title = models.CharField(max_length=100)
    japanese_title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    authors = models.CharField(max_length=100)
    publication_date = models.CharField(max_length=100)
    chapter = models.IntegerField(default=0)
    volume = models.IntegerField(default=0)  
    READING = "Reading"
    PTR = "Plan to read"
    COMPLETED = "Completed"
    ESTADO = [
        (READING, "Reading"),
        (PTR, "Plan to read"),
        (COMPLETED, "Completed"),
    ]
    current_estado = models.CharField(
        max_length=50,
        choices=ESTADO,
        default=PTR,
    )

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Shounen"
        verbose_name_plural = "Shounen"
        ordering = ['title']


class Manhwa(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)  
    title = models.CharField(max_length=100)
    korean_title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    authors = models.CharField(max_length=100)
    publication_date = models.CharField(max_length=100)
    chapter = models.IntegerField(default=0)
    volume = models.IntegerField(default=0)  
    READING = "Reading"
    PTR = "Plan to read"
    COMPLETED = "Completed"
    ESTADO = [
        (READING, "Reading"),
        (PTR, "Plan to read"),
        (COMPLETED, "Completed"),
    ]
    current_estado = models.CharField(
        max_length=50,
        choices=ESTADO,
        default=PTR,
    )

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Manhwa"
        verbose_name_plural = "Manhwa"
        ordering = ['title']


class Shoujo(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)  
    title = models.CharField(max_length=100)
    japanese_title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    authors = models.CharField(max_length=100)
    publication_date = models.CharField(max_length=100)
    chapter = models.IntegerField(default=0)
    volume = models.IntegerField(default=0)  
    READING = "Reading"
    PTR = "Plan to read"
    COMPLETED = "Completed"
    ESTADO = [
        (READING, "Reading"),
        (PTR, "Plan to read"),
        (COMPLETED, "Completed"),
    ]
    current_estado = models.CharField(
        max_length=50,
        choices=ESTADO,
        default=PTR,
    )

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Shoujo"
        verbose_name_plural = "Shoujo"
        ordering = ['title']


class Review(models.Model):
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    comment = models.TextField(null=True)
    NYS = "Not Yet Scored"
    A = "1"
    H = "2"
    VB = "3"
    B = "4"
    AV = "5"
    F = "6"
    G = "7"
    VG = "8"
    GR = "9"
    MP = "10"
    SCORE = [
        (NYS, "Not Yet Scored"),
        (A, "1 (Apalling)"),
        (VB, "2 (Horrible)"),
        (VB, "3 (Very Bad)"),
        (B, "4 (Bad)"),
        (AV, "5 (Avarage)"),
        (F, "6 (Fine)"),
        (G, "7 (Good)"),
        (VG, "8 (Very Good)"),
        (GR, "9 (Great)"),
        (MP, "10 (Masterpiece)"),
    ]
    rating = models.CharField(
        max_length=50,
        choices=SCORE,
        default=NYS,
    )

    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['username']


class Manga(models.Model): 
    title = models.CharField(max_length=100)
    chapter = models.IntegerField(default=0)
    volume = models.IntegerField(default=0)   
    READING = "Reading"
    PTR = "Plan to read"
    COMPLETED = "Completed"
    ESTADO = [
        (READING, "Reading"),
        (PTR, "Plan to read"),
        (COMPLETED, "Completed"),
    ]
    current_estado = models.CharField(
        max_length=50,
        choices=ESTADO,
        default=PTR,
    )

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Manga"
        verbose_name_plural = "Manga"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatars")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"

