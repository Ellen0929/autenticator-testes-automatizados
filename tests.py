import pytest
from accounts.models import CustomUser as User  # Modelo corrigido

@pytest.mark.django_db
def test_login_com_credenciais_validas(client):
    """Testa login com usuário e senha corretos"""
    User.objects.create_user(username="ellen", password="Senha123")

    response = client.post("/accounts/login/", {"username": "ellen", "password": "Senha123"})

    assert response.status_code == 302  # Redirecionamento esperado
    assert response.url == "/accounts/dashboard/"  # Verifica se redireciona para o dashboard

@pytest.mark.django_db
def test_login_com_senha_incorreta(client):
    """Testa login com senha errada"""
    User.objects.create_user(username="ellen", password="Senha123")

    response = client.post("/accounts/login/", {"username": "ellen", "password": "SenhaErrada"})

    assert response.status_code == 200  # A página de login é recarregada
    assert "Credenciais inválidas" in response.content.decode("utf-8")  # ✅ Correção aqui

@pytest.mark.django_db
def test_login_com_usuario_inexistente(client):
    """Testa login com um usuário que não existe"""
    response = client.post("/accounts/login/", {"username": "usuario_fake", "password": "Senha123"})

    assert response.status_code == 200  # A página de login é recarregada
    assert "Credenciais inválidas" in response.content.decode("utf-8")