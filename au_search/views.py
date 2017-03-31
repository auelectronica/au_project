from django.shortcuts import render
from django.shortcuts import redirect
from au_search.models import Part

# Create your views here.
def home_view(request):
    return render(request, 'au_search/home.html')

def search_view(request):
    keyword = request.GET.get('keyword','')
    if keyword != '':
        found_parts = Part.objects.filter(part_id__startswith=keyword)[:10]
        total_found = Part.objects.filter(part_id__startswith=keyword).count()
        context_dic = {
                'keyword': keyword,
                'found_parts': found_parts,
                'total_found': total_found,
                }
        return render(request, 'au_search/search.html', context=context_dic)
    else:
        return redirect('/')
