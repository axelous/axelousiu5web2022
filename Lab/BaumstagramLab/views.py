# Обработчики или контроллеры приложения.
# Обработка запросов, решение что нужно делать и отправка ответа пользователю.
# Бизнес-логика - здесь
from django.shortcuts import render
from datetime import date
from BaumstagramLab.models import Photos, Accounts, Users

# tmp_data = { 'photos' : [
#          {'title': 'Я на Кубке', 'id': 1, 'img': 'images/1.jpg', 'des': 'Вот тут я был на кубке','date': '30.12.2017'},
#         {'title': 'Мы на Кубке', 'id': 2, 'img': 'images/2.jpg', 'des': 'А это - наша команда на кубке', 'date': '14.02.2018'},
#         {'title': 'Сам кубок', 'id': 3, 'img': 'images/3.jpg', 'des': 'Это - сам кубок', 'date': '14.02.2018'}
# ]
# }

def Welcome(request):
    return render(request, 'index.html', { 'data': {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})

# def GetPics(request):
#     return render(request, 'pics.html', {'data': {
#         'current_date': date.today(),
#         'pics': Photos.objects.all()
#     }})

def GetPic(request, id):
    return render(request, 'pic.html', {'data': {
        'current_date': date.today(),
        'pic': Photos.objects.filter(idphoto=id)[0]
    }})

def GetUsers(request):
    return render(request, 'users.html', {'data': {
        'current_date': date.today(),
        'users': Users.objects.all()
    }})

def GetUser(request, idd):
    return render(request, 'pics.html', {'data': {
        'current_date': date.today(),
        'account': Accounts.objects.all(),
        'pics': Photos.objects.all(),
        'idd': idd
    }})
