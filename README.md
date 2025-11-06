# Fake News Detection System

An intelligent web application that analyzes news headlines from any website URL and determines their authenticity using machine learning. The system supports multi-language detection and automatically translates non-English content for analysis.

## 🎯 Overview

This project combines natural language processing, machine learning, and web scraping to combat misinformation by providing real-time fake news detection. Simply input a news article URL, and the system will extract the headline, detect its language, translate it if necessary, and classify it as REAL or FAKE using a trained logistic regression model.

## ✨ Features

- **URL-Based Analysis**: Analyze news articles directly from their web URLs
- **Multi-Language Support**: Automatically detects and translates headlines in various languages
- **Machine Learning Classification**: Uses TF-IDF vectorization and Logistic Regression for accurate predictions
- **Real-Time Processing**: Instant results with detailed analysis breakdown
- **Clean Modern UI**: Responsive interface built with HTML, CSS, and JavaScript
- **Headline Extraction**: Intelligent web scraping to extract article headlines
- **Language Detection**: Automatic language identification using langdetect

## 🛠️ Technology Stack

### Backend
- **Python 3.x**
- **Flask**: Lightweight web framework for API endpoints
- **scikit-learn**: Machine learning library for model training and prediction
- **BeautifulSoup4**: HTML parsing and web scraping
- **googletrans**: Language translation API
- **langdetect**: Language detection library
- **pandas**: Data manipulation and analysis
- **requests**: HTTP library for web scraping

### Frontend
- **HTML5**: Structure and semantic markup
- **CSS3**: Modern styling and responsive design
- **JavaScript**: Interactive functionality and AJAX requests

### Machine Learning Pipeline
- **CountVectorizer**: Text tokenization and feature extraction
- **TfidfTransformer**: Term frequency-inverse document frequency weighting
- **Logistic Regression**: Binary classification model

## 📋 Prerequisites

```bash
Python 3.7+
pip (Python package manager)
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask googletrans==4.0.0-rc1 beautifulsoup4 requests pandas scikit-learn langdetect
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Prepare Dataset

Ensure you have the `combined_dataset.csv` file in the project root directory with the following structure:

```csv
news,label
"Headline text here",0
"Another headline",1
```

- **Label 0**: REAL news
- **Label 1**: FAKE news

## 🎮 Usage

### 1. Start the Flask Server

```bash
python app.py
```

The application will start on `http://localhost:5000`

### 2. Access the Web Interface

Open your browser and navigate to:
```
http://localhost:5000
```

### 3. Analyze News Articles

1. **Enter URL**: Paste the full URL of a news article
2. **Submit**: Click the analyze button
3. **View Results**: See the classification, original headline, detected language, and English translation

## 📊 How It Works

### Step-by-Step Process

1. **URL Input**: User provides a news article URL
2. **Web Scraping**: BeautifulSoup extracts the headline from the webpage
3. **Language Detection**: System identifies the headline's language
4. **Translation**: If not in English, headline is translated using Google Translate
5. **Feature Extraction**: Text is converted to TF-IDF features
6. **Classification**: Logistic Regression model predicts REAL or FAKE
7. **Results Display**: User receives comprehensive analysis

### Machine Learning Model

The system uses a supervised learning pipeline:

```python
Pipeline([
    ('vect', CountVectorizer()),      # Convert text to word count vectors
    ('tfidf', TfidfTransformer()),    # Apply TF-IDF weighting
    ('clf', LogisticRegression())     # Binary classification
])
```

## 🌐 API Endpoints

### GET `/`
Returns the main application interface

**Response**: HTML page

### POST `/detect_fake_news`
Analyzes a news article URL for fake news detection

**Request Body** (form-data):
```
website_url: "https://example.com/news-article"
```

**Response** (JSON):
```json
{
  "detected_lang": "en",
  "translated_headline": "Breaking News: Major Event Occurs",
  "original_text": "Breaking News: Major Event Occurs",
  "classification": "REAL"
}
```

**Error Response**:
```json
{
  "error": "Error message description"
}
```

## 📁 Project Structure

