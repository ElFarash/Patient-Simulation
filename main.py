from transcriber import speech_text
from audio_recorder import record 
from transformer import load_model 
import librosa
import soundfile
from pydub import AudioSegment
import time


file = open("context.txt")
context = file.read().replace("\n", " ")
file.close()

print("Model loading ...")
start = time.time()
qa = load_model()
end = time.time()
model_time = end - start 
print(f'Model loaded in {model_time}')


while(True):
	check = input("Press 1 to Record the Question, 2 to Write the Question, 3 to Exit: ")

	if(check == '1'):
		record_path= record()
		
		# Read and rewrite the file with soundfile
		x,_ = librosa.load(record_path , sr=16000)
		soundfile.write(record_path, x, 16000)
		newAudio = AudioSegment.from_wav(record_path)
		newAudio.export(record_path, format="wav")
		
		#deep speech model
		transcript = speech_text(record_path)
		print(f'Your Question is: {transcript} ?')

		# question answering model
		answer = qa(question=transcript, context=context)
		print(f"Patient Answer: '{answer['answer']}' with score {answer['score']}")

	elif(check == '2'):
		q = input("Write the Question to the Patient: ")
		answer = qa(question=q, context=context)
		print(f"Patient Answer: '{answer['answer']}' with score {answer['score']}")

	else:
		exit()








