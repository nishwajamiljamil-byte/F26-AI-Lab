from task2_chunks import documents, word_chunks
from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

doc_records= []
for doc_id, text in documents.items():
    extracted_chunks= word_chunks(text, 40, 10, doc_id)
    for chunk in extracted_chunks:
        doc_records.append({
            "id": chunk["id"],
            "source": doc_id,
            "start": chunk["start"],
            "end": chunk["end"],
            "text": chunk["text"]
        })
corpus_texts =[item["text"] for item in doc_records]
test_queries=[
    "Can students get extra time due to medical leave?",
    "How many days can library books be borrowed?",
    "What percentage of attendance is required?"
]
tfidf_vec= TfidfVectorizer()
tfidf_matrix=tfidf_vec.fit_transform(corpus_texts)
model=SentenceTransformer("all-MiniLM-L6-v2")
chunk_embeddings=model.encode(corpus_texts, convert_to_tensor=True)
for query in test_queries:
    print("\n====================")
    print("Testing Query:", query)
    query_vector =tfidf_vec.transform([query])
    tfidf_scores =cosine_similarity(query_vector, tfidf_matrix)[0]
    tfidf_best= tfidf_scores.argmax()
    print("\nTF-IDF Result:")
    print("Chunk ID:", doc_records[tfidf_best]["id"])
    print("Evidence:", doc_records[tfidf_best]["text"])
    query_embedding =model.encode(query, convert_to_tensor=True)
    scores =util.cos_sim(query_embedding, chunk_embeddings)[0]
    best= int(scores.argmax())
    print("\nEmbedding Result:")
    print("Chunk ID:" , doc_records[best]["id"])
    print("Similarity Score:", round(float(scores[best]), 3))
    print("Source Doc:", doc_records[best]["source"])
    print("Offsets (Start-End):", doc_records[best]["start"], "End:", doc_records[best]["end"])
    print("Original Evidence:", doc_records[best]["text"])