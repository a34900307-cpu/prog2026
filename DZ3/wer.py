
def calculate_wer(reference, hypothesis):
    ref = reference.lower().split()
    hyp = hypothesis.lower().split()

    n = len(ref)
    m = len(hyp)

    # Створюємо таблицю для порівняння слів
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    # Знаходимо мінімальну кількість помилок
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if ref[i - 1] == hyp[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j - 1] + 1,
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1
                )

    # Підраховуємо заміни, видалення та вставки
    s = d = ins = 0
    i, j = n, m

    while i > 0 or j > 0:
        if i > 0 and j > 0 and ref[i - 1] == hyp[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            s += 1
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            d += 1
            i -= 1
        else:
            ins += 1
            j -= 1

    wer = (s + d + ins) / n if n > 0 else 0

    return {
        "WER": round(wer, 4),
        "S": s,
        "D": d,
        "I": ins,
        "N": n
    }
