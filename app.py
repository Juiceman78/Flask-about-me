from flask import Flask, render_template

app = Flask(__name__)

# Sample movie data
things = [
    {"id": 1, "title": "Volleyball", "description": "I like volleyball"},
    {"id": 2, "title": "Snowboarding", "description": "I'm tuff at snowboarding"},
    {"id": 3, "title": "Ashton Hall", "description": "Saratoga Water"}
]

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', things=things) 


app.run(debug=True)