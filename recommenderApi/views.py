from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from recommenderApi.recommender_model import load_model, predict
from recommenderApi.helpers import filterData, filterResult, extractDataFromInput
# Create your views here.


def get_recommendations(request):
    if request.method == 'POST':
        info = extractDataFromInput(request.GET)
        product_history = request.GET.getlist('product_history') if 'product_history' in request.GET else []
        filteredData = filterData(info, product_history, {})
        model = load_model()
        result = predict(model, filteredData)
        filteredResult = filterResult(result, info['ncodpers'])
        return JsonResponse({'data': filteredResult})
    else:
        return HttpResponseNotFound('Method Not Supported')
