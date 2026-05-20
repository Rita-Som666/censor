import pyaudio
import numpy as np
import sounddevice as sd
import vosk
import json
import sys

# Проверка Vosk
#if not vosk.Model.exists("model"):
#    print("Модель Vosk не найдена в папке 'model'")
#    sys.exit(1)

model = vosk.Model("model")
rec = vosk.KaldiRecognizer(model, 16000)

# Открытие микрофона через PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=4000)

print("Говорите что-нибудь... Для выхода нажмите Ctrl+C")

try:
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "")
            if text:
                print(f"Распознано: {text}")
        else:
            partial = json.loads(rec.PartialResult())
            if partial.get("partial"):
                print(f"\r[частично]: {partial['partial']}", end="")
except KeyboardInterrupt:
    print("\nВыход")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()