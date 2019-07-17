import os
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import time



weight_backup = "weather_weight.h5"
learning_rate = 0.001

def build_model():
    model = Sequential()
    model.add(Dense(24, input_dim=2, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(2, activation='linear'))
    model.compile(loss='mean_squared_error', optimizer=Adam(lr=learning_rate))

    if os.path.isfile(weight_backup):
        model.load_weights(weight_backup)
    return model


def create_dataset(look_back=1):
    load_memory = open("memory.pickle", "rb")
    memory = pickle.load(load_memory)
    dataX, dataY = [], []
    for i in range(len(memory) - look_back - 1):
        dataX.append(memory[i])
        dataY.append(memory[i + look_back])
    return np.array(dataX), np.array(dataY)

while True:
    state, target = create_dataset()
    model1 = build_model()
    model1.fit(state, target, epochs=1, batch_size=60, verbose=2)
    model1.save_weights(weight_backup)
    model1.save("model.h5")
    time.sleep(60)

