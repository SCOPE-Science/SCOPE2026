"""Independent checks for (a,b)-regular subsets of squares of cycles.

Run with Python 3.8+; uses only the standard library.
"""
from collections import Counter, defaultdict
from itertools import product

EXPECTED = {
    (0, 1): ('00001',),
    (0, 2): ('001',),
    (1, 2): ('00011', '00101'),
    (1, 3): ('0011',),
    (2, 2): ('000111', '01'),
    (2, 3): ('00111', '01011'),
    (2, 4): ('011',),
    (3, 4): ('01111',),
}


def canonical(word):
    return min(word[k:] + word[:k] for k in range(len(word)))


def transition(state, a, b):
    nxt = b + (a - b) * state[2] - state[0] - state[1] - state[3]
    if nxt not in (0, 1):
        return None
    return state[1:] + (nxt,)


def cycles_for(a, b):
    states = tuple(product((0, 1), repeat=4))
    nxt = {s: transition(s, a, b) for s in states}
    seen = set()
    out = set()
    for state in states:
        if state in seen:
            continue
        walk = []
        here = state
        while here is not None and here not in seen and here not in walk:
            walk.append(here)
            here = nxt[here]
        if here in walk:
            orbit = walk[walk.index(here):]
            word = ''.join(str(s[0]) for s in orbit)
            if 0 < word.count('1') < len(word):
                out.add(canonical(word))
        seen.update(walk)
    return tuple(sorted(out))


def predicted(n):
    d = Counter()
    for key, words in EXPECTED.items():
        d[key] = sum(len(w) for w in words if n % len(w) == 0)
    return +d


def exhaustive_graph(n):
    d = Counter()
    neighbor = [tuple((i + j) % n for j in (-2, -1, 1, 2)) for i in range(n)]
    assert all(len(set(ns)) == 4 for ns in neighbor)
    for bits in product((0, 1), repeat=n):
        size = sum(bits)
        if size == 0 or size == n:
            continue
        included = {sum(bits[j] for j in neighbor[i]) for i in range(n) if bits[i]}
        excluded = {sum(bits[j] for j in neighbor[i]) for i in range(n) if not bits[i]}
        if len(included) == 1 and len(excluded) == 1:
            d[(included.pop(), excluded.pop())] += 1
    return d


def main():
    actual = {(a, b): cycles_for(a, b) for a in range(5) for b in range(5)}
    actual = {k: v for k, v in actual.items() if v}
    assert actual == EXPECTED, (actual, EXPECTED)
    print('ALL_25_PARAMETER_STATE_GRAPHS_OK 400 states 11 nonconstant primitive cycles')
    nsets = 0
    for n in range(5, 15):
        got = exhaustive_graph(n)
        want = predicted(n)
        assert got == want, (n, got, want)
        nsets += 2**n
    print('INDEPENDENT_EXHAUSTIVE_GRAPH_CHECK_OK n=5..14 total_bitstrings=', nsets)
    for n in range(5, 181):
        for (a, b), words in EXPECTED.items():
            for word in words:
                if n % len(word):
                    continue
                for shift in range(len(word)):
                    w = (word[shift:] + word[:shift]) * (n // len(word))
                    vals = tuple(int(t) for t in w)
                    assert 0 < sum(vals) < n
                    for i in range(n):
                        degree_in = sum(vals[(i + t) % n] for t in (-2, -1, 1, 2))
                        assert degree_in == (a if vals[i] else b), (n, a, b, word, shift, i)
    print('ALL_CLASSIFIED_FAMILIES_DIRECTLY_CHECKED n=5..180')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
