# Grammar Checker Website - Emergency Engineer Product

A web-based grammar checking tool built with Flask that analyzes text for grammatical errors, spelling mistakes, and provides improvement suggestions.

## Features

✅ **Grammar Checking** - Detects spelling errors, punctuation issues, and common grammar mistakes
✅ **Text Correction** - Provides a corrected version of the text
✅ **Error Highlighting** - Lists all errors with categories and suggestions
✅ **Scoring System** - Assigns an overall score (0-100) and grade (A-F) based on grammar accuracy
✅ **Improvement Suggestions** - Provides actionable tips to improve writing quality
✅ **User-Friendly Interface** - Clean, organized layout with clear sections
✅ **Open Source** - Uses TextBlob for grammar checking (no Java required)

## Project Structure

```
grammer_cheker/
├── app.py                    # Flask application main file
├── templates/
│   └── index.html           # Main HTML template
├── static/
│   ├── style.css            # CSS styling
│   └── script.js            # JavaScript for interactivity
├── grammer/                 # Virtual environment
└── README.md                # This file
```

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup Steps

1. **Create and activate virtual environment:**
   ```bash
   cd d:/AIprojects/python2026/grammer_cheker
   python -m venv grammer
   ./grammer/Scripts/activate  # On Windows
   # or: source grammer/bin/activate  # On Linux/Mac
   ```

2. **Install dependencies:**
   ```bash
   pip install flask requests textblob nltk
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   Navigate to `http://localhost:5000` in your web browser

## Usage

1. **Enter Text**: Paste or type the text you want to check in the input area
2. **Check Grammar**: Click the "Check Grammar" button or press Ctrl+Enter
3. **Review Results**: 
   - View your overall score and grade
   - See the original text
   - Review all errors with categories and suggestions
   - View the corrected version
   - Read improvement suggestions
4. **Copy Results**: Use the copy button to copy the corrected text

## Scoring System

- **Score**: 0-100 points based on error density
- **Grade**: 
  - A: 90-100 (Excellent)
  - B: 80-89 (Good)
  - C: 70-79 (Fair)
  - D: 60-69 (Poor)
  - F: Below 60 (Very Poor)

## Error Categories Detected

- **Spelling**: Misspelled words
- **Punctuation**: Missing or misplaced punctuation
- **Capitalization**: Improper capitalization
- **Grammar**: General grammar issues
- **Subject-Verb Agreement**: Subjects and verbs not agreeing in number
- **Verb Tense**: Inconsistent or incorrect verb tenses
- **Article**: Incorrect use of 'a', 'an', 'the'
- **Word Confusion**: Commonly confused words (their/there, it's/its, etc.)

## Technologies Used

- **Backend**: Flask 3.1.2
- **Grammar Checking**: TextBlob 0.19.0, NLTK 3.9.2
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Python Version**: 3.13.2

## Features in Detail

### Original Text Display
Shows the exact text you submitted for grammar checking.

### Corrected Text
Provides an automatically corrected version of your text with suggestions applied.

### Error Details
Each error includes:
- Error message explaining the issue
- Category of error
- Suggestions for correction
- Position in text

### Improvement Suggestions
Personalized suggestions based on:
- Most common error types in your text
- Writing quality recommendations
- Tips for better grammar and style

## Keyboard Shortcuts

- **Ctrl+Enter** (Windows/Linux) or **Cmd+Enter** (Mac): Check grammar

## Browser Compatibility

- Chrome/Chromium (Recommended)
- Firefox
- Safari
- Edge
- Opera

## Notes

- The application requires an internet connection for optimal performance
- Results are processed locally; no data is stored on servers
- For best results, use texts with at least 3-5 words
- The grammar checker uses pattern matching and NLP algorithms for accuracy

## Development

To modify the application:

1. Edit `app.py` for backend logic
2. Edit `templates/index.html` for HTML structure
3. Edit `static/style.css` for styling
4. Edit `static/script.js` for frontend interactivity

## Troubleshooting

**Issue**: Port 5000 is already in use
**Solution**: Change the port in `app.py` (line: `app.run(debug=True, port=5000)`)

**Issue**: TextBlob not detecting errors
**Solution**: Ensure NLTK data is downloaded by running:
```python
import nltk
nltk.download('corpora/wordnet')
```

## Future Enhancements

- Integration with advanced NLP models
- Multiple language support
- Document upload functionality
- Real-time checking as you type
- Export results to PDF
- Plagiarism detection
- More detailed error explanations

## License

This project is open-source and available for educational and commercial use.

## Support

For issues or suggestions, please ensure:
1. Flask is running on http://localhost:5000
2. All dependencies are installed
3. You're using a supported browser
4. JavaScript is enabled in your browser

---

**Created**: February 2, 2026
**Project**: Emergency Engineer Product - Grammar Checker
**Version**: 1.0.0
