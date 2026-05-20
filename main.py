import pyaudio as pa
import numpy as np
import sounddevice as sd
import random as rnd


minorScaleCoefficient = [1, 1.122, 1.260, 1.335, 1.498, 1.682, 1.888, 2.000 ]

for i in range (0,8,1):

    sampleRate = 44100
    duration = 0.5
    frequency = 440 * minorScaleCoefficient[i]

    t = np.linspace(0, duration, int(sampleRate * duration), endpoint = False)

    audioSignal = np.sin(2 * np.pi * frequency * t)

    sd.play(audioSignal, sampleRate)

    sd.wait()