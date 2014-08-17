from django.shortcuts import render, redirect

from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        # .objects.create() creates a new Item without calling .save()
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    # else:
    #     new_item_text = ''

    return render(request, 'home.html')
