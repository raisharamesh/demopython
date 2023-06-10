from django.shortcuts import render
from django.db.models import Q
from shop.models import product

def SearchResult(request):
    query = request.GET.get('q', '')
    print(query)  # Add this line to check the value of the query
    products = product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'query': query, 'products': products})

