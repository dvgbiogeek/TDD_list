from django.http import HttpResponse
from django.shortcuts import render

from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        # .objects.create() creates a new Item without calling .save()
        Item.objects.create(text=new_item_text)
    else:
        new_item_text = ''

    return render(request, 'home.html', {
        'new_item_text': new_item_text,
        })
