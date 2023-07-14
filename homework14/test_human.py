"""Test the Human class in the attached file. I will check the coverage. Write as many TCs as possible"""
import pytest

from homework14.human import Human


def test_age_getter(create_human):
    expected_age = 25
    human = Human('Ivan', expected_age, 'male')

    assert human.age == expected_age, 'provided age is not equals to the expected'


def test_gender_getter(create_human):
    expected_gender = 'male'
    human = Human('Ivan', 25, expected_gender)

    assert human.gender == 'male', 'provided gender is not equals to the expected'


def test_grow_valid(create_human):
    human = create_human
    new_age = human.age + 1
    human.grow()

    assert human.age == new_age, 'age should be incremented'


def test_grow_valid_corner_case(human_99_years_old):
    human = human_99_years_old
    new_age = human.age + 1
    human.grow()

    assert human.age == new_age, 'age should be incremented'


def test_dead_person(human_100_years_old):
    human = human_100_years_old
    human.grow()

    assert human._Human__status == 'dead', 'It is still alive'


def test_if_person_dead(human_100_years_old):
    human = human_100_years_old
    human.grow()

    with pytest.raises(Exception) as exc_info:
        human._Human__is_alive()

    assert str(exc_info.value) == f'{human._Human__name} is already dead...', 'Human is not dead'


def test_if_person_dead_after_grow(human_100_years_old):
    human = human_100_years_old
    human.grow()

    with pytest.raises(Exception) as exc_info:
        human.grow()

    assert str(exc_info.value) == f'{human._Human__name} is already dead...', 'Human is still alive'


def test_if_person_alive(create_human):
    human = create_human
    human._Human__is_alive()

    assert human._Human__is_alive() is True, 'Human is not alive'


def test_change_gender_valid(create_human):
    human = create_human
    new_gender = 'female'
    human.change_gender(new_gender)

    assert human.gender == new_gender, 'gender should be changed'


def test_change_gender_human_is_not_alive(human_100_years_old):
    human = human_100_years_old
    new_gender = 'female'
    human.grow()

    with pytest.raises(Exception) as exc_info:
        human.change_gender(new_gender)

    assert str(exc_info.value) == f'{human._Human__name} is already dead...', 'Human is still alive'


def test_change_gender_not_valid(create_human):
    human = create_human
    new_gender = 'not_valid_gender'

    with pytest.raises(Exception) as exc_info:
        human.change_gender(new_gender)

    assert str(exc_info.value) == 'Not correct name of gender', 'exception is not worked'
