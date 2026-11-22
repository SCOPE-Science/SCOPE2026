"""Independent finite checks of the ternary tortoise collision law.

Run: python3 verification/exhaustive.py
No third-party dependencies.
"""
from collections import Counter
from itertools import product


def tortoise_recursive(word):
    if not word:
        return word
    maximum = max(word)
    chunks = word.split(maximum)
    if len(chunks) == 1:
        return word
    out = tortoise_recursive(chunks[0]) + tortoise_recursive(chunks[1]) + maximum
    for chunk in chunks[2:]:
        out += tortoise_recursive(chunk) + maximum
    return out


def tortoise_stack(word):
    stack = []
    output = []
    for letter in word:
        while stack and stack[-1] <= letter:
            output.append(stack.pop())
        stack.append(letter)
    while stack:
        output.append(stack.pop())
    return ''.join(output)


def binary_fertility(word):
    if '1' not in word:
        return 1
    return word.index('1') + 1 if word.endswith('1') else 0


def binary_double(word):
    return sum(binary_fertility(word[:j])*binary_fertility(word[j:])
               for j in range(len(word) + 1))


def predicted_fertility(word):
    if '2' not in word:
        return binary_fertility(word)
    if not word.endswith('2'):
        return 0
    parts = word.split('2')
    result = binary_double(parts[0])
    for block in parts[1:-1]:
        result *= binary_fertility(block)
    return result


# Exact coefficients of the rational generating function, calculated by
# polynomial recurrence rather than a symbolic algebra library.
N = (1, -8, 32, -68, 83, -60, 24)
P1 = (1, -2, 1)
P2 = (1, -4, 4)
P3 = (1, -5, 7, -5)


def product_polys(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return tuple(c)


def coefficients(count):
    den = product_polys(product_polys(P1, P2), P3)
    seq = []
    for n in range(count):
        rhs = N[n] if n < len(N) else 0
        rhs -= sum(den[j] * seq[n-j] for j in range(1, min(n, len(den)-1)+1))
        assert rhs % den[0] == 0
        seq.append(rhs // den[0])
    return seq


def main():
    expected = coefficients(10)
    checked_input_words = 0
    checked_fibers = 0
    for n in range(10):
        fibers = Counter()
        for letters in product('012', repeat=n):
            word = ''.join(letters)
            a = tortoise_recursive(word)
            b = tortoise_stack(word)
            assert a == b, (word, a, b)
            fibers[a] += 1
            checked_input_words += 1
        square_sum = 0
        for letters in product('012', repeat=n):
            output = ''.join(letters)
            got = fibers.get(output, 0)
            expected_fiber = predicted_fertility(output)
            assert got == expected_fiber, (output, got, expected_fiber)
            square_sum += got*got
            checked_fibers += 1
        assert square_sum == expected[n], (n, square_sum, expected[n])
    print('PASS: lengths 0..9, source words', checked_input_words,
          'output candidates', checked_fibers)
    print('collision sums:', *expected)


if __name__ == '__main__':
    main()
