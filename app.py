from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/form")
def show_form():
    """ Generates and returns form from list of prompts. """ 

    return render_template("questions.html", 
        prompts=silly_story.prompts)


@app.route("/story")
def show_story():
    """ Generates and returns story from form inputs.  """

    inputs = request.args

    full_story = silly_story.generate(inputs)

    return render_template("story.html",
        story=full_story)
