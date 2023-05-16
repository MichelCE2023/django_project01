# o trabalho de "render" e ler um arquivo e renderizar esse arquivo.
from django.shortcuts import render


"""
Aula 24:

A primeira coisa é falar para o "Django" retornar "render" e passamos
a função que "render" pede que é "request". E assim, ela vai renderizar
um template "home.html". Depois, dentro da pasta recipes, vamos criar uma
pasta chamada de "templates". Essa pasta de template do Django já é
inteligente o suficiente para buscar coisas que eu informar aqui dentro dela.
Por exemplo, home.html ele já vai buscar dentro dela diretamente, ou seja, ele
não vai buscar fora em outros locais, mas somente dentro dela. Então por isso,
que não precisamos falar a pasta que precisamos, falamos apenas o arquivo.
Então vamos lá dentro de templates e vamos criar o arquivo "home.html".

Depois de criar um template inicial (!) em home.html, esperamos ver um erro.
Assim, se atualizarmos a página aparece o erro "TemplateDoesNotExist". O Django
não sabe, ele não tem ciência, que a pasta recipes existe. Então como ele não
tem ciência que esse recipes existe ele não está buscando coisas dentro da
pasta templates desse recipes. Então, para informar para o Django que temos um
app chamado de recipes precisamos ir no caminho: project/setting.py, que é o
arquivo mestre, ou seja, o setting do Django. Nesse setting.py encontramos:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
Ou seja, os apps que já estão instalados no nosso Django.

Esses apps acima já vêm por padrão o "admin" que é a área administrativo que a
gente vai ver depois do Django, "auth" que é parte de autenticação de usuário,
"contenttypes" que são os tipos de conteúdo, "sessions que são sessões do
usuário. "messages" são mensagens, flash messages, que veremos depois, e
"staticfiles" que veremos depois também. Só que a gente temos que informar
para o Django que temos apps também, ou seja, temos que informar os apps que
vamos criar, por exemplo, o apps: "recipes". Se compilarmos o nosso HTML, agora
ele já está carregando o nosso HTML. Assim, automaticamente o Django já começou
a buscar coisas nas pastas padrão dele, então essa pasta templates aqui já
podemos assumir que é uma pasta padrão.

Se usarmos a configuração padrão que tem em project/setting.py/TEMPLATES=[],que
é a configuração que vem, ou seja, se usarmos essa configuração padrão que vem
com Django ele vai buscar automaticamente pra você na pasta templates todo o
HTML que colocarmos lá.

Mas isso pode trazer um transtorno grande até por conta do seguinte. Pode ser.
E isso vai acontecer inevitavelmente, pode ser que tenhamos uma outra
pasta chamada de "base_templates", que são arquivos de base que utilizamos, ou
seja, arquivos que podem ser estendidos (vamos aprender mais sobre isso nas
próximas aulas, mas supondo temos uma pasta chamada de base e nessa pasta
supomos que tenhamos um arquivo igual ao "home.html". Se fizermos isso aqui
podemos ir lá em setting.py/TEMPLATES conseguimos informar para o Django
pastas adicionais. Então, por exemplo, aqui colocamos numa pasta aleatória que
é a base_template que colocamos um arquivo HTML nessa pasta base_templates.
Então, agora temos que informar para o Django se eu quiser que ele busque aqui
templates, temos que informar para ele project/setting.py/TEMPLATES/DIR=[]
que é uma lista. No qual podemos colocar quantos caminhos quisermos. E para
facilitar a nossa vida o Django tem uma constante escrita no topo do arquivo
setting.py, que é chamada de BASE_DIR,
    BASE_DIR = Path(__file__).resolve().parent.parent
e esse comando resolver para o caminho deste arquivo:"Path(__file__).resolve()"
que no caso o caminho deste arquivo ele resolve, o "parent" desse arquivo que
seria a pasta "project" que no caso é o "parent" da pasta project.
Em resumo ele resolve pra raiz do nosso projeto aqui, então se usarmos esse
BASE_DIR, quer dizer que teremos acesso ao caminho completo da raiz do nosso
site. Portanto, podemos ir em TEMPLATES e usar isso ao nosso favor. Por
exemplo, queremos que ele adicione a pasta base_templates. Assim,
    'DIRS': [ BASE_DIR / 'base_templates',]

Após compilar apareceu no browser o nome BASE no lugar de "Recipes". Isso acon-
teceu porquê, como criamos um arquivo solto chamado de home.html na pasta
base_templates e no nosso apps "recipes" templates um outro arquivo também
chamado de home.html, o Django vai dar prioridade na ordem que tiver em
TEMPLATES/DIR[], ou seja, na ordem que ele encontrar primeiro. Então esses
dois arquivos home.html, como já falado aqui em views.py,

    def home(request):
    return render(request, 'home.html')

que eu quero que ele carregue o arquivo home.html, e aqui no caso para ele é
qualquer home.html que ele encontrar vai ser esse que ele vai usar. E isso a
gente chama de colisão de nomes no Django, ou seja, os nomes colidiram e o
Django vai usar um dos dois, e isso gera confusão, gera transtorno, gera erros
no projeto, e isso é muito ruim.

Então o que vamos fazer a partir de agora, nos vamos começar a dar um
name_space para os nossos arquivos de template. Como assim, no name_space?
Vimos que jogamos dentro da pasta templates o arquivo direto home.html, assim
ao invés de fazer isso, nós vamos criar uma outra pasta chamada de recipes
dentro da pasta recipes, pois estamos nos referindo a pasta geral recipes e
depois movemos no arquivo home.html(recipes). Ou seja,

            recipes/templates/recipes/home.html

Assim, criamos agora basicamente um name_space para esse arquivo, ou seja,
toda vez que for referir ao arquivo home.html precisamos também
referir a "recipes" pois queremos ser específico, ou seja, queremos o
home.html que está dentro da pasta recipes, assim

    def home(request):
    return render(request, 'recipes/home.html')

ou seja, agora temos namespace recipes para me proteger.

Podemos gerar um namespace para os arquivos globais, aqui no caso por
exemplo, gosto de chamar os arquivos globais de globais. Então vamos chamar
aqui no caso a pasta de global dentro da pasta base_templates, e movemos
o arquivo home.html(BASE) de base_templates para global, ou seja,

        base_templates/global/home.html

agora nunca mais iremos conseguir colidir esse nomes:

    def home(request):
    return render(request, 'global/home.html')

    ou,

    def home(request):
    return render(request, 'recipes/home.html')

e é basicamente isso, e isso se chama de "namespace" que a gente está fazendo.
"""


def home(request):
    return render(request, 'recipes/home.html')
