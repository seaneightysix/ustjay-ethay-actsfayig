import os

import requests
from flask import Flask, send_file, Response, redirect, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def get_pig_latin(fact):

    url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    data = {"input_text": fact}
    res = requests.post(url, data, allow_redirects=False)
    link = res.headers["Location"]

    return link

@app.route('/', methods = ['GET'])
def home():

    fact = get_fact()
    link = get_pig_latin(fact)

    return render_template('home.jinja2', fact=fact, link=link)
    #return redirect(link)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

