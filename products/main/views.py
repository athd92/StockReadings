from django.shortcuts import render
from .forms import SearchForm
from .models import Aliment, UpdateDate
from datetime import datetime, date


def index(request):
    """index view function

    Args:
        request (request): renders the index.html template
    """
    form = SearchForm()
    context = {"form": form}
    return render(request, "index.html", context)


def get_infos(request):
    """returns aliment info

    Args:
        request (GET request): request form index data
    """
    if request.method == "GET":
        now = datetime.now()
        form = SearchForm()
        actions = []
        aliments = []
        data = request.GET.get("stockreading")
        try:
            res = Aliment.objects.get(stockreading=data)
            action = UpdateDate.objects.create(
                aliment_ref=res, updated_at=now
            )
            aliments.append(res)
        except:
            aliments = []

        history = UpdateDate.objects.filter(aliment_ref=res)
        for i in history:
            actions.append(i)

        context = {"aliments": aliments, "form": form, "actions": actions}
        return render(request, "index.html", context)


def get_all(request):
    """returns all aliments codes

    Args:
        request (GET request): request form index data
    """
    if request.method == "GET":
        form = SearchForm()
        res = Aliment.objects.all()
        stockreading_list = []
        for i in res:
            stockreading_list.append(i.stockreading)
        context = {"stockreading_list": stockreading_list, "form": form}
        return render(request, "index.html", context)


def get_past(request):
    """returns aliment pasts codes

    Args:
        request (GET request): request form index data
    """
    if request.method == "GET":
        form = SearchForm()
        day = date.today()
        res = Aliment.objects.filter(expires_at__lte=day)
        expired_list = []
        for i in res:
            expired_list.append(i)
        context = {"expired_list": expired_list, "form": form}
        return render(request, "index.html", context)
