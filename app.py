from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import re
from collections import Counter

app = Flask(__name__)

def calculate_score(original_text, errors):
    """
    Calculate grammar score based on errors found
    Score is out of 100
    """
    if not original_text.strip():
        return 0
    
    words = len(original_text.split())
    error_count = len(errors)
    
    # Error penalty per word
    error_percentage = (error_count / max(words, 1)) * 100
    
    # Score calculation: Start with 100, subtract error percentage
    score = max(0, 100 - error_percentage * 5)
    
    return round(score, 2)

def get_error_category(error_dict):
    """Categorize grammar errors"""
    rule_id = error_dict.get('rule_id', '').lower()
    category = error_dict.get('category', 'Grammar').lower()
    message = error_dict.get('message', '').lower()
    
    if 'spelling' in rule_id or 'spelling' in category or 'spelling' in message:
        return 'Spelling'
    elif 'agreement' in rule_id or 'subject' in message or 'verb' in message:
        return 'Subject-Verb Agreement'
    elif 'punctuation' in category or 'period' in message or 'comma' in message:
        return 'Punctuation'
    elif 'article' in rule_id or 'article' in message:
        return 'Article'
    elif 'tense' in rule_id or 'tense' in message:
        return 'Verb Tense'
    elif 'style' in rule_id or 'word choice' in message:
        return 'Style/Word Choice'
    elif 'capital' in category or 'capital' in message:
        return 'Capitalization'
    elif 'confusion' in rule_id:
        return 'Word Confusion'
    else:
        return 'Grammar'

def get_suggestions(errors):
    """Generate improvement suggestions based on error types"""
    suggestions = []
    error_categories = {}
    
    for error in errors:
        category = error.get('category', 'Grammar')
        if category not in error_categories:
            error_categories[category] = 0
        error_categories[category] += 1
    
    # Generate suggestions based on most common errors
    if 'Spelling' in error_categories:
        suggestions.append(f"✓ Review spelling: {error_categories['Spelling']} spelling error(s) found. Use a spell checker or dictionary.")
    
    if 'Punctuation' in error_categories:
        suggestions.append(f"✓ Check punctuation: {error_categories['Punctuation']} punctuation issue(s). Ensure proper comma placement and sentence endings.")
    
    if 'Subject-Verb Agreement' in error_categories:
        suggestions.append(f"✓ Subject-verb agreement: {error_categories['Subject-Verb Agreement']} issue(s). Ensure subjects and verbs agree in number.")
    
    if 'Verb Tense' in error_categories:
        suggestions.append(f"✓ Verb tense consistency: {error_categories['Verb Tense']} issue(s). Maintain consistent verb tenses throughout.")
    
    if 'Article' in error_categories:
        suggestions.append(f"✓ Article usage: {error_categories['Article']} issue(s). Check for correct use of 'a', 'an', and 'the'.")
    
    if 'Style/Word Choice' in error_categories:
        suggestions.append(f"✓ Word choice: {error_categories['Style/Word Choice']} suggestion(s). Consider using more precise or formal language.")
    
    if 'Capitalization' in error_categories:
        suggestions.append(f"✓ Capitalization: {error_categories['Capitalization']} issue(s). Ensure proper capitalization of sentences and proper nouns.")
    
    if 'Word Confusion' in error_categories:
        suggestions.append(f"✓ Word confusion: {error_categories['Word Confusion']} issue(s). Double-check commonly confused words (their/there, it's/its, etc.).")
    
    if 'Grammar' in error_categories:
        suggestions.append(f"✓ General grammar: {error_categories['Grammar']} issue(s). Review sentence structure and grammar rules.")
    
    # General suggestions
    total_errors = sum(error_categories.values())
    if total_errors == 0:
        suggestions.append("✓ Excellent! Your text has no grammatical errors.")
    else:
        suggestions.append(f"✓ Overall: Proofread carefully for {total_errors} identified error(s).")
        suggestions.append("✓ Read your text aloud to catch awkward phrasing.")
        suggestions.append("✓ Use simpler, more direct sentence structures where possible.")
    
    return suggestions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-grammar', methods=['POST'])
def check_grammar():
    data = request.json
    text = data.get('text', '')
    
    if not text.strip():
        return jsonify({
            'error': 'Please enter some text to check'
        }), 400
    
    try:
        # Use TextBlob for spell correction and analysis
        blob = TextBlob(text)
        
        # Get corrected text
        corrected_text = str(blob.correct())
        
        # Detect errors by comparing original and corrected versions
        errors = detect_errors(text, corrected_text, blob)
        
        # Calculate score
        score = calculate_score(text, errors)
        
        # Get suggestions
        suggestions = get_suggestions(errors)
        
        # Assign grade based on score
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        return jsonify({
            'original_text': text,
            'corrected_text': corrected_text,
            'errors': errors,
            'error_count': len(errors),
            'score': score,
            'grade': grade,
            'suggestions': suggestions
        })
    
    except Exception as e:
        return jsonify({
            'error': f'Error checking grammar: {str(e)}'
        }), 500

