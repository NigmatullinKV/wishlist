from datetime import datetime

from django.shortcuts import render, get_object_or_404

from .models import WishList
from .forms import ProductForm


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {"title": "Wishlist | about project"})


def list_page(request, pk):
    """View page the wishlist."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form.create_at = datetime.now()
        form.save()
        print(form.pk, form.title)
    else:
        form = ProductForm()
        wishlist = get_object_or_404(WishList, pk=pk)

    return render(
        request,
        'wish_list.html',
        {
            'wishlist': wishlist,
            'is_owner_list': wishlist.owner == request.user,
            'form': form
        }
    )
