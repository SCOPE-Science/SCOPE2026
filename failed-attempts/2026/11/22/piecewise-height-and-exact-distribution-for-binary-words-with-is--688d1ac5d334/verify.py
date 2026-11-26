"""Independent finite corroboration of the isolated-marker height and counting laws.

Python 3 standard library only. This verifies finite cases; the proof in RESULT.md
establishes the unrestricted theorems.
"""
from itertools import product
from math import comb


def subsequences(w):
    seen = {""}
    for c in w:
        seen |= {x + c for x in tuple(seen)}
    return seen


def direct_insertion_height(w):
    before = subsequences(w)
    return 1 + max(
        min(map(len, subsequences(w[:i] + b + w[i:]) - before)) - 1
        for i in range(len(w) + 1) for b in "01"
    )


def side_distances(w):
    # Independent dynamic implementation of the source's side-distance recursion.
    values = [(0, 0)]
    last = [-1, -1]
    for pos, c in enumerate(w):
        b = int(c)
        a = 1 - b
        prev = values[-1]
        nxt = list(prev)
        nxt[b] += 1
        nxt[a] = 0 if last[a] < 0 else min(prev[a], 1 + values[last[a]][b])
        values.append(tuple(nxt))
        last[b] = pos
    return values


def dynamic_height(w):
    left = side_distances(w)
    right = side_distances(w[::-1])
    return 1 + max(
        left[i][b] + right[len(w) - i][b]
        for i in range(len(w) + 1) for b in (0, 1)
    )


def word(gaps):
    return "1".join("0" * a for a in gaps)


def height_bound(gaps):
    return len(gaps) + max(gaps)


def choose(a, b):
    return comb(a, b) if a >= b >= 0 else 0


def coefficient_formula(t, S, H):
    B = H - t - 1
    if B <= 0:
        return 0
    return sum((-1) ** j * choose(t + 1, j) * choose(S - 1 - j * B, t)
               for j in range(t + 2))


def run():
    dyn_count = direct_count = coefficient_count = 0
    for t in range(3, 7):
        for gaps in product((1, 2, 3), repeat=t + 1):
            assert dynamic_height(word(gaps)) == height_bound(gaps), (t, gaps)
            dyn_count += 1
    for t in range(3, 5):
        for gaps in product((1, 2, 3), repeat=t + 1):
            w = word(gaps)
            assert direct_insertion_height(w) == height_bound(gaps), (t, gaps)
            direct_count += 1
    for t in range(3, 6):
        for H in range(t + 2, t + 8):
            B = H - t - 1
            counts = {}
            for gaps in product(range(1, B + 1), repeat=t + 1):
                S = sum(gaps)
                counts[S] = counts.get(S, 0) + 1
            assert sum(counts.values()) == B ** (t + 1)
            for S in range(t + 1, (t + 1) * B + 2):
                assert counts.get(S, 0) == coefficient_formula(t, S, H), (t, S, H)
                coefficient_count += 1
    print(f"PASS: {dyn_count} dynamic-height cases, {direct_count} direct-subsequence cases, "
          f"{coefficient_count} coefficient cases")


if __name__ == "__main__":
    run()
