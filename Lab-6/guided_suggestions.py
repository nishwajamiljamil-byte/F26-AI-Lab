from task2_chunks import documents, word_chunks
from sentence_transformers import SentenceTransformer, util

chunk_data= []
for doc_id,body_text in documents.items():
    chunks_list= word_chunks(body_text, 40, 10, doc_id)
    for chunk in chunks_list:
        chunk_data.append({
            "id": chunk["id"],
            "source": doc_id,
            "start": chunk ["start"],
            "end": chunk[ "end"],
            "text": chunk["text"]
        })
model= SentenceTransformer("all-MiniLM-L6-v2")
all_texts= [item["text"] for item in chunk_data]
chunk_embeddings= model.encode(all_texts, convert_to_tensor=True)
print("Guided Suggestions Started!")
user_query= input("\nEnter your question: ")
if user_query.strip() == "":
    print("Please enter a question.")
else:
    query_embedding= model.encode(user_query, convert_to_tensor=True)
    similarity_scores= util.cos_sim(query_embedding, chunk_embeddings)[0]
    top_3= similarity_scores.argsort(descending=True)[:3]
    print("\nSuggested Results:")
    for i in top_3:
        i = int(i)
        match_record= chunk_data[i]
        print("\nChunk ID:", match_record["id"])
        print("Similarity:", round(float(similarity_scores[i]), 3))
        print("similarity Source:", match_record["source"])
        print("Start:", match_record["start"], "End:", match_record["end"])
        print("Original Evidence:", match_record["text"])