def detect_errors(original, corrected, blob):
    """
    Detect grammar and spelling errors by comparing original and corrected text
    """
    errors = []
    
    # Detect spelling errors by comparing original and corrected
    if original != corrected:
        # Find differences between original and corrected text
        original_words = original.split()
        corrected_words = corrected.split()
        
        # Build position map for original text
        pos = 0
        word_positions = []
        for word in original_words:
            word_pos = original.find(word, pos)
            if word_pos != -1:
                word_positions.append((word, word_pos, word_pos + len(word)))
                pos = word_pos + len(word)
            else:
                word_positions.append((word, pos, pos + len(word)))
        
        # Compare words
        for i, (orig_word, _, _) in enumerate(word_positions):
            if i < len(corrected_words):
                corr_word = corrected_words[i]
                if orig_word.lower() != corr_word.lower():
                    # Find position in original text
                    word_pos = original.lower().find(orig_word.lower())
                    if word_pos != -1:
                        error_info = {
                            'message': f'Spelling error: "{orig_word}" might be incorrect',
                            'from_pos': word_pos,
                            'to_pos': word_pos + len(orig_word),
                            'original': orig_word,
                            'suggestions': [corr_word],
                            'category': 'Spelling',
                            'rule_id': 'SPELLING'
                        }
                        errors.append(error_info)
    
    # Detect common grammar errors
    grammar_errors = check_common_grammar_errors(original)
    errors.extend(grammar_errors)
    
    # Detect capitalization errors
    capital_errors = check_capitalization(original)
    errors.extend(capital_errors)
    
    # Detect punctuation errors
    punct_errors = check_punctuation(original)
    errors.extend(punct_errors)
    
    # Remove duplicates based on position
    unique_errors = []
    seen_positions = set()
    for error in errors:
        pos_key = (error['from_pos'], error['to_pos'])
        if pos_key not in seen_positions:
            unique_errors.append(error)
            seen_positions.add(pos_key)
    
    return unique_errors

def check_common_grammar_errors(text):
    """Check for common grammar errors"""
    errors = []
    
    # Check for double spaces
    double_space_pattern = r'  +'
    for match in re.finditer(double_space_pattern, text):
        error_info = {
            'message': 'Double space detected',
            'from_pos': match.start(),
            'to_pos': match.end(),
            'original': match.group(),
            'suggestions': [' '],
            'category': 'Punctuation',
            'rule_id': 'DOUBLE_SPACE'
        }
        errors.append(error_info)
    
    # Check for missing space after punctuation
    missing_space_pattern = r'[.!?,;:](?=[A-Z])'
    for match in re.finditer(missing_space_pattern, text):
        pos = match.start() + 1
        error_info = {
            'message': 'Missing space after punctuation',
            'from_pos': pos,
            'to_pos': pos,
            'original': text[match.start():match.end()],
            'suggestions': [text[match.start()] + ' '],
            'category': 'Punctuation',
            'rule_id': 'MISSING_SPACE'
        }
        errors.append(error_info)
    
    # Check for common confusions
    confusion_pairs = [
        (r'\btheir\b', 'there/their', 'they\'re/their'),
        (r'\byour\b', 'your/you\'re', 'you\'re'),
        (r'\bits\b', 'it\'s/its', 'it\'s'),
        (r'\ba\s+([aeiou])', 'a/an', 'an'),
        (r'\ban\s+([^aeiou])', 'an/a', 'a')
    ]
    
    for pattern, issue, suggestion in confusion_pairs:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            error_info = {
                'message': f'Possible {issue} confusion',
                'from_pos': match.start(),
                'to_pos': match.end(),
                'original': match.group(),
                'suggestions': [suggestion],
                'category': 'Grammar',
                'rule_id': 'CONFUSION_CHECK'
            }
            # Add to errors but don't duplicate exact matches
            if not any(e['original'].lower() == match.group().lower() and 
                      e['from_pos'] == match.start() for e in errors):
                errors.append(error_info)
    
    return errors

def check_capitalization(text):
    """Check for capitalization errors"""
    errors = []
    
    # Check for sentences not starting with capital letter
    sentence_pattern = r'(?:^|[.!?]\s+)([a-z])'
    for match in re.finditer(sentence_pattern, text, re.MULTILINE):
        pos = match.start(1)
        error_info = {
            'message': 'Sentence should start with capital letter',
            'from_pos': pos,
            'to_pos': pos + 1,
            'original': match.group(1),
            'suggestions': [match.group(1).upper()],
            'category': 'Capitalization',
            'rule_id': 'CAPITALIZATION'
        }
        errors.append(error_info)
    
    return errors

def check_punctuation(text):
    """Check for punctuation errors"""
    errors = []
    
    # Check for missing period at end
    if text.strip() and text.strip()[-1] not in '.!?':
        if len(text.strip()) > 10:  # Only flag longer texts
            error_info = {
                'message': 'Missing period at end of text',
                'from_pos': len(text) - 1,
                'to_pos': len(text),
                'original': '',
                'suggestions': ['.'],
                'category': 'Punctuation',
                'rule_id': 'MISSING_PERIOD'
            }
            errors.append(error_info)
    
    return errors

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
