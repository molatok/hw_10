import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    with open("candidates.json", "r", encoding='utf-8') as candidates:
        candidates_list = json.load(candidates)

        result = '<pre>'
        for candidate in candidates_list:
            result += (
                f'Имя кандидата - {candidate["name"]}\n'
                f'Позиция кандидата - {candidate["position"]}\n'
                f'Навыки через запятую - {candidate["skills"]}\n'
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
