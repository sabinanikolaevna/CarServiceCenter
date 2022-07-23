from django.http.response import HttpResponse
from django import shortcuts
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http.request import HttpRequest


oil = []
tires = []
diagnosics = []
all = []



def change_oil(request):
    number = int(len(oil))
    time = number * 2
    oil.append(f'{number+1}')
    all.append(number + 1)
    return HttpResponse(f'<div>Your number is {number + 1}</div><div>Please wait around {time} minutes</div>')


def tiress(request):
    n_oil = int(len(oil))
    n_tires = int(len(tires))
    time = n_oil * 2 + n_tires * 5
    number = n_oil + n_tires
    tires.append(f'{int(len(all))+1}')
    all.append(number + 1)
    return HttpResponse(f'<div>Your number is {number + 1}</div><div>Please wait around {time} minutes</div>')


def diag(request):
    n_oil = int(len(oil))
    n_tires = int(len(tires))
    n_diag = int(len(diagnosics))
    time = n_oil * 2 + n_tires * 5 + n_diag * 30
    number = n_oil + n_tires + n_diag
    diagnosics.append(f'{int(len(all))+1}')
    all.append(number + 1)
    return HttpResponse(f'<div>Your number is {number + 1}</div><div>Please wait around {time} minutes</div>')



def welcome(request):
    return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')

def menu(request):
    return render_to_response('menu.html')

def processing(request):
    data = {'x':  len(oil), 'y': len(tires), 'z': len(diagnosics)}
    return render(request, 'processing.html', context=data)

def next(response):
    if len(all) != 0:
        n = all[0]
        all.pop(0)
        return HttpResponse(f'<div>Ticket #{n}</div>')
    return HttpResponse('<div>Waiting for the next client</div>')



