from flask import Flask, json, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todos(db.Model):
    periority = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(200), nullable=False, unique=True)

@app.route("/light-theme")
def todo_app_light():
    return render_template("base.html", title="Todo App - light",
                                        bg_img="images/bg-img.jpg",
                                        body_color="bg-white",
                                        container_color="bg-white",
                                        input_text_color="text-black",
                                        input_bg_color="bg-gray-200",
                                        todo_text_color="text-black",
                                        todo_bg_color="bg-gray-200",
                                        todo_list=Todos.query.all())


@app.route("/dark-theme")
def rodo_app_dark():
    return render_template("base.html", title="Todo App - dark",
                                        bg_img="images/bg-img-dark.jpg",
                                        body_color="bg-slate-950",
                                        container_color="bg-slate-800",
                                        input_text_color="text-gray-100",
                                        input_bg_color="bg-slate-700",
                                        todo_text_color="text-gray-300",
                                        todo_bg_color="bg-slate-700")


@app.route("/add", methods=["POST"])
def add():
    json_object = request.get_json()
    db.session.add(Todos(periority=len(Todos.query.all())+1, todo=json_object['todo']))
    db.session.commit()
    return redirect(url_for("todo_app_light"))




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # for i in Todos.query.all():
        #     db.session.delete(i)
        # db.session.commit() 
    app.run(debug=True)
