from django.shortcuts import render
from myapp.forms import MenuForm
from .models import Menu
from django.http import JsonResponse

# Add code for form_view() function below

def form_view(request):
    form = MenuForm()
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            # clean form
            cd = form.cleaned_data
            # menu fields
            mf = Menu(
                item_name=cd['item_name'],
                category=cd['category'],
                description=cd['description'],
            )
            mf.save()

            # JSON response
            return JsonResponse({
                "message" : "success"
            })
    return render(request, "menu_items.html", {"form": form})