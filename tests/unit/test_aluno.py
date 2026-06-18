import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================

def test_calcular_media_usa_a_quantidade_real_de_notas():
    aluno = Aluno(nome="Ana", notas=[10, 8], faltas=0)

    assert aluno.calcular_media() == pytest.approx(9.0)

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
