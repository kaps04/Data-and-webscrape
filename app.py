from flask import Flask
import json

app= Flask(__name__)

@app.route("/")
def home():
     with open('data.json') as f:
        return json.load(f)
   
if __name__ =='__main__':
    app.run(debug=True, port=8000) 
    
    
