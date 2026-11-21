import re

def check_prefixes(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Введіть текст для перевірки.")

    # Навчальний набір слів з можливим чергуванням у-/в-
    pairs = {
        "вчитель": "учитель",
        "учитель": "вчитель",
        "вчитися": "учитися",
        "учитися": "вчитися",
        "вправа": "управа",
        "управа": "вправа",
    }

    results = []

    for match in re.finditer(r"[А-Яа-яІіЇїЄєҐґ]+", text):
        word = match.group()
        alternative = pairs.get(word.lower())

        if alternative:
            results.append({
                "word": word,
                "alternative": alternative,
                "position": match.start()
            })

    return results

print("Модуль перевірки варіантів у-/в- створено.")
