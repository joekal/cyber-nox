from django.db import models
from django.utils.html import format_html

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('CYBER', 'Cybersécurité'),
        ('DEV', 'Développement Digital'),
    ]
    title = models.CharField(max_length=200, verbose_name="Titre du service")
    description = models.TextField(verbose_name="Description")
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, verbose_name="Catégorie")
    icon_name = models.CharField(max_length=50, help_text="Nom de l'icône Phosphor")

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre du projet")
    client_name = models.CharField(max_length=200, blank=True, verbose_name="Client")
    description = models.TextField()
    category_tag = models.CharField(max_length=50, verbose_name="Tag (ex: Web)")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    result_text = models.CharField(max_length=100, verbose_name="Résultat (KPI)")
    
    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="Co-Fondateur")
    bio = models.TextField(blank=True)
    certifications = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom du client")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Sujet")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Reçu le")
    
    # Nouveau champ pour le suivi
    is_replied = models.BooleanField(default=False, verbose_name="Répondu ?")

    class Meta:
        verbose_name = "Message Client"
        verbose_name_plural = "Boîte de Réception"
        ordering = ['-created_at'] # Les plus récents en premier

    def __str__(self):
        return f"{self.name} - {self.subject}"
