from flask import Flask, jsonify

from hr_questions import select_questions

app = Flask(__name__)


@app.route('/', methods=['POST'])
def technical():

    questions = select_questions()

    return jsonify(
        {
            'hr_questions': questions
        }
    )


@app.route('/', methods=['GET'])
def hello():
    return '<h2>HR Interviewer</h2>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=65535)
