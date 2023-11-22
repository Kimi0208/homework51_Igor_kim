from django.shortcuts import render
from hello.cat_controller import CatDB


def cat_info(request):
    print(request.method)
    if request.method == 'POST':
        CatDB.name = request.POST.get('name')
        cat_stat = CatDB.to_dict()
        return render(request, template_name='play.html', context=cat_stat)
    elif request.method == 'GET':
        if request.GET.get('select') is not None:
            CatDB.choose_action(request.GET.get('select'))
            cat_stat = CatDB.to_dict()
            return render(request, template_name='play.html', context=cat_stat)


def start(request):
    return render(request, template_name='start.html')
