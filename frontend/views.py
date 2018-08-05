from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def segmentation(request):
    return render(request, 'segmentation.html')


def collocation(request):
    return render(request, 'collocation.html')


def concordance(request):
    return render(request, 'concordance.html')


def wordcloud(request):
    return render(request, 'wordcloud.html')


def sentipol(request):
    return render(request, 'sentipol.html')


def apidoc(request):
    return render(request, 'apidoc.html')
