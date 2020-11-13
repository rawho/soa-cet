from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.mail import send_mail

# Create your views here.

def index(request):
    artists = Artist.objects.all()
    images = Image.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        artist = request.POST['artist']
        subject = f'I want to Buy An Art from {name}'
        message_body = f'Hello {artist}, \nI liked your art listed in the soacet website. I like to buy it from you \n\nDetails: \nName: {name} \nPhone No: {phone} \nEmail: {email}'

        # send email
        send_mail(
            subject, #subject
            message_body, #message
            email, #from email
            ['info.soacet@gmail.com', artist], #to email
        )
        send_mail(
            'We received your email - SOACET', #subject
            f'Thank you {name}, \n \t\t we received your email. we will get back to you soon', #message
            'info.soacet@gmail.com', #from email
            [email], #to email
        )

        return render(request, 'website/index.html', {
            'name' : name,
            'artists' : artists,
            'images' : images
        })
    else:
        return render(request, 'website/index.html', {
            'artists' : artists,
            'images' : images,
        })

    
def artist_detail(request, pk, slug):
    artist = Artist.objects.get(id=pk)
    images = artist.image_set.all()
    # images = image.filter(artist=artist)
    return render(request, 'website/artist_detail.html',{
        'artist' : artist,
        'images' : images
    })
