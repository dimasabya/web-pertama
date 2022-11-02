from django.shortcuts import render

# Create your views here.
def index(request):
    context= {
        'judul': 'Blog',
        'heading': 'Blog Django',
        'subheading': 'silahkan baca baca di halaman blog ini'
    }
    return render(request, 'blog/index.html', context)