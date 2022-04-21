import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    with open("candidates.json", "r", encoding='utf-8') as candidates:
        candidates_list = candidates.load(candidates)
        for candidate in candidates_list:
            result = (f'Имя кандидата')
        result = '<pre>'
        result += (
            f'Имя кандидата - {candidate["name"]}'
            f'Позиция кандидата - {candidate["position"]}'
            f'Навыки через запятую - {candidate["skills"]}'
        )
        result += '</pre>'
        return result


@app.route("/candidates/<candidate_id>")
def candidates(candidate_id):
    pass


@app.route("/skills/<skill>")
def skills(skill):
    pass


app.run()
