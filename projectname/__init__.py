from flask import Flask

app = Flask(
    __name__,
    static_folder="views/static",
    template_folder="views/templates",
)

import projectname.controllers.controller  # noqa: F401
