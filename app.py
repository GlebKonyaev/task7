from flask import Flask, jsonify, render_template
import src.example_package_gleb_koniaev.monaco.cli_for_html as html
import src.example_package_gleb_koniaev.monaco.report_printer as form
import sys

app = Flask(__name__)


@app.route("/report")
def hello_world():
    sys.argv = ["cli.py", "--files", "./files"]
    report, errors = html.main()
    formatted_report = [
        (form.ReportPrinter.format_time(time), name, team)
        for time, name, team in report
    ]
    return render_template("index.html", report=formatted_report, errors=errors)


@app.route("/desc")
def hello_desc():
    sys.argv = ["cli.py", "--files", "./files", "--desc"]
    report, errors = html.main()
    formatted_report = [
        (form.ReportPrinter.format_time(time), name, team)
        for time, name, team in report
    ]
    return render_template("index.html", report=formatted_report, errors=errors)


if __name__ == "__main__":
    app.run(debug=True)
