from django.shortcuts import render
from django.http import Http404, JsonResponse, HttpResponse
import json

from .models import Item, Option

# Create your views here.
class JsonInputHandler:

    @classmethod
    def post_input(cls, request):
        return HttpResponse(status=500)

    @classmethod
    def get_input(cls, request):
        return HttpResponse(status=403)

    @classmethod
    def run(cls, request):
        print(request)
        if request.method == 'POST':
            return cls.post_input(request)
        else:
            return cls.get_input(request)

class ApiItemListHandler(JsonInputHandler):

    @classmethod
    def post_input(cls, request):
        data_list = list(Item.objects.all().values())
        options_dict = {}
        options_dict['data'] = data_list
        return JsonResponse(options_dict)

class ApiItemHandler(JsonInputHandler):

    @classmethod
    def post_input(cls, request):
        data = json.loads(request.body)
        item_id = data.get('id', -1)
        print(item_id)
        print(type(item_id))
        if type(item_id) == int and item_id > 0:
            try:
                item = Item.objects.get(pk=item_id)
                print(item)
            except Item.DoesNotExist:
                raise Http404(f"Can not find Item with id: {item_id}")
            option_list = list(Option.objects.all().values())
            options_dict = {}
            options_dict['item'] = item.__dict__()
            options_dict['option'] = option_list
            print(options_dict)
            return JsonResponse(options_dict)
        else:
            return HttpResponse(status=400)
