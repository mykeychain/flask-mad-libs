from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@apps.route("/form")
def show_form():

    prompt_list

    return render_template("questions.html", 
        prompts=prompt_list)