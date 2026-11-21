import re

VOWELS = "аеєиіїоуюя"
CONSONANTS = "бвгґджзйклмнпрстфхцчшщ"

def check_uv(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Введіть український текст.")

    words = list(re.finditer(r"[А-Яа-яІіЇїЄєҐґ']+", text))
    results = []

    for i, match in enumerate(words):
        word = match.group()

        if word.lower() not in ("у", "в") or i == len(words) - 1:
            continue

        next_word = words[i + 1].group()
        previous_word = words[i - 1].group() if i > 0 else ""

        prev = previous_word[-1].lower() if previous_word else ""
        nxt = next_word[0].lower()

        suggestion = None
        reason = ""

        if prev in CONSONANTS and nxt in CONSONANTS:
            suggestion = "у"
            reason = "Між приголосними переважно вживаємо «у»."

        elif prev in VOWELS and nxt in VOWELS:
            suggestion = "в"
            reason = "Між голосними переважно вживаємо «в»."

        elif prev in VOWELS and nxt in CONSONANTS:
            suggestion = "в"
            reason = "Після голосного перед приголосним переважно вживаємо «в»."

        elif not previous_word and nxt in CONSONANTS:
            suggestion = "у"
            reason = "На початку речення перед приголосним переважно вживаємо «у»."

        if suggestion and word.lower() != suggestion:
            results.append({
                "word": word,
                "suggestion": suggestion.upper() if word[0].isupper() else suggestion,
                "reason": reason,
                "position": match.start()
            })

    return results
