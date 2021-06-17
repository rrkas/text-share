import uuid

from flask import *

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
def home():
    return render_template('home.html', generate_file_id=generate_file_id)


@main_bp.route('/edit/<file_id>')
def editor(file_id):
    return render_template('editor.html', file_id=file_id, save=save)


def generate_file_id():
    file_id = uuid.uuid4().hex
    return file_id


@main_bp.route('/save/<file_id>', methods=['POST'])
def save(file_id):
    print(file_id)
    print(request.json)
    for k, v in request.form.items():
        print('form:', k, v)
    for k, v in request.args.items():
        print('args:', k, v)
    for k, v in request.values.items():
        print('value:', k, v)
    return '200'
