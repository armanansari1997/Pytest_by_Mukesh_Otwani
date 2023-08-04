import pytest
import sys


@pytest.mark.parametrize("username, password",
                         [
                             ("Selenium", "WebDriver"),
                             ("Python", "Pytest"),
                             ("Mukesh", "Otwani"),
                             ('API', 'Web')
                         ]
                         )
def test_demo(username, password):
    print("Username :", username)
    print("Password :", password)
