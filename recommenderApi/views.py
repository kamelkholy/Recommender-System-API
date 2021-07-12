from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.crypto import get_random_string
from recommenderApi.recommender_model import load_model, predict
from recommenderApi.helpers import filterData, filterResult
# Create your views here.


def get_recommendations(request):
    info = {
        'fecha_dato': '2016-06-28',
        'ncodpers': get_random_string(8),
        'age': '56',
        'sexo': 'V',
        'pais_residencia': 'ES',
        'antiguedad': '256',
        'ind_actividad_cliente': '1',
        'segmento': '01 - TOP',
        'renta': '326124.90',
        'tiprel_1mes': 'A',
        'indfall': 'N',
        'tipodom': '1',
        'ind_empleado': 'F',
        'canal_entrada': '',
        'ind_nuevo': '',
        'indrel': '',
        'indrel_1mes': '1',
        'indresi': '',
        'indext': '',
        'conyuemp': ''
    }

    filteredData = filterData(info, {})
    model = load_model()

    result = predict(model, filteredData)
    filteredResult = filterResult(result, info['ncodpers'])
    return JsonResponse({'data': filteredResult})
