import pytest
from accounts.models import CustomUser as User 

@pytest.mark.django_db
def test_login_com_credenciais_validas(client):
    """Testa login com usuário e senha corretos"""
    User.objects.create_user(username="ellen", password="Senha123")

    response = client.post("/accounts/login/", {"username": "ellen", "password": "Senha123"})

    assert response.status_code == 302  
    assert response.url == "/accounts/dashboard/"  
    
@pytest.mark.django_db
def test_login_com_senha_incorreta(client):
    """Testa login com senha errada"""
    User.objects.create_user(username="ellen", password="Senha123")

    response = client.post("/accounts/login/", {"username": "ellen", "password": "SenhaErrada"})

    assert response.status_code == 200  # A página de login é recarregada
    assert "Credenciais inválidas" in response.content.decode("utf-8")  

@pytest.mark.django_db
def test_login_com_usuario_inexistente(client):
    """Testa login com um usuário que não existe"""
    response = client.post("/accounts/login/", {"username": "usuario_fake", "password": "Senha123"})

    assert response.status_code == 200  # A página de login é recarregada
    assert "Credenciais inválidas" in response.content.decode("utf-8")
