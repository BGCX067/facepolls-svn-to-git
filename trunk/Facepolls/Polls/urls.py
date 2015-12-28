from django.conf.urls.defaults import patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Photopolls.Polls.views',
    (r'^$', 'homepage'),
    (r'cadastroenquete', 'cadastrarenquete'),
    (r'top-polls', 'TopPolls'),
    (r'minha-enquete', 'Minhaenquete'),
    (r'resultados', 'todosresultados'),
    (r'^(?P<enquete_id>\d+)/$', 'detalhe'),
    (r'^(?P<enquete_id>\d+)/resultado/$', 'resultado'),
    (r'^(?P<enquete_id>\d+)/voto/$', 'voto'),
)
