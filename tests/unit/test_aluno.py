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

def test_situacao_final_reprova_por_falta_quando_passa_de_25_por_cento():
    aluno = Aluno(nome="Eva", notas=[9, 9, 9, 9], faltas=2)

    assert aluno.situacao_final(total_aulas=4) == "Reprovado por falta"


def test_situacao_final_aprova_quando_tem_poucas_faltas_e_media_alta():
    aluno = Aluno(nome="Felipe", notas=[8, 8, 8, 8], faltas=1)

    assert aluno.situacao_final(total_aulas=5) == "Aprovado"


def test_situacao_final_reprova_por_nota_quando_tem_poucas_faltas_e_media_baixa():
    aluno = Aluno(nome="Gabriela", notas=[4, 4, 4, 4], faltas=1)

    assert aluno.situacao_final(total_aulas=5) == "Reprovado por nota"


def test_situacao_final_nao_reprova_por_falta_quando_tem_exatamente_25_por_cento():
    aluno = Aluno(nome="Henrique", notas=[4, 4, 4, 4], faltas=1)

    assert aluno.situacao_final(total_aulas=4) == "Reprovado por nota"


def test_situacao_final_reprova_por_falta_quando_ultrapassa_25_por_cento_por_pouco():
    aluno = Aluno(nome="Isabela", notas=[9, 9, 9, 9], faltas=2)

    assert aluno.situacao_final(total_aulas=7) == "Reprovado por falta"


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método

def test_enviar_boletim_aciona_servico_quando_aluno_estiver_reprovado():
    aluno = Aluno(nome="Joana", notas=[4, 4, 4, 4], faltas=0)
    email_service = MagicMock()

    aluno.enviar_boletim(email_service)

    email_service.assert_called_once_with("Joana", 4.0)


def test_enviar_boletim_nao_aciona_servico_quando_aluno_estiver_aprovado():
    aluno = Aluno(nome="Kaique", notas=[8, 8, 8, 8], faltas=0)
    email_service = MagicMock()

    aluno.enviar_boletim(email_service)

    email_service.assert_not_called()
