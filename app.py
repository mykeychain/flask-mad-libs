from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def choose_story():
    """ Generates drop down for user to choose a story template. """

    return render_template("index.html",
        story_templates=stories.story_templates)


@app.route("/form")
def show_form():
    """ Generates and returns form from list of prompts. """ 

    template = request.args["story-templates"] 

    return render_template("questions.html", 
        prompts = stories.story_templates[template].prompts,
        story_template = template)


@app.route("/story")
def show_story():
    """ Generates and returns story from form inputs.  """

    story_type = request.args["story_template"]
    inputs = request.args

    full_story = stories.story_templates[story_type].generate(inputs)

    return render_template("story.html",
        story = full_story)
