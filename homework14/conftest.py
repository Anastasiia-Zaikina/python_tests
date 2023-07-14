import pytest

from homework14.human import Human


@pytest.fixture()
def create_human():
    human = Human(name='Ostin', age=25, gender='male')
    return human

@pytest.fixture()
def human_99_years_old():
    human = Human(name='Lara', age=99, gender='female')
    return human

@pytest.fixture()
def human_100_years_old():
    human = Human(name='Steven', age=100, gender='male')
    return human
