Objective

The goal of this project is to build a web-based plagiarism detection tool that compares a user’s input text with the content of a reference document and identifies similarities. It helps in detecting copied or duplicated content using NLP and machine learning techniques.

🔹 Key Features

Web Interface (Flask App)

Users can enter a text snippet into a web form.

The application compares this text with the content of a reference file (document.txt).

Displays whether the input text is plagiarized along with a similarity score.

Text Normalization

Input text and reference text are normalized for better comparison:

Converted to lowercase.

Tokenized into words.

Punctuation removed.

Stopwords are kept to preserve context (important for plagiarism detection).

Plagiarism Detection

Uses TF-IDF (Term Frequency–Inverse Document Frequency) to represent text.

Uses Cosine Similarity to measure similarity between input and reference text.

A threshold (0.3 in this code) is used to decide if plagiarism is detected.

Plagiarism with Document File

Reads the entire document.txt file.

Compares user’s input with the whole document.

Returns:

✅ Plagiarized (if similarity ≥ threshold)

❌ Not Plagiarized (if similarity < threshold).

Browser Auto-Open

The app automatically opens in the browser when started.

🔹 Technologies Used

Python – Main programming language.

Flask – For building the web interface.

NLTK – For text tokenization and stopwords.

Scikit-learn – For TF-IDF vectorization and cosine similarity.

HTML (Jinja templates) – For displaying results in the browser.

🔹 Workflow

User enters a text in the input box.

Application loads a reference document (document.txt).

Both texts are normalized (lowercased, tokenized, punctuation removed).

TF-IDF is applied to extract text features.

Cosine similarity is calculated between input and reference document.

If similarity ≥ 0.3 → plagiarism detected.

Result is displayed on the web page with similarity score.

🔹 Example

Reference document (document.txt):
Artificial Intelligence is transforming industries worldwide.

User Input 1:
AI is transforming industries worldwide.

Normalized Texts → similar word distribution.

Similarity Score → 0.82 (high).

Result: ✅ Plagiarized

User Input 2:
The cat sat on the mat.

Very different from document.

Similarity Score → 0.05

Result: ❌ Not Plagiarized
