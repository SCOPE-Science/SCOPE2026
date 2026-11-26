"""Independent state-by-state verification of symbolic reset constructions.
This is supporting finite corroboration only; see RESULT.md for the all-n proof.
Run: python3 verify_direct.py.
"""


def apply(word, size):
    image = list(range(size))
    for letter in word:
        if letter == 'a':
            image = [(value + 1) % size for value in image]
        elif letter == 'b':
            image = [0 if value == size - 1 else value for value in image]
        else:
            raise AssertionError('Unknown letter')
    return frozenset(image)


def canonical(n):
    return 'b' + ('a' * (n - 1) + 'b') * (n - 2)


def corrected(n):
    return 'b' + ('a' * (n - 1) + 'b') * (n - 3) + 'a' * (n - 3) + 'baa' + 'b'


def main():
    for n in range(4, 71):
        base = canonical(n)
        alt = corrected(n)
        assert len(base) == (n - 1) ** 2
        assert len(alt) == (n - 1) ** 2 + 1
        assert len(apply(base, n)) == 1
        assert len(apply(alt, n)) == 1
        assert (len(apply(base, 3)) == 1) == (n % 3 == 0)
        assert len(apply(alt, 3)) == 1
        # Track the intermediate large-automaton image used in the proof.
        prefix = 'b' + ('a' * (n - 1) + 'b') * (n - 3)
        assert apply(prefix, n) == frozenset({0, 1})
    print('DIRECT_OK n=4..70')


if __name__ == '__main__':
    main()
