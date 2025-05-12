from flask import Flask,render_template, request
import src.example_package_gleb_koniaev.monaco.cli_for_html as html
import src.example_package_gleb_koniaev.monaco.report_printer as form
import sys
import os
import re

app = Flask(__name__)


def load_abbrevations(file_path):
    abbrevations = {}
    with open(file_path, "r") as f:
        for lines in f:
            if lines.strip():
                match = re.match(r"^([^_]+)_([^_]+)_(.+)$", lines.strip())
                if match:
                    code, name, team = match.groups()
                    abbrevations[f"{name}_{team}".lower()] = code
                else:
                    print(f"Warning: Could not parse line: {lines.strip()}")
    return abbrevations


abbreviations = load_abbrevations(os.path.join("files", "abbreviations.txt"))


@app.route("/report")
def report():
    sys.argv = ["cli.py", "--files", "./files"]
    report, errors = html.main()
    formatted_report = [
        (form.ReportPrinter.format_time(time), name, team)
        for time, name, team in report
    ]
    return render_template("index.html", report=formatted_report, errors=errors)


@app.route("/report/drivers")
def drivers():
    order = request.args.get("order", "asc")
    sys.argv = ["cli.py", "--files", "./files", "--desc" if order == "desc" else ""]
    report, errors = html.main()
    return ""



if __name__ == "__main__":
    app.run(debug=True)
