import json


def get_candidates(path):
    """получаем список кандидатов из файла"""
    with open(path, "r", encoding='utf-8') as candidates:
        return json.load(candidates)


def candidates_form(candidates_list):
    """форматируем в соответствии с требованиями список"""
    result = '<pre>'
    for candidate in candidates_list:
        result += (
            f'Имя кандидата - {candidate["name"]}\n'
            f'Позиция кандидата - {candidate["position"]}\n'
            f'Навыки через запятую - {candidate["skills"]}\n'
            f'\n'
        )
    result += '</pre>'
    return result


def by_id_search(candidates_list, candidate_id):
    """поиск по ID"""
    for candidate in candidates_list:
        if candidate["id"] == candidate_id:
            return candidate


def by_skill_search(candidates_list, candidate_skill):
    """поиск по скиллу"""
    list_by_skill = []
    for candidate in candidates_list:
        candidate_skills = candidate["skills"].lower().split(", ")
        if candidate_skill in candidate_skills:
            list_by_skill.append(candidate)
    return list_by_skill
