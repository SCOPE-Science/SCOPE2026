"""Independent exhaustive small-parameter checks of the stated tortoise spectra.

Run with Python 3: python verify.py

These are finite checks; the theorem for arbitrary parameters uses the proof.
"""

def tortoise_delete(word):
    at = word.find('1')
    return word if at < 0 else word[:at] + word[at + 1:] + '1'


def tortoise_gaps(word):
    gaps = word.split('1')
    if len(gaps) == 1:
        return word
    return gaps[0] + gaps[1] + '1' + ''.join(
        gaps[j] + '1' for j in range(2, len(gaps))
    )


def predicted_one_step(a, b, n):
    p = a + b
    if b == 1:
        q, r = divmod(n, p)
        if q == 0:
            return 2
        if q == 1:
            return r + 1
        return p
    if n == 1:
        return 2
    if n <= p:
        return min(n, a) + min(n, b) - 1
    return p


def predicted_sparse(a, k, n):
    p = a + 1
    q, r = divmod(n, p)
    if q < k:
        return 1 if r == 0 else 2
    if q == k:
        return r + 1
    return p


def factors(a, b, n):
    block = '0' * a + '1' * b
    p = len(block)
    text = block * (n // p + 3)
    return {text[i:i + n] for i in range(p)}


def check():
    comparisons = 0
    for a in range(1, 13):
        for b in range(1, 13):
            for n in range(1, 4 * (a + b) + 4):
                words = factors(a, b, n)
                out1 = {tortoise_delete(w) for w in words}
                out2 = {tortoise_gaps(w) for w in words}
                expected = predicted_one_step(a, b, n)
                assert out1 == out2, (a, b, n, 'different maps')
                assert len(out1) == expected, (a, b, n, len(out1), expected)
                comparisons += 1
    for a in range(1, 13):
        p = a + 1
        for k in range(1, 11):
            for n in range(1, (k + 3) * p + 3):
                words = factors(a, 1, n)
                out1 = set(words)
                out2 = set(words)
                for _ in range(k):
                    out1 = {tortoise_delete(w) for w in out1}
                    out2 = {tortoise_gaps(w) for w in out2}
                expected = predicted_sparse(a, k, n)
                assert out1 == out2, (a, k, n, 'different maps')
                assert len(out1) == expected, (a, k, n, len(out1), expected)
                comparisons += 1
    print(f'PASS: {comparisons} parameter-length comparisons; two operator implementations agree.')


if __name__ == '__main__':
    check()
