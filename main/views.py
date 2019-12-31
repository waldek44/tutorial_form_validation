from .forms import PostForm
from django.shortcuts import HttpResponse, render


def home(request):
    if request.method == 'POST':
        # Pass the form data to the form class
        details = PostForm(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            return HttpResponse("świetnie! zapisało ci to w db")

        else:
            return render(request, "home.html", {'form': details})
    else:
        form = PostForm(None)
        return render(request, 'home.html', {'form': form})
