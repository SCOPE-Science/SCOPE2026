"""Independent finite checks for cyclically twisted cubes in binary-digit-sum words.

Requires Python 3.9+; does not use third-party packages.
"""

def morphic_prefix(modulus, min_length):
    word = [0]
    while len(word) < min_length:
        word = [letter for a in word for letter in (a, (a + 1) % modulus)]
    return word


def power_two(n):
    return n > 0 and n & (n - 1) == 0


def valuation_two(n):
    assert n >= 1
    return (n & -n).bit_length() - 1


def predicted(modulus, start, root_length):
    if not power_two(root_length):
        return False
    q, r = divmod(start, root_length)
    if r:
        return q % 2 == 0 and valuation_two(q + 2) % modulus == 0
    if q % 2 == 0:
        return valuation_two(q + 2) % modulus == 0
    return valuation_two(q + 1) % modulus == 0


def direct(word, start, root_length, modulus):
    root = word[start:start + root_length]
    second = word[start + root_length:start + 2 * root_length]
    third = word[start + 2 * root_length:start + 3 * root_length]
    return all(b == (a + 1) % modulus and c == (a + 2) % modulus
               for a, b, c in zip(root, second, third))


def run_checks():
    comparisons = 0
    found = 0
    for modulus in range(3, 11):
        # Morphic construction is independent of the binary-popcount generator.
        generated = morphic_prefix(modulus, 16384)
        for i, a in enumerate(generated):
            assert a == i.bit_count() % modulus, (modulus, i)
        for root_length in range(1, 121):
            for start in range(0, 4096):
                actual = direct(generated, start, root_length, modulus)
                expected = predicted(modulus, start, root_length)
                assert actual == expected, (modulus, start, root_length)
                comparisons += 1
                found += int(actual)
            # Check exact least occurrence independently by scanning longer prefixes.
            if power_two(root_length):
                first = (2 ** modulus - 2) * root_length
                if first + 3 * root_length < 16384:
                    assert direct(generated, first, root_length, modulus)
                    assert all(not direct(generated, s, root_length, modulus) for s in range(first))
    print('PASS: morphic-vs-digit-sum prefix agreement for 131072 letters')
    print(f'PASS: {comparisons} direct/predicted twisted-cube comparisons')
    print(f'PASS: {found} positive instances in the tested grid')
    print('PASS: all tested minimal starts match the claimed first-occurrence formula')


if __name__ == '__main__':
    run_checks()
