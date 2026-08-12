import re
import unicodedata

CONTROL_SEQUENCE_RE = re.compile(r'[\u0000-\u001F\u007F-\u009F]')
ZERO_WIDTH_RE = re.compile(r'[\u200B-\u200F\u202A-\u202E]')

attack_actions = [
    r'ignore', r'bypass', r'override', r'disable', r'remove', r'skip', r'forget', r'drop', r'disable', r'stop'
]
attack_targets = [
    r'system', r'prompt', r'instructions?', r'filters?', r'safety', r'rules?', r'security', r'developer'
]
direct_attack_phrases = [
    r'skip all rules',
    r'follow only my instructions',
    r'forget restrictions',
    r'drop all filters',
    r'remove limitations',
    r'ignore previous instructions',
    r'ignore all safety',
    r'ignore all prompt',
    r'ignore all system prompt'
]

combination_patterns = [
    rf'\b(?:{action})\b.*\b(?:{target})\b' for action in attack_actions for target in attack_targets
] + [
    rf'\b(?:{target})\b.*\b(?:{action})\b' for action in attack_actions for target in attack_targets
]

def is_confusable(ch: str) -> bool:
    try:
        name = unicodedata.name(ch)
        return any(tag in name for tag in ['CYRILLIC', 'GREEK', 'ARABIC', 'HEBREW'])
    except ValueError:
        return False


def score_prompt(prompt: str):
    score = 0
    reasons = []
    lower_prompt = prompt.lower()

    if CONTROL_SEQUENCE_RE.search(prompt):
        score += 10
        reasons.append('Control or non-printable character found')

    if ZERO_WIDTH_RE.search(prompt):
        score += 10
        reasons.append('Zero-width formatting character found')

    if any(re.search(pattern, lower_prompt) for pattern in combination_patterns):
        score += 3
        reasons.append('Suspicious instruction bypass pattern detected')

    if any(phrase in lower_prompt for phrase in direct_attack_phrases):
        score += 3
        reasons.append('Direct prompt injection phrase detected')

    if any(is_confusable(ch) for ch in prompt if not ch.isspace()):
        score += 1
        reasons.append('Character with confusable script detected')

    if len(prompt) > 250 and any(word in lower_prompt for word in ['ignore', 'bypass', 'prompt', 'system', 'developer']):
        score += 1
        reasons.append('Long query with potentially risky keywords')

    return score, reasons


def filter_prompt(prompt: str):
    if not isinstance(prompt, str):
        return False, 'Input must be a text string.'

    normalized = prompt.strip()
    if not normalized:
        return False, 'Please enter a non-empty query.'

    if len(normalized) > 300:
        return False, 'Input is too long. Keep it under 300 characters.'

    score, reasons = score_prompt(normalized)
    if score >= 3:
        return False, f'High-risk prompt blocked. Reasons: {reasons}'

    return True, normalized
