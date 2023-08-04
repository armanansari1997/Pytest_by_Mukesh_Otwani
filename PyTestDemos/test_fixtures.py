import pytest


@pytest.fixture
def setup():
    print('Start Browser')
    yield
    print('Close Browser')  # Write your cleanup activities


def test_1(setup):
    # print('Start Browser')
    print('Test 1 executed')
    # print('Close Browser')


def test_2(setup):
    # print('Start Browser')
    print('Test 1 executed')
    # print('Close Browser')


def test_3(setup):
    # print('Start Browser')
    print('Test 1 executed')
    # print('Close Browser')