from django.shortcuts import render
from .forms import SearchForm, AddInfos
from .models import Aliment, UpdateDate
from datetime import datetime, date


def index(request):
    """index view function

    Args:
        request (request): renders the index.html template
    """
    form = SearchForm()
    add_form = AddInfos()
    context = {"form": form, "add_form": add_form}
    return render(request, "index.html", context)


def get_infos(request):
    """returns aliment info

    Args:
        request (GET request): request form index data
    """
    if request.method == "GET":
        now = datetime.now()
        add_form = AddInfos()

        form = SearchForm()
        actions = []
        aliments = []
        data = request.GET.get("stockreading")
        try:
            res = Aliment.objects.get(stockreading=data)
            action = UpdateDate.objects.create(aliment_ref=res, updated_at=now)
            aliments.append(res)
        except:
            aliments = []

        history = UpdateDate.objects.filter(aliment_ref=res)
        for i in history:
            actions.append(i)

        context = {
            "aliments": aliments,
            "form": form,
            "actions": actions,
            "add_form": add_form,
        }
        return render(request, "index.html", context)


def get_all(request):
    """returns all aliments codes

    Args:
        request (GET request): request form index data
    """
    if request.method == "GET":
        add_form = AddInfos()
        form = SearchForm()
        res = Aliment.objects.all()
        stockreading_list = []
        for i in res:
            stockreading_list.append(i.stockreading)
        context = {
            "stockreading_list": stockreading_list,
            "form": form,
            "add_form": add_form,
        }
        return render(request, "index.html", context)


def get_past(request):
    """returns aliment pasts codes

    Args:
        request (GET request): request form index data
    """
    if request.method == "GET":
        form = SearchForm()
        add_form = AddInfos()
        day = date.today()
        res = Aliment.objects.filter(expires_at__lte=day)
        expired_list = []
        for i in res:
            expired_list.append(i)
        context = {
            "expired_list": expired_list,
            "form": form,
            "add_form": add_form,
        }
        return render(request, "index.html", context)


def add_infos(request):
    """Adding stockreading infos function"""
    if request.method == "POST":
        add_form = AddInfos()
        form = SearchForm()
        name = request.POST['name']
        description = request.POST['description']
        stockreading = request.POST['stockreading']
        expires_at = request.POST['expires']
        created_at = datetime.now()
        try:
            Aliment.objects.create(
                name=name,
                description=description,
                created_at=created_at,
                stockreading=stockreading,
                expires_at=expires_at,
            )
        except:
            print("SAVE ERROR")
        context = {"form": form, "add_form": add_form}
        return render(request, "index.html", context)
