# Quick Start Guide - Grammar Checker

## ⚡ Getting Started in 3 Steps

### Step 1: Activate Virtual Environment
Open terminal in the project directory and run:

**Windows (Git Bash/PowerShell):**
```bash
./grammer/Scripts/activate
```

**Linux/Mac:**
```bash
source grammer/bin/activate
```

### Step 2: Run the Application
```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
```

### Step 3: Open in Browser
Navigate to: **http://localhost:5000**

---

## 🚀 How to Use the Grammar Checker

1. **Paste Your Text**
   - Click in the text area
   - Paste or type your text

2. **Check Grammar**
   - Click "Check Grammar" button
   - Or press Ctrl+Enter (Windows/Linux) / Cmd+Enter (Mac)

3. **Review Results**
   - Check your score and grade
   - Review errors found
   - Read suggestions for improvement
   - Copy the corrected text

---

## 📊 Understanding Your Score

Your score is based on the number and severity of errors:

| Score | Grade | Status |
|-------|-------|--------|
| 90-100 | A | Excellent - Very few or no errors |
| 80-89 | B | Good - Minor errors |
| 70-79 | C | Fair - Some errors |
| 60-69 | D | Poor - Multiple errors |
| Below 60 | F | Very Poor - Many errors |

---

## ✅ What Gets Checked

- ✏️ **Spelling** - Misspelled words
- 📍 **Punctuation** - Missing commas, periods, etc.
- 🔤 **Capitalization** - Improper capitalization
- 🔄 **Tense** - Verb tense consistency
- 📝 **Grammar** - General grammar rules
- 🎯 **Word Choice** - Confusing word pairs (their/there, etc.)

---

## 🛠️ Troubleshooting

**Problem**: Application won't start
- Check if port 5000 is available
- Ensure virtual environment is activated
- Verify all packages are installed: `pip list`

**Problem**: Grammar checker not working
- Try refreshing the page (F5)
- Clear browser cache
- Make sure Flask is still running

**Problem**: Port 5000 already in use
- Change port in app.py: Find `app.run(debug=True, port=5000)` and change 5000 to another number like 5001

---

## 📁 Project Files

- **app.py** - Main Flask application with grammar checking logic
- **templates/index.html** - Web interface
- **static/style.css** - Styling and design
- **static/script.js** - Interactive features
- **grammer/** - Virtual environment with all dependencies

---

## 💡 Tips for Best Results

1. Use longer texts (3+ sentences) for more accurate checking
2. The corrected text shows the most likely corrections
3. Read suggestions carefully - they're tailored to your text's errors
4. Use the copy button to save corrected text
5. Always review corrections before using them

---

## 🔐 Privacy

- All checking is done locally
- No data is sent to external servers
- Your text is not stored anywhere
- Everything is processed in-memory

---

## 📞 Need Help?

Refer to README.md for detailed documentation or modify the Flask app for custom configurations.

**Enjoy using Grammar Checker! 🎉**
