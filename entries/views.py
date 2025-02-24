from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import DataEntry
from django.urls import reverse

def entry_list(request):
    category_filter = request.GET.get('category')
    search_query = request.GET.get('search')
    
    entries = DataEntry.objects.all()
    
    if category_filter:
        entries = entries.filter(category=category_filter)
    
    if search_query:
        entries = entries.filter(content__icontains=search_query)
    
    # Pagination
    paginator = Paginator(entries, 10)  # Show 10 entries per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Category statistics
    category_stats = DataEntry.objects.values('category').annotate(count=Count('id'))
    
    context = {
        'page_obj': page_obj,
        'category_stats': category_stats,
        'category_filter': category_filter,
        'search_query': search_query,
    }
    return render(request, 'entries/entry_list.html', context)

def entry_create(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        category = request.POST.get('category')
        
        if content and category:
            DataEntry.objects.create(
                content=content,
                category=category
            )
            messages.success(request, 'Entry created successfully!')
            return redirect('entry_list')
        else:
            messages.error(request, 'Please fill all required fields.')
    
    return render(request, 'entries/entry_form.html')

def entry_detail(request, entry_id):
    entry = get_object_or_404(DataEntry, id=entry_id)
    return render(request, 'entries/entry_detail.html', {'entry': entry})

def toggle_review(request, entry_id):
    if request.method == 'POST':
        entry = get_object_or_404(DataEntry, id=entry_id)
        entry.is_reviewed = not entry.is_reviewed
        entry.save()
        
        if request.headers.get('HX-Request'):
            csrf_token = request.COOKIES.get('csrftoken', '')
            button_class = 'success' if entry.is_reviewed else 'secondary'
            button_text = 'Reviewed' if entry.is_reviewed else 'Mark as Reviewed'
            
            button_html = f'''
                <button class="btn btn-sm btn-{button_class}"
                    hx-post="{reverse('toggle_review', args=[entry.id])}"
                    hx-swap="outerHTML"
                    hx-headers='{{"X-CSRFToken": "{csrf_token}"}}'>
                    {button_text}
                </button>
            '''
            
            return HttpResponse(button_html.strip())
        
        return redirect(request.META.get('HTTP_REFERER', 'entry_list'))
    return HttpResponse(status=405)
def entry_detail(request, entry_id):
    entry = get_object_or_404(DataEntry, id=entry_id)
    return render(request, 'entries/entry_detail.html', {'entry': entry})
