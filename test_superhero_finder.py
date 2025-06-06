import pytest
from superhero_finder import find_tallest_hero_by_criteria

def test_tallest_male_with_job():
    hero = find_tallest_hero_by_criteria(gender='Male', has_job=True)
    assert hero['appearance']['gender'] == 'Male'
    assert hero['work']['occupation'] != '-'

def test_tallest_female_with_job():
    hero = find_tallest_hero_by_criteria(gender='Female', has_job=True)
    assert hero['appearance']['gender'] == 'Female'
    assert hero['work']['occupation'] != '-'

def test_tallest_hero_no_job():
    hero = find_tallest_hero_by_criteria(has_job=False)
    assert hero['work']['occupation'] == '-' or not hero['work']['occupation']

def test_no_matching_heroes():
    with pytest.raises(ValueError, match="No heroes found"):
        find_tallest_hero_by_criteria(gender='Unknown', has_job=True)
