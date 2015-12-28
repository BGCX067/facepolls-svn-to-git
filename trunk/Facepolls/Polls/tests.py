# -*-coding:utf-8-*-

from django.test import TestCase
from datetime import datetime
import unittest
from django.test.client import Client
from Polls.models import Enquete, Votacao

class PollTest(unittest.TestCase):
    def setUp(self):
        pergunta="Qual a maior torcida a do Flamengo ou a do Vasco??"
        now = datetime.now()
        self.poll = Enquete.objects.create(pergunta=pergunta, data=now)
        self.poll.votacao_set.create(opcao="Flamengo", quantidadevotos=0)
        self.poll.votacao_set.create(opcao="Vasco", quantidadevotos=0)

    def test_models(self):
        self.assertEqual(self.poll.votacao_set.all().count(), 2)

    def test_voting(self):
        c = Client()
        # Executar uma opcao na votacao atraves do metodo Post
        response = c.post('/enquete/1/voto/', {'opcao': '1',})
        # O voto do client foi redirecionado e depois verificar se a reposta eh 1
        self.assertEqual(response.status_code, 200)
        # Pega a votacao e verifica se eh um voto
        opcao = Votacao.objects.get(pk=1)
        self.assertEqual(opcao.quantidadevotos, 1)

    def test_status_http_vote_wrong(self):
        c = Client()
        # Se for um voto invalido - opcao nao existe
        response = c.post('/enquete/1/voto/', {'opcao': '10',})
        # Codigo da resposta do http correto = 200
        self.assertEqual(response.status_code, 200)
        # Caso voto incorreto retorna = 0
        self.assertEqual(response.content, '0')

    def test_status_http_vote_ok(self):
        c = Client()
        # Se for um voto valido e se opcao existir
        response = c.post('/enquete/1/voto/', {'opcao':'2'})
        # Codigo da resposta do http correto = 200
        self.assertEqual(response.status_code, 200)
        # Caso o voto certo = 1
        self.assertEqual(response.content, '1')


        # Se for um voto invalido - Enquete nao existir
        #response = c.post('/enquete/5/voto/', {'opcao': '1',})
        #self.assertEqual(response.status_code, 404)

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
