from django.contrib import admin
from django.utils.html import format_html
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Service, Project, TeamMember, ContactMessage

# Configuration du titre de l'admin
admin.site.site_header = "Administration CYBER-NOX"
admin.site.site_title = "Portail Admin Cyber-Nox"
admin.site.index_title = "Tableau de bord de gestion"

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ('name', 'subject', 'email_link', 'created_at', 'status_icon')
    # Filtres sur la droite
    list_filter = ('is_replied', 'created_at')
    # Barre de recherche
    search_fields = ('name', 'email', 'subject', 'message')
    # Champs en lecture seule (pour ne pas modifier le message du client par erreur)
    readonly_fields = ('created_at', 'name', 'email', 'subject', 'message')
    
    # Action groupée : "Marquer comme répondu"
    actions = ['mark_as_replied', 'send_quick_acknowledgement']

    def email_link(self, obj):
        """Crée un lien cliquable pour ouvrir le logiciel de mail par défaut"""
        return format_html('<a href="mailto:{}?subject=RE: {}">{}</a>', obj.email, obj.subject, obj.email)
    email_link.short_description = "Envoyer un mail"

    def status_icon(self, obj):
        """Affiche une icône visuelle pour le statut"""
        if obj.is_replied:
            return format_html('<span style="color: green;">✔ Traité</span>')
        return format_html('<span style="color: red;">⏳ En attente</span>')
    status_icon.short_description = "Statut"

    # --- ACTIONS PERSONNALISÉES ---

    @admin.action(description="Marquer comme traité/répondu")
    def mark_as_replied(self, request, queryset):
        queryset.update(is_replied=True)
        self.message_user(request, "Les messages sélectionnés ont été marqués comme traités.")

    @admin.action(description="Envoyer un accusé de réception par Email")
    def send_quick_acknowledgement(self, request, queryset):
        """Envoie un mail type automatique"""
        count = 0
        for msg in queryset:
            if not msg.is_replied:
                try:
                    send_mail(
                        subject=f"CYBER-NOX : Bien reçu - {msg.subject}",
                        message=f"Bonjour {msg.name},\n\nNous avons bien reçu votre demande concernant '{msg.subject}'.\nNotre équipe va l'analyser et revenir vers vous sous 24h.\n\nCordialement,\nL'équipe CYBER-NOX.",
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[msg.email],
                        fail_silently=False,
                    )
                    msg.is_replied = True
                    msg.save()
                    count += 1
                except Exception as e:
                    self.message_user(request, f"Erreur d'envoi à {msg.email}: {e}", level=messages.ERROR)
        
        if count > 0:
            self.message_user(request, f"{count} emails de confirmation envoyés avec succès.")

# Enregistrement simple des autres modèles
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client_name', 'category_tag')

admin.site.register(TeamMember)