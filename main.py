from flask import Flask, request, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill
filename = 'candidates.json'

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = load_candidates_from_json(filename)
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:idx>')
def candidate_page(idx):
    candidate = get_candidate(idx)
    if not candidate:
        return 'Нет такого кандидата'
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_candidates_page(candidate_name):
    candidate = get_candidates_by_name(candidate_name)
    if not candidate:
        return 'Нет такого кандидата'
    return render_template('search.html', candidate=candidate)


@app.route('/skill/<skill_name>')
def skkill_candidates_page(skill):
    candidate = get_candidates_by_skill(skill)
    if not candidate:
        return 'Нет такого скила'
    return render_template('skills.html', skill=skill, candidate=candidate)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
