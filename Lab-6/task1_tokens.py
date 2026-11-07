
import re

sample_texts=[
    "Hello, how are you?",
    "I don't like cold coffe.",
    "Contact me at student@gmail.com",
    "My course code is CS4944",
    "",
    "میرا نام نین ہے"
]

for text in sample_texts:
    space_tokens= text.split()
    regex_tokens_list= re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
    print("Original: ", text)
    print("Whitespace tokens:", space_tokens, "Count:", len(space_tokens))
    print("Regex tokens:", regex_tokens_list, "Count:", len(regex_tokens_list))
    print("---------")
print("\n Model Tokenizer (tiktoken): ")    
try:
    import tiktoken
    gpt_tokenizer=tiktoken.get_encoding("cl100k_base")
    for text in ["Hello, how are you?", "I don't like cold cofee,"]:
        ids=gpt_tokenizer.encode(text)
        print("Original:", text)
        print(" Model tokens:", ids, "Count:", len(ids))
        print("-----------")
except ImportError:
    print("tiktoken is not installed")
    print("install it with: pip install tiktoken")

print("Explanation:")
print("1. In whitespace splitting, punctuation stays with the word, like Hello, is one token. In regex, comma becomes a separate token.")
print("2. Regex breaks don't into 3 parts and email into parts too, while whitespace keeps them as 1 token.")
print("CS4944 stays as one token in both methods because it has no space or punctuation.")
print("Urdu text works with regex because \\w also matches Urdu letters, but it is still not perfect for all languages.")
print("Normalization Risk: If we lowercase everything, US (country) and us (pronoun) become same, so meaning changes.")
print("Note: This regex is not a complete multilingual tokenizer.")