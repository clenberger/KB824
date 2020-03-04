from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    """Return gallery."""
    return render_template('gallery.html')

@app.route('/highlights')
def highlight():
    """Return highlights."""
    return render_template('highlights.html')
