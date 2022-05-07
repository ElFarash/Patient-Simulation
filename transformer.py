
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers import pipeline

def load_model():
	tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-distilled-squad")
	model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased-distilled-squad")
	qa = pipeline("question-answering", model=model, tokenizer=tokenizer)
	return qa

def QA():
	# Open and read the article
	question = "What is the capital of the Netherlands?"
	question2= "what is the busiest seaport in Europe?"
	context = r"The four largest cities in the Netherlands are Amsterdam, Rotterdam, The Hague and Utrecht.[17] Amsterdam is the country's most populous city and nominal capital,[18] while The Hague holds the seat of the States General, Cabinet and Supreme Court.[19] The Port of Rotterdam is the busiest seaport in Europe, and the busiest in any country outside East Asia and Southeast Asia, behind only China and Singapore."

	# Generating an answer to the question in context
	answer = qa(question=question, context=context)
	answer2 = qa(question=question2, context=context)
	# Print the answer
	print(f"Question: {question}")
	print(f"Answer: '{answer['answer']}' with score {answer['score']}")

	print(f"Question: {question2}")
	print(f"Answer: '{answer2['answer']}' with score {answer2['score']}")