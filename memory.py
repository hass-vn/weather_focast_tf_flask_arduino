import numpy as np
import serial
from collections import deque
import pickle


ser = serial.Serial('/dev/ttyUSB0', 9600)
state = np.zeros(2)
memory = deque(maxlen=2000)

def read_arduino():
    value = ser.readline().decode()
    value = value.split()
    state[0] = float(value[0]) / 10
    state[1] = float(value[1]) / 10
    memory.append(state)

while True:
    read_arduino()
    save_memory = np.array(memory)
    memory_out = open("memory.pickle", "wb")
    pickle.dump(save_memory, memory_out)
    memory_out.close()

