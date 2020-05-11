from django.shortcuts import render
from .models import User


# Create your views here.
def user_output_data_view(request, *args, **kwargs):
    obj = User.objects.all()

    context = {
        "obj": obj
    }
    return render(request, "User/data_output.html", context)
