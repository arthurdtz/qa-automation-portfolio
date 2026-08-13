import requests


class TestUsersEndpoint:
    # Testes do endpoint /users da API reqres.in

    def test_get_single_user_returns_200(self, base_url, headers):
        # GET de usuário existente deve retornar status 200
        response = requests.get(f"{base_url}/users/2", headers=headers)
        assert response.status_code == 200

    def test_get_single_user_returns_correct_data(self, base_url, headers):
        # GET de usuário existente deve retornar os dados corretos
        response = requests.get(f"{base_url}/users/2", headers=headers)
        data = response.json()["data"]

        assert data["id"] == 2
        assert "email" in data
        assert "first_name" in data

    def test_get_nonexistent_user_returns_404(self, base_url, headers):
        # GET de usuário inexistente deve retornar 404
        response = requests.get(f"{base_url}/users/999", headers=headers)
        assert response.status_code == 404

    def test_create_user_returns_201(self, base_url, headers):
        # POST para criar usuário deve retornar status 201 (created)
        payload = {"name": "Arthur Meneses", "job": "QA Automation Engineer"}
        response = requests.post(f"{base_url}/users", json=payload, headers=headers)

        assert response.status_code == 201

    def test_create_user_returns_submitted_data(self, base_url, headers):
        """Resposta do POST deve conter os dados enviados, mais um id gerado"""
        payload = {"name": "Arthur Meneses", "job": "QA Automation Engineer"}
        response = requests.post(f"{base_url}/users", json=payload, headers=headers)
        data = response.json()

        assert data["name"] == payload["name"]
        assert data["job"] == payload["job"]
        assert "id" in data

    def test_update_user_returns_200(self, base_url, headers):
        # PUT para atualizar usuário deve retornar status 200
        payload = {"name": "Arthur Meneses", "job": "Senior QA Automation Engineer"}
        response = requests.put(f"{base_url}/users/2", json=payload, headers=headers)

        assert response.status_code == 200

    def test_delete_user_returns_204(self, base_url, headers):
        # DELETE de usuário deve retornar status 204 (no content)
        response = requests.delete(f"{base_url}/users/2", headers=headers)
        assert response.status_code == 204