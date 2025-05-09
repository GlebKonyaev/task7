import src.example_package_gleb_koniaev.monaco.cli
import sys

sys.argv = ["cli.py", "--files", "./files"]

ab = src.example_package_gleb_koniaev.monaco.cli.main()
print(type(ab))
