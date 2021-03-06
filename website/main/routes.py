import os
import uuid

from flask import *

main_bp = Blueprint('main_bp', __name__)

files_dir = os.path.join(current_app.root_path, 'files')


@main_bp.route('/')
def home():
    return render_template('home.html', generate_file_id=generate_file_id)


@main_bp.route('/edit/<file_id>')
def editor(file_id):
    file = os.path.join(files_dir, file_id + '.txt')
    if not os.path.exists(files_dir):
        os.mkdir(files_dir)
    if not os.path.exists(file):
        open(file, 'w').close()
    with open(file) as f:
        text = f.read()
    return render_template('editor.html', file_id=file_id, save=save, text=text)


@main_bp.route('/view/<file_id>')
def view(file_id):
    file = os.path.join(files_dir, file_id + '.txt')
    if not os.path.exists(files_dir):
        abort(400)
    file = open(file)
    text = file.read()
    file.close()
    # text = text.replace('\n', '<br>')
    return render_template('viewer.html', text=text, file_id=file_id)


@main_bp.route('/save/<file_id>', methods=['POST'])
def save(file_id):
    if 'text' in request.json.keys():
        text = request.json['text']
        if len(text) > 0:
            file = os.path.join(files_dir, file_id + '.txt')
            if os.path.exists(file):
                with open(file, 'w') as file_writeable:
                    file_writeable.write(text)
                # with open(file) as file_readable:
                #     print(file_readable.read())
                return '200'
            return '404'
    return '500'


def generate_file_id():
    if not os.path.exists(files_dir):
        os.mkdir(files_dir)
    file_id = uuid.uuid4().hex
    while os.path.exists(os.path.join(files_dir, file_id + '.txt')):
        file_id = uuid.uuid4().hex
    return file_id

#================errors========================

@main_bp.app_errorhandler(400)
def error_400():
    pass