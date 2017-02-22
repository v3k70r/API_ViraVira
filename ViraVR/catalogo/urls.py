from django.conf.urls import url
from catalogo import views

urlpatterns = [
    url(r'^especies/$', views.especie_list),
    url(r'^especies/(?P<pk>[0-9]+)/$', views.especie_detail),
    url(r'^especies/por_nombre/(<nombre>[a-z])/$', views.especie_detail_nombre),
    url(r'^clasificaciones/$', views.clasificacion_list),
    url(r'^clasificaciones/(?P<pk>[0-9]+)/$', views.clasificacion_detail),
]