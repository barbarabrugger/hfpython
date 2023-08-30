import html
from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route("/search4", methods=["POST"])
def do_search() -> "html":
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    the_title = "Here are your results:"
    the_results = search4letters(phrase, letters)
    return render_template(
        "results.html",
        the_phrase=phrase,
        the_letters=letters,
        the_title=the_title,
        the_results=the_results,
    )


@app.route("/")
@app.route("/entry")
def entry_page() -> "html":
    return render_template(
        "entry.html", the_title="Welcome to search4letters on the web!"
    )


if __name__ == "__main__":
    app.run(debug=True)
