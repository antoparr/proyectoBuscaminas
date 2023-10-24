from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import tableForm
from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(req):
    return render(req, 'ActBuscaminas/index.html')


def form_tablero(request):
    if request.method == "GET":
        table_form = tableForm(request.GET)
        table_form_v = tableForm()
        if table_form.is_valid():
            columna = int(table_form.cleaned_data['columna'])
            fila = int(table_form.cleaned_data['fila'])

            filas_list = range(fila)
            columnas_list = range(columna)

            return render(request, 'ActBuscaminas/tablero.html',
                          {'columna': columnas_list, "fila": filas_list, "tableForm": table_form})
    else:
        table_form = tableForm()

    return render(request, 'ActBuscaminas/tablero.html', {'tableForm': table_form})