```
fake-news-detector/
│
├── app.py                      # Main Flask application
├── combined_dataset.csv        # Training dataset
├── requirements.txt            # Python dependencies
│
├── templates/
│   └── index.html             # Frontend HTML interface
│
├── static/
│   ├── css/
│   │   └── style.css          # Styling
│   ├── js/
│   │   └── main.js            # JavaScript logic
│   └── assets/
│       └── images/            # Images and icons
│
└── README.md                  # Project documentation
```

## 🔍 Supported Languages

The system can detect and translate headlines from multiple languages including:
- English
- Spanish
- French
- German
- Italian
- Portuguese
- Hindi
- Chinese
- Japanese
- Arabic
- And many more...

## 🐛 Troubleshooting

### Common Issues

**Issue**: `googletrans` translation errors
```bash
# Solution: Install specific version
pip install googletrans==4.0.0-rc1
```

**Issue**: Website scraping fails
- **Cause**: Website structure doesn't contain `<h1>` tags
- **Solution**: Modify `get_headline_from_website()` to match target website's HTML structure

**Issue**: Model accuracy is low
- **Solution**: Retrain with a larger, more diverse dataset

**Issue**: Language detection fails
```bash
# Solution: Reinstall langdetect
pip uninstall langdetect
pip install langdetect
```

## 📈 Model Performance

The model's performance depends on the quality and size of the training dataset. To improve accuracy:

1. **Increase Dataset Size**: More training examples lead to better generalization
2. **Balance Classes**: Ensure equal representation of REAL and FAKE news
3. **Feature Engineering**: Experiment with n-grams, word embeddings
4. **Hyperparameter Tuning**: Optimize LogisticRegression parameters
5. **Cross-Validation**: Use k-fold validation to assess model robustness

## 🔒 Security Considerations

- **Input Validation**: Always validate and sanitize user-provided URLs
- **Rate Limiting**: Implement rate limiting to prevent abuse
- **HTTPS**: Use HTTPS in production environments
- **CORS**: Configure Cross-Origin Resource Sharing appropriately
- **Error Handling**: Never expose sensitive error details to users

## 🚧 Future Enhancements

- [ ] Add support for full article analysis (not just headlines)
- [ ] Implement deep learning models (BERT, GPT) for improved accuracy
- [ ] Create user authentication and history tracking
- [ ] Add confidence scores for predictions
- [ ] Implement real-time fact-checking with external APIs
- [ ] Support for social media post analysis
- [ ] Browser extension for instant verification
- [ ] Mobile application development
- [ ] Multi-source verification and credibility scoring
- [ ] Export reports as PDF

## 📊 Dataset Information

The model is trained on a combined dataset of news articles labeled as REAL (0) or FAKE (1). For best results:

- **Minimum Dataset Size**: 10,000+ articles
- **Recommended Format**: CSV with 'news' and 'label' columns
- **Data Sources**: Kaggle, FakeNewsNet, LIAR dataset
- **Preprocessing**: Remove duplicates, handle missing values, balance classes

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Write clear commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **scikit-learn**: For providing excellent machine learning tools
- **Flask**: For the lightweight and flexible web framework
- **BeautifulSoup**: For powerful HTML parsing capabilities
- **Google Translate**: For multi-language support
- **Open Source Community**: For inspiration and resources

## 📚 References

- [Fake News Detection using Machine Learning](https://www.kaggle.com/c/fake-news)
- [TF-IDF Vectorization](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting)
- [Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## 📞 Support

For questions, issues, or suggestions:

- **GitHub Issues**: [Create an issue](https://github.com/yourusername/fake-news-detector/issues)
- **Email**: your.email@example.com
- **Documentation**: Check the [Wiki](https://github.com/yourusername/fake-news-detector/wiki)

## 📝 Changelog

### Version 1.0.0 (Current)
- Initial release
- Basic fake news detection functionality
- Multi-language support
- Web scraping capabilities
- RESTful API endpoints

---

⭐ **If you find this project helpful, please consider giving it a star!**

**Made with ❤️ for a more informed world**

## 🎓 Educational Use

This project is ideal for:
- Machine Learning students learning NLP and classification
- Web development learners exploring Flask applications
- Data Science enthusiasts working on real-world problems
- Researchers studying misinformation detection
- Developers building content verification systems

---

**Disclaimer**: This tool is designed for educational and research purposes. While it aims to detect fake news, it should not be the sole source for determining news authenticity. Always verify information from multiple credible sources.
