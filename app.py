from flask import Flask, render_template, request
from edamam import recipe_search

app = Flask(__name__)
app.config.from_object('config')
app_id = app.config["APP_ID"]
app_key = app.config["APP_KEY"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipe')
def show_recipe():
    ingredient = request.args.get('ingredient')
    health = request.args.get('health')
    preference = request.args.get('preference')
    hits = recipe_search(ingredient, health, preference,app_id,app_key)
    # set second argument to pass the data
    return render_template('recipe.html', hits=hits)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tips')
def tips():
    return render_template('tips.html')

# it checks if a module is being imported or not
if __name__ == '__main__':
    app.run(debug=True)  # set debug=True so it's auto updated and we don't have to restart the server every time
