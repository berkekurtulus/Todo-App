from flask import Flask, render_template
from flask_login import LoginManager
from models import db, User
from routes.todos import todos_bp
from routes.auth import auth_bp

app = Flask(__name__)
app.secret_key = "todo_app_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(todos_bp)
app.register_blueprint(auth_bp)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
