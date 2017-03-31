from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from au_search.models import Part

# Create your views here.
def home_view(request):
    return render(request, 'au_search/home.html')

PAGE_SIZE = 10

def search_view(request):
    keyword = request.GET.get('keyword','')
    page_index = int(request.GET.get('page', 1))
    if keyword != '':

        found_parts = Part.objects.filter(part_id__startswith=keyword)
        total_found = found_parts.count()

        p = Paginator(found_parts, PAGE_SIZE)

        current_page = p.page(page_index)
        page_range = p.page_range

        has_next = current_page.has_next()
        has_previous = current_page.has_previous()
        
        page_parts = current_page.object_list

        context_dic = {
                'keyword': keyword,
                'page_parts': page_parts,
                'total_found': total_found,
                'page_range': page_range,
                'current_page': current_page,
                'active_page_index': page_index,
                }
        return render(request, 'au_search/search.html', context=context_dic)
    else:
        return redirect('/')
