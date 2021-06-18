
from flask import Flask, render_template, json, request
site = Flask(__name__)


@site.route('/')
def visualize():
    return render_template('base_space.html')


if __name__ == '__main__':
    site.run(debug=True)
