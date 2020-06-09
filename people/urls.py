from django.urls import path

from .views import people_views as pv

urlpatterns = [
    # /people/
    path('', pv.home, name="index"),
    #/people/listar
    path('listar', pv.listar, name="listar"),
    # /people/detalar/1/
    path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),
    # /people/excluir/1/
    path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),
    # /people/cadastro
    path('cadastro', pv.cadastro, name="cadastro"),
    # /people/cadastrar
    path('cadastrar', pv.cadastrar, name="cadastrar"),
    # query filto por idade
    path('queryfilterage/', pv.queryfilterage, name="queryfilterage"),
    # query filto por data de nascimento
	path('queryfilterdateofbirth/', pv.queryfilterdateofbirth, name="queryfilterdateofbirth"),
    # query filto pelos primeiros registros
	path('queryfirstrecords/', pv.queryfirstrecords, name="queryfirstrecords"),
    # query filto por nome
	path('queryfiltername/', pv.queryfiltername, name="queryfiltername")
]
