from flask import Flask, request, render_template
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import webbrowser
import threading
import time
import nltk

# Set NLTK data path (if necessary)
nltk.data.path.append("C:\\Users\\gandl\\AppData\\Roaming\\nltk_data")

# Ensure NLTK datasets are downloaded
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Initialize stopwords
stop_words = set(stopwords.words('english'))

def normalize_text(text):
    """
    Normalize text by tokenizing, lowercasing, and removing punctuation.
    Stopword removal is disabled for better context preservation.
    """
    # Tokenization and lowercase conversion
    tokens = word_tokenize(text.lower())
    # Remove punctuation only (keep stopwords)
    tokens = [word for word in tokens if word.isalnum()]
    return " ".join(tokens)

def check_plagiarism(text1, text2):
    """
    Compare two texts using TF-IDF and cosine similarity.
    """
    # Normalize texts
    text1_normalized = normalize_text(text1)
    text2_normalized = normalize_text(text2)
    print("Normalized Text 1:", text1_normalized)
    print("Normalized Text 2:", text2_normalized)
    
    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1_normalized, text2_normalized])
    
    # Calculate cosine similarity
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    print("Similarity Score:", similarity_score)
    
    # Determine if the texts are plagiarized
    plagiarism_threshold = 0.3  # Lowered threshold for better sensitivity
    is_plagiarized = similarity_score >= plagiarism_threshold
    return is_plagiarized, similarity_score

def check_plagiarism_with_document(input_text, document_path):
    """
    Compare input text with the entire document.
    """
    try:
        # Read the document
        with open(document_path, 'r', encoding='utf-8') as file:
            document_text = file.read()
        
        # Compare input text with the entire document
        is_plagiarized, similarity_score = check_plagiarism(input_text, document_text)
        return is_plagiarized, similarity_score
    except FileNotFoundError:
        print(f"Error: File not found at {document_path}")
        return False, 0
    except Exception as e:
        print(f"Error: {e}")
        return False, 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text1 = request.form['text1']
        document_path = r'C:\Users\gandl\OneDrive\Desktop\Project\document.txt'  # Path to the document file
        is_plagiarized, similarity_score = check_plagiarism_with_document(text1, document_path)
        return render_template('index.html', is_plagiarized=is_plagiarized, similarity_score=similarity_score)
    return render_template('index.html', is_plagiarized=None, similarity_score=None)

def open_browser():
    # Wait for the server to start
    time.sleep(1)
    # Open the browser
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Start the browser in a separate thread
    threading.Thread(target=open_browser).start()
    # Run the Flask app
    app.run(debug=True)
