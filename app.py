import os
from datetime import datetime
import weasyprint
from mako.template import Template
from mako.lookup import TemplateLookup

# from flask import Flask, render_template_string

from data import example_data as data

mylookup = TemplateLookup(directories=["templates"])
root_path = os.path.dirname(__file__)
css = os.path.join(root_path, "static/css/styles.css")
# app = Flask(__name__)


def get_age_text(age):
    last = int(repr(age)[-1])
    if last == 1:
        return "год"
    elif last in [2, 3, 4]:
        return "года"
    else:
        return "лет"


# @app.route("/")
def index():
    now = datetime.now()
    formatted_date = now.strftime("%d-%m-%Y-%H_%M")
    # Разница возраста микробиоты и пациента
    patient_age = data["personal_data"]["patient_age"]
    microbiota_age = data["microbiota_age"]
    diff = abs(microbiota_age - patient_age)

    data["age_diff"] = diff
    data["age_diff_text"] = get_age_text(diff)

    if microbiota_age > patient_age:
        data["first_age"] = patient_age
        data["first_age_text"] = {
            "text": get_age_text(patient_age),
            "title": "возраст пациента",
        }
        data["second_age"] = microbiota_age
        data["second_age_text"] = {
            "text": get_age_text(microbiota_age),
            "title": "возраст микробиоты",
        }
        data["bar_width"] = 110 - patient_age / microbiota_age * 100
    else:
        data["first_age"] = microbiota_age
        data["first_age_text"] = {
            "text": get_age_text(microbiota_age),
            "title": "возраст микробиоты",
        }
        data["second_age"] = patient_age
        data["second_age_text"] = {
            "text": get_age_text(patient_age),
            "title": "возраст пациента",
        }
        data["bar_width"] = 100 - microbiota_age / patient_age * 100

    html_str = render_template("index.html", data=data)
    weasyprint.HTML(string=html_str).write_pdf(
        f"{formatted_date}.pdf", stylesheets=[css]
    )

    print(
        f"pdf file is saved as {formatted_date}.pdf to {root_path}/{formatted_date}.pdf"
    )

    return ""
    # return render_template_string(str(html_str))


def render_template(template_name, **kwargs):
    mytemplate = mylookup.get_template(template_name)
    return mytemplate.render(**kwargs)


if __name__ == "__main__":
    index()
    # app.run(debug=True)
