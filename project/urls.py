from django.contrib import admin
from django.urls import path, include

"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
O protocolo HTTP é um protocolo que a gente geralmente utiliza para navegar na
internet ou para trafegar coisas da internet.
Funcionamento do protocolo http:
    O cliente vai e faz um HTTP REQUEST e o servidor retorna para ele um
    HTTP RESPONSE.

  Errada:
HTTP REQUEST
def my_view(request):
    ...
HTTP RESPONSE

  Correto:
def my_view(request):
    return HttpResponse('UMA LINDA STRING')

/////////////////////////########/////////////////////////
def home(request):
    return HttpResponse('HOME')


def sobre(request):
    return HttpResponse('sobre')


def contato(request):
    return HttpResponse('contato')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Quando não temos nada entre aspas, temos a raiz do
    site(página inicial)

    path('sobre/', sobre),  # /sobre/ -> a / antes de sobre significa o
    domínio que já temos.

    path('contato/', contato)  # /contato/
]


O código acima fica insustentável, pois como podemos ver para cada o URL
teremos que ter uma função, e essas funções geralmente não vão ser muito
pequenas. Então teremos que fazer determinadas lógicas, fazer alguma coisa
dentro do nosso 'view', no qual vai crescer um pouquinho, que vai ter
mais algumas linhas dentro das funções. Ou seja, imaginamos que temos umas 100
rotas, teriamos umas 100 path no 'urlpatterns = [...]' e umas 100 funções no
mesmo arquivo. Então isso é inviável. Então o Django permite que a gente crie
app's. Ou seja, é possível criar pastas para determinadas funções, por exemplo,
para a pasta inicial (home), teriamos uma pasta home, para o contato, teriamos
uma pasta contato,...No nosso caso aqui a gente não vai separar as coisas, pois
a Home, Contato e Sobre seriam coisas do mesmo site. Então vamos criar somente
um 'app' para a gente poder ter um app separado do coração do Django.

def home(request):
    return HttpResponse('HOME')


def sobre(request):
    return HttpResponse('sobre')


def contato(request):
    return HttpResponse('contato')



OBSERVAÇÃO: Pode copiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Quando não temos nada entre aspas, temos a raiz do
    # site(página inicial)
    path('sobre/', sobre),  # /sobre/ -> a barra(/) antes de sobre significa o
    # domínio que já temos.
    path('contato/', contato)  # /contato/
]

essas coisas para outro lado, pois no Django tem um padrão
que é muito utilizado aqui para essas URLs acima que é fazer
uma URL ser filha de outra URL, que pode ter outras filhas
e que essas filhas podem ter outras filhas e assim por diante.
Podemos encaixar a URL dentro de um URL dentro de URL e assim
por diante. Ou seja, vamos copiar todo o "urlpatterns = []",
menos o comando : path('admin/', admin.site.urls), e vamos na
pasta "recipes" e criamos um novo arquivo chamado de o "urls.py",
ou seja, o mesmo nome do outro arquivo que existe aqui.

Podemos agora substituir esse o urlpatterns[...]:

from django.contrib import admin
from django.urls import path
from recipes.views import home, sobre, contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato)  # /contato/
]
em um comando mais simplificado para eu não ter essa duplicação de código.
Então a gente pode apagar o "from recipes.views import home, sobre, contato"
e apagar: "path('', home)","path('sobre/', sobre)","path('contato/', contato)",
e agora vamos incluir aqueles arquivos de recipes/urls. Assim, para incluir o
podemos usar uma função do Django chamada "include", então podemos importar
aqui:
    from django.urls import path, include

E essa função include recebe uma string, onde vamos indicar o nome do app e o
nome do arquivo que tem as URLs que é pra ele incluir. Então:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls'))
]

Beleza é basicamente assim que funciona isso aqui.

Agora será que isso vai funcionar.

Vamos testar vamos atualizar a página tudo funciona.
"""


# Resumindo a Aula 23:
"""
Começamos movendo as nossas views para dentro do arquivo recipes/views.
E a gente moveu também toda a URL pra dentro de um arquivo que nem existia que
é o urls.py que está dentro de recipes. Portanto, agora podemos trabalhar
isoladamente, inclusive a gente pode até separar cada uma das funções de view
para dentro do seu próprio arquivo também, no qual veremos isso mais pra frente
caso nosso site comece a ficar muito bagunçado com muito código aqui.
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls'))
]
