from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'au_search/home.html')

def search_view(request):
    return render(request, 'au_search/search.html')
