from django.shortcuts import render, redirect
from .models import Record, Menu
from .tts import menu_teller, menu_crawling_teller
import time

def return_speech(request):
    record_list = Record.objects.all()
    context = {'record_list': record_list}
    return render(request, "speech.html", context)
# Create your views here.

def tts_create(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        record = Record.objects.create(title=request.POST.get('title'), text=text, file_url='')
        menu_teller(record.id, text)
        record.file_url = "/static/file/record_" + str(record.id) + ".mp3"
        record.save()
    record_list = Record.objects.all()
    context = {'record_list': record_list}
    return redirect('tts')

def menu_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        menu = Menu.objects.create(title=request.POST.get('title'), file_url='')
        menu_crawling_teller(menu.id)
        time.sleep(10)
        menu.file_url = "/static/file/menu_" + str(menu.id) + ".mp3"
        menu.save()
    menu_list = Menu.objects.all()
    context = {'menu_list': menu_list}
    return redirect('menu_tts')

def return_menu(request):
    menu_list = Menu.objects.all()
    context = {'menu_list': menu_list}
    return render(request, "menu.html", context)
