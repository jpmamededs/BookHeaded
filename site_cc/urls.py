from django.urls import path
from . import views
from .views import (
    clubes_view, 
    club_detail_view,
    CategoriaView,
    add_club_view,
    clube_update_view,
    delete_club_view,
    add_categoria_view,
    meus_clubes_view,
    aprovar_membro,
    adicionar_membro,
    recusar_membro,
    adicionar_membro_publico,
    avaliacao_view,
    add_comentario_view,
    seguir_usuario,
    criar_maratona_view,
    profile,
    lista_usuarios,
    favoritar_clube,
    top_livros,
    add_top_livros,
    get_modalidades,
    get_categorias,
    detalhes_maratona_view,
    finalizar_maratona_view,
    listar_historico_maratona_view,
)

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('clube/<int:pk>/', club_detail_view, name='club-Detail'),
    path('addClube/', add_club_view, name='addClube'),
    path('clube/edit/<int:pk>/', clube_update_view, name='updateClube'),
    path('api/modalidades/', views.get_modalidades, name='api_modalidades'),
    path('api/categorias/', views.get_categorias, name='api_categorias'),
    path('clube/delete/<int:pk>/', delete_club_view, name='deleteClube'),
    path('clubs/', clubes_view, name='clubs'),
    path('addCategoria/', add_categoria_view, name='addCategoria'),
    path('myclubes/',  meus_clubes_view, name='myclubes'),
    path('clube/<int:clube_id>/adicionar/', adicionar_membro, name='adicionar-membro'),
    path('clube/<int:clube_id>/aprovar/<int:membro_id>/', aprovar_membro, name='aprovar-membro'),
    path('clube/<int:clube_id>/recusar-membro/<int:membro_id>/', recusar_membro, name='recusar-membro'),
    path('categoria/<str:cats>/', CategoriaView, name='categoria'),
    path('clube/<int:clube_id>/juntar', adicionar_membro_publico, name='adicionar-membro-publico'),
    path('avaliacao/<int:pk>/', avaliacao_view, name='avaliacoes_clube'),
    path('clube/<int:pk>/Comentario/', add_comentario_view, name='add_comentario'),
    path('introducao/', views.introducao, name='introducao'),
    path('equipe/', views.equipe, name='equipe'),
    path('contato/', views.contato, name='contato'),
    path('clube/<int:clube_id>/atualizar_progresso/',views.atualizar_progresso, name='atualizar_progresso'),
    path('perfil/<int:user_id>/', profile, name='profile'),
    path('seguir/<int:user_id>/', seguir_usuario, name='seguir_usuario'),
    path('clube/favoritar/<int:clube_id>/', views.favoritar_clube, name='favoritar_clube'),
    path('clube/<int:clube_id>/top-livros/', views.top_livros, name='top_livros'),
    path('clube/<int:clube_id>/add-top-livros/', views.add_top_livros, name='add_top_livros'),
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('clube/<int:clube_id>/criar_maratona/', views.criar_maratona_view, name='criar_maratona'),
    path('clube/<int:clube_id>/detalhes_maratona/', detalhes_maratona_view, name='detalhes_maratona'),
    path('clube/<int:clube_id>/finalizar_maratona/', views.finalizar_maratona_view, name='finalizar_maratona'),
    path('clube/<int:clube_id>/listar_historico_maratona/', listar_historico_maratona_view, name='listar_historico_maratona'),
]
