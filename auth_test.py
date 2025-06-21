from page.AuthPage import AuthPage
from page.MainPage import MainPage

def test_auth(browser):
    email = "llirik1552@gmail.com"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "jfjieiewoh@#$*$")

    main_page = MainPage(browser)
    main_page.open_menu()

    info = main_page.get_account_info()

    assert main_page.get_current_url().endswith("kirilla1552/boards")
    assert info[0] == "Кирилл Кириченко"
    assert info[1] == email