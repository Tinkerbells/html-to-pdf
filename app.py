import os
import weasyprint
from mako.template import Template
from mako.lookup import TemplateLookup
from flask import Flask, render_template_string

from data import example_data as data

mylookup = TemplateLookup(directories=["templates"])
root_path = os.path.dirname(__file__)
css = os.path.join(root_path, "static/css/styles.css")
app = Flask(__name__)


@app.route("/")
def index():
    html_str = render_template("index.html", data=data)
    weasyprint.HTML(string=html_str).write_pdf("output.pdf", stylesheets=[css])
    print(f"pdf file is saved as output.pdf to {root_path}/output.pdf")
    return render_template_string(html_str)


def render_template(template_name, **kwargs):
    mytemplate = mylookup.get_template(template_name)
    return mytemplate.render(**kwargs)


if __name__ == "__main__":
    # index()
    app.run(debug=True)
