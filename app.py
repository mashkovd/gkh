from flask import Flask, jsonify, send_from_directory, make_response, request
from flask_cors import CORS
from flask.json import JSONEncoder
from datetime import date
import json
from models import Session, Consultants, Patients, Departments, SickLists, Diagnoses, Reasons
from settings import *
from werkzeug.serving import run_simple


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app = Flask(__name__, static_folder='static/')
app.config['JSON_AS_ASCII'] = False
app.json_encoder = CustomJSONEncoder
CORS(app)


@app.route('/')
def index():
    return app.send_static_file("index.html")


def get_dict_from_cursor(res):
    return [dict(item.items()) for item in res]


@app.route('/<path:path>')
def static_dist(path):
    # тут пробрасываем статику
    return send_from_directory("static/dist", path)


@app.route('/api/consultants')
def consultants():
    session = Session()
    res = session.execute(session.query(Consultants.id.label('value'),
                                        Consultants.consultant_name.label('text')
                                        ).order_by(Consultants.consultant_name)
                          ).fetchall()
    session.close()
    return jsonify({
        'items': get_dict_from_cursor(res),
        'fields': CONSULTANTS_FIELDS
    })


@app.route('/api/patients')
def patients():
    session = Session()
    res = session.execute(session.query(Patients)).fetchall()
    session.close()
    return jsonify({
        'items': get_dict_from_cursor(res),
        'fields': PATIENTS_FIELDS
    })


@app.route('/api/departments')
def departments():
    session = Session()
    res = session.execute(session.query(Departments.id.label('value'),
                                        Departments.department_name.label('text'),
                                        ).order_by(Departments.department_name)).fetchall()
    session.close()
    return jsonify({
        'items': get_dict_from_cursor(res),
        'fields': DEPARTMENTS_FIELDS
    })


@app.route('/api/diagnoses')
def diagnoses():
    session = Session()
    res = session.execute(session.query(Diagnoses)).fetchall()
    session.close()
    return jsonify({
        'items': get_dict_from_cursor(res),
        'fields': DIAGNOSES_FIELDS
    })


@app.route('/api/sick_lists')
def sick_lists():
    session = Session()
    if request.args.get('currentPage') is None:
        cur_page = 1
    else:
        cur_page = int(request.args.get('currentPage'))
    per_page = int(request.args.get('perPage'))

    number, correction, consultants, departments, diagnoses = None, None, None, None, None
    if request.args.get('filter'):
        correction = json.loads(request.args.get('filter')).get('correction')
        number = json.loads(request.args.get('filter')).get('number')
        consultant = json.loads(request.args.get('filter')).get('consultant')
        department = json.loads(request.args.get('filter')).get('department')
        diagnose = json.loads(request.args.get('filter')).get('diagnose')

    s = session.query(SickLists, Patients, Departments, Diagnoses, Reasons, Consultants). \
        join(Consultants). \
        join(Patients). \
        join(Departments). \
        join(Diagnoses). \
        join(Reasons).options()

    if number is not None:
        s = s.filter(SickLists.number_of_consultation == int(number))
    if correction is not None:
        s = s.filter(SickLists.correction == int(correction))
    if consultant is not None:
        s = s.filter(SickLists.consultant_id == int(consultant))
    if department is not None:
        s = s.filter(SickLists.department_id == int(department))
    if diagnose is not None:
        s = s.filter(Diagnoses.diagnose_name.like(f"%{diagnose}%"))

    res = session.execute(s).fetchall()
    total_rows = len(res)
    res = res[(cur_page - 1) * per_page: cur_page * per_page]
    session.close()
    return jsonify({
        'items': get_dict_from_cursor(res),
        'fields': SICKLIST_FIELDS,
        'totalRows': total_rows
    })


if __name__ == '__main__':
    run_simple(hostname='localhost',
               port=5000,
               application=app,
               use_reloader=True,
               use_debugger=True)
