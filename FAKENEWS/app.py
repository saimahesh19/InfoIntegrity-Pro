# from flask import Flask, render_template, request, jsonify
# from googletrans import Translator
# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
# from sklearn.pipeline import Pipeline
# from sklearn.linear_model import LogisticRegression
# from langdetect import detect

# app = Flask(__name__)

# # Load your fake news detection model
# dataset_path = 'combined_dataset.csv'  # Update with the correct path
# data = pd.read_csv(dataset_path)
# data['news'].fillna("", inplace=True)
# X = data['news']
# y = data['label']
# fake_news_pipeline = Pipeline([
#     ('vect', CountVectorizer()),
#     ('tfidf', TfidfTransformer()),
#     ('clf', LogisticRegression())
# ])
# fake_news_pipeline.fit(X, y)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/detect_fake_news', methods=['POST'])
# def detect_fake_news():
#     try:
#         website_url = request.form['website_url']

#         if not website_url:
#             return jsonify({'error': 'Please enter a valid website URL'})

#         # Get the headline from the website
#         headline = get_headline_from_website(website_url)

#         if headline:
#             # Detect the language of the headline
#             detected_lang = detect(headline)

#             # Translate the headline to English if it's not already in English
#             if detected_lang != 'en':
#                 translator = Translator()
#                 translated = translator.translate(headline, src=detected_lang, dest='en')
#                 english_text = translated.text
#             else:
#                 english_text = headline

#             result = {
#                 'detected_lang': detected_lang,
#                 'translated_headline': english_text,
#                 'original_text': headline
#             }

#             # Use the fake news detection model
#             predicted_label = fake_news_pipeline.predict([english_text])
#             if predicted_label[0] == 0:
#                 result['classification'] = 'REAL'
#             else:
#                 result['classification'] = 'FAKE'

#             return jsonify(result)
#         else:
#             return jsonify({'error': 'No headline found on the specified website'})
#     except Exception as e:
#         return jsonify({'error': 'An error occurred during translation and detection'})


# def get_headline_from_website(url):
#     # Send an HTTP GET request to the specified URL
#     response = requests.get(url)

#     if response.status_code == 200:
#         # Parse the HTML content of the page
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find and extract the headline
#         headline = None

#         # You'll need to inspect the website's HTML structure to determine the proper selector
#         # and update the code below accordingly.

#         # Example: if the headline is in an <h1> element
#         headline_element = soup.find('h1')
#         if headline_element:
#             headline = headline_element.text

#         return headline
#     else:
#         print("Failed to retrieve the web page. Status code:", response.status_code)
#         return None

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from bs4 import BeautifulSoup
import requests
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from langdetect import detect

app = Flask(__name__)

# Load your fake news detection model
dataset_path = 'combined_dataset.csv'  # Update with the correct path
data = pd.read_csv(dataset_path)
data['news'] = data['news'].fillna("")
X = data['news']
y = data['label']
fake_news_pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LogisticRegression())
])
fake_news_pipeline.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_fake_news', methods=['POST'])
def detect_fake_news():
    try:
        website_url = request.form['website_url']

        if not website_url:
            return jsonify({'error': 'Please enter a valid website URL'})

        # Get the headline from the website
        headline = get_headline_from_website(website_url)

        if headline:
            # Detect the language of the headline
            detected_lang = detect(headline)

            # Translate the headline to English if it's not already in English
            if detected_lang != 'en':
                translator = Translator()
                translated = translator.translate(headline, src=detected_lang, dest='en')
                english_text = translated.text
            else:
                english_text = headline

            result = {
                'detected_lang': detected_lang,
                'translated_headline': english_text,
                'original_text': headline
            }

            # Use the fake news detection model
            predicted_label = fake_news_pipeline.predict([english_text])
            if predicted_label[0] == 0:
                result['classification'] = 'REAL'
            else:
                result['classification'] = 'FAKE'

            return jsonify(result)
        else:
            return jsonify({'error': 'No headline found on the specified website'})
    except Exception as e:
        return jsonify({'error': 'An error occurred during translation and detection'})


def get_headline_from_website(url):
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and extract the headline
        headline = None

        # You'll need to inspect the website's HTML structure to determine the proper selector
        # and update the code below accordingly.

        # Example: if the headline is in an <h1> element
        headline_element = soup.find('h1')
        if headline_element:
            headline = headline_element.text

        return headline
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)
        return None

if __name__ == '__main__':
    app.run(debug=True)