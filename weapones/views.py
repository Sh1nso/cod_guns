from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

list_of_weapones = ['Automatic Rifle', 'SMG', 'Shotgun', 'Tactical Rifle', 'Sniper Scope', 'Pistols']



dict_of_automatic_rifle = {
    '1': 'Т22',
    'b3': 'Т22',
    'a4': 'Т22',
    '4': '55',
    'm44': '55',
    }

dict_of_smgs = {
    'marco5': 'Тут будут ссылки на все обвесы для Марко 5',
    'blinxen': 'Тут будут ссылки на все обвесы для Blixen',
    'armoguera': 'Тут будут ссылки на все обвесы для Armoguera',
    'ots9': 'Тут будут ссылки на все обвесы для OTS 9',
    'mp5': 'Тут будут ссылки на все обвесы для MP5',
    }

dict_of_shotguns = {
    '1': 'Т22',
    'b3': 'Т22',
    'a4': 'Т22',
    '4': '55',
    'm44': '55',
    }

dict_of_tactical_rifle = {
    '1': 'Т22',
    'b3': 'Т22',
    'a4': 'Т22',
    '4': '55',
    'm44': '55',
    }

dict_of_snipers = {
    '1': 'Т22',
    'b3': 'Т22',
    'a4': 'Т22',
    '4': '55',
    'm44': '55',
    }

dict_of_pistols = {
    '1': 'Т22',
    'b3': 'Т22',
    'a4': 'Т22',
    '4': '55',
    'm44': '55',
    }

dict_of_weapones = {
    #'Automatic Rifle': dict_of_automatic_rifle,
    'SMG' : ['marco5', 'blinxen', 'armoguera', 'ots9', 'mp5'],
    #'Shotgun': dict_of_shotguns,
    #'Tactical Rifle': dict_of_tactical_rifle,
    #'Sniper Scope' : dict_of_snipers,
    #'Pistols' : dict_of_pistols

}

def main_menu(request):
    rez = ''
    for i in dict_of_weapones:
        redirect_path = reverse('weapon-name', args=[i])
        rez += f'<li> <a href="{redirect_path}"> {i.title()} </a> </li>'
    return HttpResponse(f'<ol>{rez}</ol>')

def get_info_about_type_of_weapone(request, some_weapone: str):
    name_of_weapone = dict_of_weapones.get(some_weapone,None)
    rez = ''
    if name_of_weapone:
        for i in dict_of_weapones[some_weapone]:
            redirect_path = reverse('smg-name', args=[i])
            rez += f'<li> <a href="{redirect_path}"> {i.title()} </a> </li>'
        return HttpResponse(rez)
    else:
        return HttpResponseNotFound(f'Неизвестная SMG - {some_weapone.upper()}')


def get_info_about_some_smg(request, some_smg: str):
    description = dict_of_smgs.get(some_smg, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f'Неизвестная SMG - {some_smg.upper()}')

def get_info_about_some_smg_by_number(request, some_smg: int):
    number_smgs = list(dict_of_smgs.keys())
    if some_smg > len(number_smgs):
        return HttpResponseNotFound(f'Не верный номер - {some_smg}')
    name_smg = number_smgs[some_smg-1]
    redirect_url = reverse('smg-name', args=(name_smg, ))
    return HttpResponseRedirect(redirect_url)
