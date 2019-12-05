from flask import Blueprint, jsonify

from models import Men, db


api = Blueprint('api', __name__,url_prefix='/api')
index = Blueprint('index', __name__,url_prefix='/')



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

@index.route('/')
@index.route('/index')
def get_index():
    return '''
        <html>
             <title>
               MegaRestful web service
             </title> 
             <body>
              <h3>API:</h3>
              <a href =" ./api/Men">Men</a> 
              </body>
        </html>
             
           '''
