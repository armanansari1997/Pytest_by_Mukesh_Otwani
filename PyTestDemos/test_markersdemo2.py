import pytest
import sys


@pytest.mark.skip
def test_login():
    print('Login done')


@pytest.mark.skipif(sys.version_info < (3, 11), reason='python version not supported')
def test_add_product():
    print('Add Product done')


@pytest.mark.xfail
def test_logout():
    assert False
    print('Logout done')


def test_close_application():
    print('Close the application')