"""Finite corroboration of a sharp FO[<] finite-horizon bound.

Run: python3 checker.py
This code checks finite cases; the all-rank theorem requires its EF proof.
"""
from itertools import product
from functools import lru_cache


def word_list(alphabet, max_length):
    return ["".join(seq) for n in range(max_length + 1)
            for seq in product(alphabet, repeat=n)]


def types_by_rank(words, max_rank):
    """Exact rank types via first-vertex characters of a coloured order."""
    types = {w: 0 for w in words}
    out = {0: types}
    for q in range(1, max_rank + 1):
        symbols = {}
        nxt = {}
        for w in words:
            key = frozenset((types[w[:i]], w[i], types[w[i+1:]])
                            for i in range(len(w)))
            if key not in symbols:
                symbols[key] = len(symbols)
            nxt[w] = symbols[key]
        types = nxt
        out[q] = types
    return out


@lru_cache(None)
def ef_equivalent(u, v, rounds, pairs=()):
    """Direct two-sided Ehrenfeucht–Fraïssé game recursion."""
    # The distinguished pairs must preserve equality, order, and letters.
    for (i, j) in pairs:
        if u[i] != v[j]:
            return False
    for (i, j) in pairs:
        for (h, k) in pairs:
            if (i < h) != (j < k) or (i == h) != (j == k):
                return False
    if rounds == 0:
        return True
    for i in range(len(u)):
        if not any(ef_equivalent(u, v, rounds-1, pairs+((i, j),))
                   for j in range(len(v))):
            return False
    for j in range(len(v)):
        if not any(ef_equivalent(u, v, rounds-1, pairs+((i, j),))
                   for i in range(len(u))):
            return False
    return True


def run():
    # The independently written game recursion checks the character algorithm.
    small = word_list('ab', 4)
    ts = types_by_rank(small, 3)
    checked = 0
    for q in range(0, 3):
        for u in small:
            for v in small:
                assert ef_equivalent(u, v, q) == (ts[q][u] == ts[q][v]), (u, v, q)
                checked += 1
    assert checked == 3 * len(small) ** 2

    # For q=1,2,3 the full range of 2^q-1 is tested over two letters.
    words = word_list('ab', 8)
    ty = types_by_rank(words, 3)
    for q in (1, 2, 3):
        threshold = (1 << q) - 1
        short_words = [w for w in words if len(w) <= threshold]
        assert len({ty[q][w] for w in short_words}) == len(short_words)
        assert ty[q]['a' * threshold] == ty[q]['a' * (threshold+1)]

    # Monochromatic-order exact truncation through q=5 and lengths up to 40.
    mono = ['a' * n for n in range(65)]
    mt = types_by_rank(mono, 6)
    for q in range(1, 7):
        threshold = (1 << q) - 1
        for n in range(65):
            for m in range(65):
                same = mt[q][mono[n]] == mt[q][mono[m]]
                assert same == (min(n, threshold) == min(m, threshold)), (q, n, m)

    # Exact horizon profile for the unary even-length regular language.
    for horizon in range(1, 64):
        rank = next(q for q in range(1, 7)
                    if len({(mt[q][mono[n]], n % 2) for n in range(horizon + 1)})
                    == len({mt[q][mono[n]] for n in range(horizon + 1)}))
        assert rank == horizon.bit_length(), (horizon, rank)

    print('SHARP_FO_WORD_HORIZON_CHECKS_OK',
          'direct_game_comparisons=', checked,
          'binary_word_lengths_through=', 8,
          'unary_lengths_through=', 64,
          'verified_ranks=1..6')


if __name__ == '__main__':
    run()
