import numpy as np
from tensorflow.keras.models import load_model
import pickle
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def weather_predict():
    model = load_model('model.h5')
    load_memory = open("memory.pickle", "rb")
    memory = pickle.load(load_memory)
    data = []
    data.append(memory[-1, :])
    data = np.array(data)
    pred = model.predict(data)
    return render_template('index.html', humidity = pred[0, 0], temperature = pred[0, 1])

if __name__ == '__main__':
    app.run()
