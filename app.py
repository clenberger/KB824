from flask import Flask, render_template, redirect, request, url_for
import requests
import os 


app = Flask(__name__)

# home route 
@app.route('/')
def index():
    # display only 
    return render_template('index.html') #home page
    

# gallery route 
@app.route('/gallery')
def gallery():
    # this route display kobi gallery of photographs. Universal
    return render_template('gallery.html') #home page
    

# highlights 
@app.route('/highlights')
def highlights():
     # this route holds kobe highlights ( videos )
    return render_template('highlights.html') #home page
    




# main module page 
if __name__ == "__main__":
    app.run(debug=True)

# Todo:
# First Attempt fail
