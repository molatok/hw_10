import json
from flask import Flask
from utils import get_candidates, candidates_form, by_id_search, by_skill_search

app = Flask(__name__)


@app.route("/")
def main():
    candidates_list = get_candidates("candidates.json")
    return candidates_form(candidates_list)


@app.route("/candidates/<int:candidate_id>")
def page_candidate(candidate_id):
    candidates_list = get_candidates("candidates.json")
    candidate = by_id_search(candidates_list, candidate_id)
    result = f'<img src="{candidate["picture"]}">'
    return result + candidates_form([candidate])


@app.route("/skills/<skill>")
def skills(skill):
    candidates_list = get_candidates("candidates.json")
    return candidates_form(by_skill_search(candidates_list, skill))


app.run()
