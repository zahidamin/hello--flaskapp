from flask import Flask, request
from tensorflow import keras
import numpy as np


app = Flask(__name__)
m = keras.models.load_model('abc.h5')
@app.route("/")
def index():
    return ''' 
    <h1>User Information</h1>
    <form action="/info" method="POST"> 
    <input type="text" name="height" placeholder="User height">
    
    <input type="submit" value="Send">

    </form>
    '''


@app.route("/info", methods=["GET","POST"])
def info():
    if request.method == "GET":
       pass
    elif request.method == "POST":
        input = [float(x) for x in request.form.values()]
        final_input = [np.array(input)]
        # prediction = model.predict(final_input)
        a = m.predict(final_input)
        # a = m.predict([[request.form['height']]])
        return "Data is showing with POST method {} Now prediction is: {}".format(request.form['height'],a)
        # return 'Predicted Weight in KGs :{}'.format(a)

app.run(debug=True)    