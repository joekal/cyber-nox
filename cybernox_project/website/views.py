from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from .models import Service, TeamMember, Project, ContactMessage

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject') or 'Message depuis le site'

        # Enregistrer le message en base
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Préparer le contenu de l'email
        email_subject = f"Cyber-Nox - Nouveau message: {subject}"
        email_body = (
            f"Vous avez reçu un nouveau message depuis le formulaire de contact.\n\n"
            f"Nom: {name}\n"
            f"Email: {email}\n"
            f"Sujet: {subject}\n\n"
            f"Message:\n{message}\n"
        )

        recipient = 'kalalajonathan297@gmail.com'
        from_email = getattr(settings, 'EMAIL_HOST_USER', None) or None
        
        try:
            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=from_email,
                recipient_list=[recipient],
                fail_silently=False,
            )
        except BadHeaderError:
            messages.error(request, "Envoi du message impossible (en-tête invalide).")
            return redirect('home')
        except Exception:
            # En cas d'erreur d'envoi, on affiche un message d'erreur mais on conserve l'enregistrement
            messages.error(request, "Une erreur est survenue lors de l'envoi de l'email. Vérifiez la configuration.")
            return redirect('home')

        messages.success(request, "Votre message a été envoyé avec succès !")
        return redirect('home')

    context = {
        'services_cyber': Service.objects.filter(category='CYBER'),
        'services_dev': Service.objects.filter(category='DEV'),
        'projects': Project.objects.all()[:3], # On affiche les 3 derniers projets
        'team_members': TeamMember.objects.all(),
    }
    return render(request, 'website/index.html', context)