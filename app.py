from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/jokes', methods=['GET'])
def get_jokes():
    response = requests.get('https://v2.jokeapi.dev/joke/Any?type=single')
    data = response.json()
    answer = {'joke': data['joke']}
    return jsonify(answer)

@app.route('/quotes', methods=['GET'])
def get_quotes():
    response = requests.get('https://zenquotes.io/api/random')
    data = response.json()[0]
    answer = {'quote': data['q'],
                'author': data['a']
              }
    return jsonify(answer)

if __name__ == '__main__':
    app.run(debug=False)