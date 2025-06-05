import requests

#Главная функция
def find_tallest_hero_by_criteria(gender=None, has_job=False):
    #Запрос данных с API
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    heroes = response.json()

    filtered_heroes = []
    for hero in heroes:
        # Проверка пола
        gender_match = (gender is None) or (hero.get('appearance', {}).get('gender') == gender)
        
        # Проверка работы (если occupation не пусто и не "-")
        occupation = hero.get('work', {}).get('occupation', '')
        job_match = not has_job or (occupation and occupation != '-')
        
        if gender_match and job_match:
            filtered_heroes.append(hero)

    if not filtered_heroes:
        raise ValueError("No heroes found matching the criteria")

    # Находим самого высокого
    tallest_hero = max(
        filtered_heroes,
        key=lambda hero: int(hero.get('appearance', {}).get('height', [0, 0])[1].split()[0])
    )
    return tallest_hero
