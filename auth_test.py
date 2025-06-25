import allure
from page.AuthPage import AuthPage
from page.MainPage import MainPage

def test_auth(browser):
    email = "llirik1552@gmail.com"
    password = "jfjieiewoh@#$*$"
    username = "Кирилл Кириченко"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("llirik1552@gmail.com", "jfjieiewoh@#$*$")

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()

    with allure.step("Проверить, что URL " + current_url + "заканчивается на kirilla1552/boards"):
        assert current_url.endswith("kirilla1552/boards")

    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть " + username):
            assert info[0] == username
        with allure.step("Почта пользователя должна быть " + email):
            assert info[1] == email
