from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    desc = RichTextUploadingField()
    image = models.ImageField(upload_to='articles')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    

class region(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nom

class secteur(models.Model):
    nom = models.CharField(max_length=255)
    region =models.ForeignKey(region,on_delete=models.SET_NULL,blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nom
    
class eglise(models.Model):
    nom = models.CharField(max_length=255)
    effectif = models.IntegerField(null=True)
    region =models.ForeignKey(region,on_delete=models.SET_NULL,blank=True,null=True)
    secteur =models.ForeignKey(secteur,on_delete=models.SET_NULL,blank=True,null=True)
    lat = models.CharField(max_length=255,null=True)
    lng = models.CharField(max_length=255,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nom

class titre(models.Model):
    letitre = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.letitre
    
class rang(models.Model):
    rang = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.rang
    
class pasteur(models.Model):
    nom = models.CharField(max_length=255)
    eglise =models.ForeignKey(eglise,on_delete=models.SET_NULL,blank=True,null=True)
    titre =models.ForeignKey(titre,on_delete=models.SET_NULL,blank=True,null=True)
    rang =models.ForeignKey(rang,on_delete=models.SET_NULL,blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nom

class poste(models.Model):
    nom = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nom
    
class bureau(models.Model):
    region =models.ForeignKey(region,on_delete=models.SET_NULL,blank=True,null=True)
    secteur =models.ForeignKey(secteur,on_delete=models.SET_NULL,blank=True,null=True)
    eglise =models.ForeignKey(eglise,on_delete=models.SET_NULL,blank=True,null=True)
    pasteur =models.ForeignKey(pasteur,on_delete=models.SET_NULL,blank=True,null=True)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True)
    poste =models.ForeignKey(poste,on_delete=models.SET_NULL,blank=True,null=True)
    desc = models.TextField()
    image = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __int__(self) -> int:
        return self.pasteur
    
class motpresident(models.Model):
    title = models.CharField(max_length=100)
    desc = RichTextUploadingField()
    image = models.ImageField(upload_to='articles')
    bureau =models.ForeignKey(bureau,on_delete=models.SET_NULL,blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
class rectangles(models.Model):
    libele = models.CharField(max_length=100)
    X = models.IntegerField()
    Y = models.IntegerField()
    Largeur = models.IntegerField()
    Hauteur = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.libele