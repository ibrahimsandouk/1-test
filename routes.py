from flask import Blueprint, jsonify

from models import Men, db


api = Blueprint('api', __name__,url_prefix='/api')



@api.route('/Men')
def get_mens():
    return jsonify([(lambda men : men.json())(men)for men in Men.query.all()])



@api.route('/Men/id/<int:men_id>')
def get_id(men_id):
    men =Men.query.get(men_id)
    return jsonify(men.json())if men else ""



@api.route('/Men/name/<string:man_name>')
def putMan (man_name):
     db.session.add(Men(name=man_name))
     db.session.commit()
     return 'done'
