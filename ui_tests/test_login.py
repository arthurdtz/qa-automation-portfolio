from pages.login_page import LoginPage

class TestLogin:
    # Testes de login em the-internet.herokuapp.com

    def test_successful_login_shows_success_message(self, driver):
        # Login com credenciais válidas deve exibir mensagem de sucesso
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("tomsmith", "SuperSecretPassword!")

        flash_message = login_page.get_flash_message()
        assert "You logged into a secure area!" in flash_message

    def test_invalid_username_shows_error_message(self, driver):
        # Username inválido deve exibir mensagem de erro
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("wronguser", "SuperSecretPassword!")

        flash_message = login_page.get_flash_message()
        assert "Your username is invalid!" in flash_message

    def test_invalid_password_shows_error_message(self, driver):
        # Password inválido deve exibir mensagem de erro
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("tomsmith", "WrongPassword!")

        flash_message = login_page.get_flash_message()
        assert "Your password is invalid!" in flash_message

    def test_empty_credentials_shows_error_message(self, driver):
        # Campos de username e password vazios devem exibir mensagem de erro
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", "")

        flash_message = login_page.get_flash_message()
        assert "Your username is invalid!" in flash_message