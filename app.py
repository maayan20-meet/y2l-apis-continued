import requests
import json
from flask import Flask, render_template, request
app = Flask(__name__)

headers = {'Authorization': 'Key 91d90c19038d4629ad99b8e84c6df34f'}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
    image_url = request.form['url-input']
    
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
    
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}

    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    info = json.loads(response.content)

    infoo = info['outputs']
    infod = infoo[0]['data']
    infoc = infod['concepts']

    hasHuman = False

    for item in infoc:
    	print('b')
    	if item['name'] == 'people':
    		print('a')
    		hasHuman = True

    firstItem = infoc[0]

    return render_template('home.html', results=json.loads(response.content), hasHuman = hasHuman, main=firstItem['name'])

if __name__ == '__main__':
    app.run(debug=True)