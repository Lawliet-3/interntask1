from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import DataEntry

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
        
        messages.error(request, 'Please fill all required fields.')
    
    return render(request, 'entries/entry_form.html')

def toggle_review(request, entry_id):
    if request.method == 'POST':
        entry = DataEntry.objects.get(id=entry_id)
        entry.is_reviewed = not entry.is_reviewed
        entry.save()
        
        if request.headers.get('HX-Request'):
            return HttpResponse(
                f'<button class="btn btn-sm btn-{"success" if entry.is_reviewed else "secondary"}" '
                f'hx-post="/entries/{entry.id}/toggle-review/" '
                f'hx-swap="outerHTML">'
                f'{"Reviewed" if entry.is_reviewed else "Mark as Reviewed"}'
                f'</button>'
            )
        
        return redirect('entry_list')
