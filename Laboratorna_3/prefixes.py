import re

VOWELS = "аеєиіїоуюя"

# Навчальний словник слів із варіантами у-/в-
PAIRS = {
    "учитель": "вчитель",
    "вчитель": "учитель",
    "учитися": "вчитися",
    "вчитися": "учитися",
    "учень": "вчень",  # не є нормативною парою
}

# Прибираємо ненормативну пару
PAIRS.pop("учень")

def check_prefixes(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Введіть український текст.")

    words = list(re.finditer(
        r"[А-Яа-яІіЇїЄєҐґ]+", text
    ))

    results = []

    for i, match in enumerate(words):
        word = match.group()
        lower = word.lower()

        if lower not in PAIRS:
            continue

        alternative = PAIRS[lower]

        if i == 0:
            continue

        previous = words[i - 1].group()
        last = previous[-1].lower()

        # Спрощена рекомендація за милозвучністю
        preferred = "в" if last in VOWELS else "у"

        if lower[0] != preferred:
            suggestion = alternative

            if word[0].isupper():
                suggestion = suggestion.capitalize()

            results.append({
                "word": word,
                "alternative": suggestion,
                "position": match.start(),
                "reason": "Рекомендація за звуковим оточенням."
            })

    return results
