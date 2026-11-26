"""Exhaustive canonical-alphabet search for simultaneous overlap-freeness.

Run: python3 verify_canonical.py
For every three-letter word, renaming symbols by order of first appearance
produces precisely one canonical word; the curling transform is unchanged.
"""
from collections import Counter


def no_new_overlap(word):
    n = len(word)
    for p in range(1, (n - 1) // 2 + 1):
        if word[n - 2 * p - 1 : n - p] == word[n - p - 1 :]:
            return False
    return True


def has_square_suffix(word):
    n = len(word)
    for width in range(1, n // 2 + 1):
        if word[n - 2 * width : n - width] == word[n - width :]:
            return True
    return False


def main():
    state = [(b'', b'')]
    for n in range(1, 86):
        extended = []
        for word, transform in state:
            next_unused = max(word) + 1 if word else 0
            for symbol in range(min(next_unused, 2) + 1):
                w = word + bytes((symbol,))
                if not no_new_overlap(w):
                    continue
                c = transform + bytes((2 if has_square_suffix(w) else 1,))
                if no_new_overlap(c):
                    extended.append((w, c))
        state = extended
        if n == 84:
            counts = Counter(c for w, c in state)
            assert len(state) == 1008
            assert len(counts) == 2
            assert all(set(w) == {0, 1, 2} for w, c in state)
            print('length=84 canonical_sources=', len(state), sep='')
            print('full_sources=', len(state) * 6, sep='')
            for transform, count in sorted(counts.items()):
                print('output=', ''.join(str(x) for x in transform),
                      ' canonical_preimages=', count,
                      ' labeled_preimages=', count * 6, sep='')
            a, b = sorted(counts)
            print('common_prefix_length=', next((i for i in range(len(a))
                  if a[i] != b[i]), len(a)), sep='')
        if n == 85:
            assert not state
            print('length=85 sources=0')


if __name__ == '__main__':
    main()
