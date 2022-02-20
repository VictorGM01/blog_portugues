from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id_post>/detalhar', views.detalhar, name='detalhar-post'),
    path('mapas_mentais', views.mapas_mentais, name='mapas-mentais'),
    path('resumos', views.resumos, name='resumos')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
