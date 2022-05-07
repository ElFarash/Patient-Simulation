import pyaudio
import wave
import os 

def record():
	arr = os.listdir("Questions")
	Question_number = len(arr)+1

	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 200
	WAVE_OUTPUT_FILENAME = f"Questions/Q{Question_number}.wav"


	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                frames_per_buffer=CHUNK)

	print("* * Please Start Asking Your Question, when done press Ctrl-C ...")

	frames = []

	try : 
		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		    data = stream.read(CHUNK)
		    frames.append(data)
	
	except KeyboardInterrupt:
		stream.stop_stream()
		stream.close()
		p.terminate()

		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()

		return WAVE_OUTPUT_FILENAME