from projectname import app
from flask import render_template
from sqlalchemy.orm import Session
from projectname.models.Template import Template
from projectname.models.Base import Base, engine


@app.route("/")
def main_page():
    with Session(engine) as session:
        Base.metadata.create_all(engine)
        data = session.query(Template).all()
    return render_template("index.html", data=data)


@app.route("/manifest.json")
def server_manifest():
    return app.send_static_file("manifest.json")


@app.route("/sw.js")
def serve_sw():
    return app.send_static_file("sw.js")
