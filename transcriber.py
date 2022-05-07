import deepspeech
import wave
import numpy as np


model_path = 'models/deepspeech-0.9.3-models.pbmm'
scorer_path = 'models/deepspeech-0.9.3-models.scorer'


ds = deepspeech.Model(model_path)
ds.enableExternalScorer(scorer_path)


def speech_text(splited_audio):

    fin = wave.open(splited_audio, 'rb')

    audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

    fin.close()

    transcript = ds.stt(audio)

    return transcript

