import json

# filename = 'candidates.json'


def load_candidates_from_json(filename):
    """Открывает на чтение файл json,
    возвращает список словарей с данными
    кандидатов
    :param -> filename.json
    :return list[dict]
    """

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_candidate(candidate_id: int):
    """Получает id(int) кандидата,
    возвращает словарь с данными этого кандидата
    :param candidate_id:
    :return: dict
    """

    for candidate in load_candidates_from_json(filename):
        if candidate_id == candidate['id']:
            return candidate


def get_candidates_by_name(candidate_name):
    """Получает name(str) кандидата,
    возвращает список с данными об этом кандидате
    :param candidate_name:
    :return: list[dict]
    """

    result = []
    for candidate in load_candidates_from_json(filename):
        if candidate['name'] == candidate_name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    """Получает skill_name(str),
    возвращает список со словарями

    :param skill_name:
    :return: list[dict]
    """
    result = []
    for candidate in load_candidates_from_json(filename):
        if skill_name in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result



# load_candidates_from_json(filename)
# # # print(get_candidate(22))
# # print(get_candidates_by_name('Sheri Torres'))
# print(get_candidates_by_skill('go'))
