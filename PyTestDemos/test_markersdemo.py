import pytest


@pytest.mark.smoke
def test_login():
    print('Login done')


@pytest.mark.regression
def test_add_product():
    print('Add Product done')


@pytest.mark.smoke
def test_logout():
    print('Logout done')
