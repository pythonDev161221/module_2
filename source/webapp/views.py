from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from webapp.models import Announce


class AnnounceListView(ListView):
    model = Announce


def index_view(request):
    return render(request, "index.html")
