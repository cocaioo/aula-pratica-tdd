import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno, contar_aprovados


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================

def test_calcular_media_usa_a_quantidade_real_de_notas():
    aluno = Aluno(nome="Ana", notas=[10, 8], faltas=0)

    assert aluno.calcular_media() == pytest.approx(9.0)


def test_situacao_aprova_quando_media_eh_exatamente_seis():
    aluno = Aluno(nome="Bruno", notas=[6, 6, 6, 6], faltas=0)

    assert aluno.situacao() == "Aprovado"


def test_menor_nota_retorna_o_menor_valor_da_lista():
    aluno = Aluno(nome="Carla", notas=[3, 9, 5, 7], faltas=0)

    assert aluno.menor_nota() == 3


def test_calcular_media_arredondada_arredonda_o_valor_da_media():
    aluno = Aluno(nome="Daniel", notas=[6, 7, 7, 7], faltas=0)

    assert aluno.calcular_media_arredondada() == 7

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função

def test_contar_aprovados_quando_todos_estao_aprovados(aluno_aprovado):
    assert contar_aprovados([aluno_aprovado, aluno_aprovado]) == 2


def test_contar_aprovados_quando_todos_estao_reprovados(aluno_reprovado):
    assert contar_aprovados([aluno_reprovado, aluno_reprovado]) == 0


def test_contar_aprovados_quando_lista_e_mista(aluno_aprovado, aluno_reprovado):
    assert contar_aprovados([aluno_aprovado, aluno_reprovado]) == 1


def test_contar_aprovados_quando_lista_e_vazia():
    assert contar_aprovados([]) == 0


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
