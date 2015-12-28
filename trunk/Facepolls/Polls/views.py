# -*-coding:utf-8-*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from Polls.models import Enquete,Votacao

def homepage(request):
    ultimas_5_noticias = Enquete.objects.all().order_by('-data')[:5]
    top_polls = Enquete.objects.all().order_by('-votado')[:3]
    return render_to_response('Polls/index.html',locals(),context_instance=RequestContext(request))

def TopPolls(request):
    ultimas_5_noticias = Enquete.objects.all().order_by('-votado')[:5]
    return render_to_response('Polls/top.html',locals(),context_instance=RequestContext(request))
    #return render_to_response('Polls/index.html', {'ultimas_5_noticias': ultimas_5_noticias})
def Minhaenquete(request):
    ultimas_5_noticias = Enquete.objects.all().order_by('-data')[:5]
    return render_to_response('Polls/top.html',locals(),context_instance=RequestContext(request))
def todosresultados(request):
    ultimas_5_noticias = Enquete.objects.all().order_by('-data')[:5]
    return render_to_response('Polls/resultados.html',locals(),context_instance=RequestContext(request))
#Mostra as opções para voto
def detalhe(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)
    #return render_to_response('Polls/enquete.html', {'enquete': p})
    return render_to_response('Polls/enquete.html',locals(),context_instance=RequestContext(request))

#def para fazer a votação
def voto(request, enquete_id):
    p = get_object_or_404(Enquete, pk=enquete_id)
    try:
        selected_opcao = p.votacao_set.get(pk=request.POST['opcao'])
    except (KeyError, Votacao.DoesNotExist):
        # Voto errado retorna '0'
        if request.POST:
            return HttpResponse('0')
        return render_to_response('Polls/detalhe.', {
            'enquete': p,
            'error_message': "Você não selecionou nenhuma opção.",
            })
    else:
        selected_opcao.quantidadevotos += 1
        selected_opcao.save()
        p.votado += 1
        p.save()
        # Voto certo retorna '1'
        #if request.POST:
            #return HttpResponse('1')
        return render_to_response('Polls/voto-criado.html', locals(), context_instance=RequestContext(request))
        #return HttpResponseRedirect('/enquete/'+str(p.id)+'/resultado')

def resultado(request, enquete_id):
    enquete = get_object_or_404(Enquete, pk=enquete_id)
    return render_to_response('Polls/result.html',locals(),context_instance=RequestContext(request))

def cadastrarenquete(request):
    from forms import VotacaoForm,EnqueteForm

    if request.method == 'POST':
        #form1 = VotacaoForm(request.POST, request.FILES)
        #form = EnqueteForm(request.POST, request.FILES)
        novaEnquete = Enquete(pergunta = request.POST['pergunta'])
        novaEnquete.save()
        iteracao = 0
        for opcao in request.POST:
            if iteracao >0:
                novaVotacao = Votacao(perguntaEnquete = novaEnquete, foto = request.FILES['foto'+str(iteracao)],opcao = request.POST['opcao'+str(iteracao)] )
                novaVotacao.save()
            iteracao += 1
        #if form1.is_valid():
            #novo_votacao = form.save(commit=False)
            #novo_votacao.perguntaEnquete_id = novo_enquete.id
            #novo_votacao = form1.save()


        return render_to_response('Polls/enquete-criada.html',locals(), context_instance=RequestContext(request))
    else:
        form = EnqueteForm()#fuu
        form1 = VotacaoForm()
    return render_to_response('Polls/minha-enquete.html', locals(), context_instance=RequestContext(request))

def page_not_found(request):
    return render_to_response('Polls/404.html', locals(), context_instance=RequestContext(request))


