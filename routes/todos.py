from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Todo

todos_bp = Blueprint("todos", __name__)


@todos_bp.route("/todos", methods=['GET', 'POST'])
@login_required
def index():
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", todos=todos)


@todos_bp.route("/add", methods=["POST"])
@login_required
def addTodo():
    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()

    if title == "" or content == "":
        flash("Please do not leave the task title or content place!", "warning")
        return redirect(url_for("todos.index"))

    newTodo = Todo(title=title, content=content,
                   complete=False, user_id=current_user.id)
    db.session.add(newTodo)
    db.session.commit()

    flash("New task successfully added!", "success")
    return redirect(url_for("todos.index"))


@todos_bp.route("/update/<int:id>")
def updateTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo:
        todo.complete = not todo.complete
        db.session.commit()
    return redirect(url_for("todos.index"))


@todos_bp.route("/delete/<int:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for("todos.index"))


@todos_bp.route("/detail/<int:id>")
def detailTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    return render_template("detail.html", todo=todo)
