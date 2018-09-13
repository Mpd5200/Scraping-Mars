from flask import flask, render_template,redirect
from flask_pymongo import Pymongo
import scrape

app = Flask(__name__)

app.config["mongo"] = "mongodb://localhost:27017//mars"
mongo = PyMongo(app)

@app.route("/")
def home():
    mars = mongo.db.collection.find()
    return render_template("index.html", Data = mars)

app.route("/scrape")
def scraper():
    mongo.db.collection.remove({})
    
    mars_fact = scrape.scrape

    news = {"news_title": mars_fact[0],
            "news_p" : mars_fact[1]}
    mongo.db.collection.insert_one(news)

    featured_image = {"featured_image_url": mars_fact[2]}
    mongo.db.collection.insert_one(featured_image)

    mars_weather = {"mars_weather": mars_fact[3]}
    mongo.db.collection.insert_one(mars_weather)
    
    fact_table = {"fact_table": mars_fact4]}
    mongo.db.collection.insert_one(fact_table)

    hemisphere= {"emispheres": mars_fact[5]}
    mongo.db.collection.insert_one(hemisphere)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True) 