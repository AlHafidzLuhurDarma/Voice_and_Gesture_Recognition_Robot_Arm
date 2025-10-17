from vosk import Model, KaldiRecognizer
import pyaudio
import json
from code_list import *
import serial

arduinoData = serial.Serial('com3', 9600)

FRAMES_PER_BUFFER = 3200 # or 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
FRAME_RATE = 16000


model = Model(r"C:\Users\user\Downloads\Compressed\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, FRAME_RATE)

mic = pyaudio.PyAudio()
stream = mic.open(
    format = FORMAT,
    channels = CHANNELS,
    rate=FRAME_RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)
print('Start Recording')
stream.start_stream()

while True:
    data = stream.read(FRAMES_PER_BUFFER)
    if recognizer.AcceptWaveform(data):
        myText = recognizer.Result()
        myText = json.loads(myText)
        print(myText["text"])
        text = myText['text']
        cmd = find_word(text)
        arduinoData.write(cmd.encode())
        if myText['text'] == 'stop':
            break