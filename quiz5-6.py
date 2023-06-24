from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cats')
def cats():
    url = "http://meow-cats.com/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        cat_images = soup.find_all("img", class_="cat-image")
        return render_template('cats.html', cat_images=cat_images)
    else:
        return "Something went wrong"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if requests.method == 'POST':
        search_query = requests.form.get('search')
        return render_template('search_results.html', search_query=search_query)
    else:
        return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)