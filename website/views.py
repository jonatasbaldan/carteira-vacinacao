import requests
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.dateparse import parse_datetime

from website import utils
from website.models import ccv_pessoa, ccv_animal, ccv_agenda, ccv_vacinas


# Create your views here.

def home(request):
    if request.method == 'POST':
        return login_user(request)
    else:
        try:
            user_data = ccv_pessoa.objects.get(cpf=request.user.username)
            animais_data = ccv_animal.objects.filter(idpessoa=user_data)
            agendas_data = []
            for animal in animais_data:
                agendas = ccv_agenda.objects.filter(idanimal=animal)
                for agenda in agendas:
                    agendas_data.append(agenda)
            return render(request, 'home.html',
                          {'user_data': user_data, 'animals': animais_data, 'schedules': agendas_data})
        except:
            return render(request, 'home.html', {})


def login_user(request):
    cpf = request.POST['cpf']
    password = request.POST['password']
    response = requests.get(utils.URLS.get('pessoa'),
                            json={'token': utils.TOKEN,
                                  'empresa': utils.EMPRESA,
                                  'cpf': cpf})

    if response.status_code == 200:
        user = response.json()
        if len(user['pessoa']) > 0:
            if not cpf_exists(cpf):
                new_user = User.objects.create_user(cpf, '', '1234')
                name = user['pessoa'][0]['nome_razao']
                new_user.first_name = name
                new_user.save()
                populate_database(user['pessoa'][0], cpf)

    user = authenticate(request, username=cpf, password=password)

    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, "Cpf ou senha incorretos.", extra_tags='alert-warning')
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def cpf_exists(cpf):
    return User.objects.filter(username=cpf).exists()


def populate_database(user, cpf):
    populate_pessoa(user, cpf)
    populate_animal(user)


def populate_pessoa(user, cpf):
    pessoa = ccv_pessoa.objects.create()
    pessoa.id = user['id_pessoa']
    pessoa.pessoa = user['nome_razao']
    pessoa.telefone = ''
    pessoa.cpf = cpf
    pessoa.save()


def populate_animal(user):
    user_id = user['id_pessoa']
    request = requests.get(utils.URLS.get('animais'),
                           json={'token': utils.TOKEN,
                                 'empresa': utils.EMPRESA,
                                 'id': user_id})

    if request.status_code == 200:
        animais = request.json()
        for animal in animais['pessoa']:
            id_animal = animal['idanimal']
            id_pessoa = ccv_pessoa.objects.get(id=user_id)
            raca = animal['raca']
            nome_animal = animal['nomeanimal']
            dt_nascimento = parse_datetime(animal['dt_nascimento'])

            new_animal = ccv_animal.objects.create(id=id_animal,
                                                   idpessoa=id_pessoa,
                                                   raca=raca,
                                                   nomeanimal=nome_animal,
                                                   dt_nascimento=dt_nascimento
                                                   )
            populate_agenda(new_animal)


def populate_agenda(animal):
    request = requests.get(utils.URLS.get('agenda'),
                           json={'token': utils.TOKEN,
                                 'empresa': utils.EMPRESA,
                                 'idanimal': animal.id})

    if request.status_code == 200:
        agendas = request.json()
        for agenda in agendas['pessoa']:
            id = agenda['idagenda']
            id_animal = animal
            populate_vacina(agenda['idvacina'])
            id_vacina = ccv_vacinas.objects.get(id=agenda['idvacina'])
            dt_agenda = parse_datetime(agenda['dt_agenda'])
            situacao = agenda['situacao']
            ccv_agenda.objects.create(id=id,
                                      idanimal=id_animal,
                                      idvacina=id_vacina,
                                      dt_agenda=dt_agenda,
                                      situacao=situacao)


def populate_vacina(id_vacina):
    try:
        ccv_vacinas.objects.get(id=id_vacina)

    except:
        request = requests.get(utils.URLS.get('vacina'),
                               json={'token': utils.TOKEN,
                                     'empresa': utils.EMPRESA,
                                     'idvacina': id_vacina})

        if request.status_code == 200:
            vacina = request.json()
            vacina = vacina['pessoa'][0]
            nome = vacina['vacina_nome']
            valor = vacina['valor']
            ccv_vacinas.objects.create(id=id_vacina, vacina_nome=nome, valor=valor)
