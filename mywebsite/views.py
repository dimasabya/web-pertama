from django.shortcuts import render

def index(request):
    context = {
        'judul': 'Web Pertama',
        'heading': 'Web Django',
        'subheading': 'Selamat Datang'
    }
    return render(request, 'index.html', context)