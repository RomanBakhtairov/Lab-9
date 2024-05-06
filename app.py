from flask import Flask,redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#Вариант 3
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cities.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#
#
class Town_visit(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    town = db.Column(db.String(85), nullable = False)#why 85? The longest place name in world - Taumatawhakatangihangakoauauotamateaturipukakapiki-maungahoronukupokaiwhenuakitanatahu
    visit_date  = db.Column(db.String(10),nullable = False)
    def __repr__(self):
        return f'Town{self.id}. You visited {self.town} on {self.visit_date}'
#
#   
@app.route('/')#main
def main():
    cities = Town_visit.query.all()
    return render_template('index.html', cities_list=cities)
#
#
@app.route('/add', methods=['POST'])#for adding the base data
def add_town():
    data = request.json
    town = Town_visit(**data)
    db.session.add(town)
    db.session.commit()
#
#
@app.route('/delete')#for deleting the base data
def drop_date():
    for city in Town_visit.query.all():
        db.session.delete(city)
    db.session.commit()
    return redirect(url_for('main'))
#
#
with app.app_context():
    db.create_all()