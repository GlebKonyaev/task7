import src.example_package_gleb_koniaev.monaco.cli
import sys
from flask import Flask, jsonify, render_template
import src.example_package_gleb_koniaev.monaco.cli_for_html as html
import src.example_package_gleb_koniaev.monaco.report_printer as form
import sys
import os
import re

sys.argv = ["cli.py", "--files", "./files"]

ab = src.example_package_gleb_koniaev.monaco.cli.main()
print(type(ab))


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
print(abbreviations)
