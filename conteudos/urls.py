from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id_post>', views.detalhar, name='detalhar-post'),
    path('posts/mapas_mentais', views.mapas_mentais, name='mapas-mentais'),
    path('posts/resumos', views.resumos, name='resumos'),
    path('posts/todos', views.resumos_e_mapas, name='todos'),
    path('posts/criadores', views.criadores, name='criadores')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
