from django.shortcuts import render
from .models import User
from .forms import user_form

# Create your views here.
def user_output_data_view(request, *args, **kwargs):
    obj = User.objects.all()

    context = {
        "obj": obj
    }
    return render(request, "User/data_output.html", context)

def user_input_data_view(request, *args, **kwargs):
    form=user_form(request.POST or None,request.FILES)
    if form.is_valid():
        form.save()
        form=user_form()
    context={
        "form": form,
    }

    return render(request, "User/data_input.html", context)
