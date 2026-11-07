from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
faq_data=[{
        "question": "What is artificial intelligence?",
        "answer": "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.",
        "source": "AI Lecture Notes"
    },
    {
        "question": "What is machine learning?",
        "answer": "Machine Learning is a part of AI that allows computers to learn from data.",
        "source": "Machine Learning Lecture Notes"
    }
]
questions_list=[item["question"] for item in faq_data]
vectorizer= TfidfVectorizer()
faq_vectors= vectorizer.fit_transform(questions_list)
print("Welcome to the FAQ Chatbot!")
print("Type your question below (or type 'exit' to quit).\n")
while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    if user_input == "":
        print("Bot: Please enter a question.")
        continue
    exact_match = False
    for entry in faq_data:
        if user_input.lower() == entry["question"].lower():
            print("Bot:", entry["answer"])
            print("Source:", entry["source"])
            exact_match = True
            break
    if exact_match:
        continue
    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, faq_vectors)
    best_match = similarity.argmax()
    score = similarity[0][best_match]
    if score >= 0.20:
        print("Bot: Did you mean:?")
        print("Suggestion:", questions_list[best_match])
        confirm = input("Bot: Is this correct? (yes/no): ")
        if confirm.lower() == "yes":
            print("Bot:", faq_data[best_match]["answer"])
            print("Source:", faq_data[best_match]["source"])
        else:
            print("Bot: Please ask another question.")
    else:
        print("Bot: Sorry, I don't have an answer for this question.")