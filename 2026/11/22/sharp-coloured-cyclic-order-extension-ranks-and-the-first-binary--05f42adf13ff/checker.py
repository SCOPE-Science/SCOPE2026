"""Independent finite checks for coloured oriented cyclic-order extension rank.

Standard-library only. The first evaluator uses the one-point game on every
subset of a finite host; the second uses the gap-splitting formula.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product


def direct_rank(word):
    """Evaluate the defining game on all induced marked substructures."""
    n = len(word)
    q = max(word, default=-1) + 1
    # Explicit palette, including missing colours, is passed using the next helper.
    return direct_rank_with_palette(word, q)


def direct_rank_with_palette(word, q):
    n = len(word)

    @lru_cache(None)
    def rank(mask):
        chosen = [i for i in range(n) if mask & (1 << i)]
        gap_index = {}
        if len(chosen) >= 2:
            # Map an unselected point to the marked cyclic predecessor.
            for i in range(len(chosen)):
                a, b = chosen[i], chosen[(i + 1) % len(chosen)]
                j = (a + 1) % n
                while j != b:
                    if not mask & (1 << j):
                        gap_index[j] = a
                    j = (j + 1) % n
        types = defaultdict(list)
        for j in range(n):
            if mask & (1 << j):
                continue
            key = (word[j], gap_index[j]) if len(chosen) >= 2 else (word[j], None)
            types[key].append(rank(mask | (1 << j)))
        keys = ([(c, a) for a in chosen for c in range(q)]
                if len(chosen) >= 2 else [(c, None) for c in range(q)])
        if any(not types[k] for k in keys):
            return 0
        return 1 + min(max(types[k]) for k in keys)

    return rank, rank(0)


def formula_rank_with_palette(word, q):
    n = len(word)

    @lru_cache(None)
    def linear_rank(segment):
        candidate = []
        for c in range(q):
            values = [min(linear_rank(segment[:i]), linear_rank(segment[i + 1:]))
                      for i, a in enumerate(segment) if a == c]
            if not values:
                return 0
            candidate.append(max(values))
        return 1 + min(candidate)

    def arc(i, j):
        vals = []
        k = (i + 1) % n
        while k != j:
            vals.append(word[k])
            k = (k + 1) % n
        return tuple(vals)

    @lru_cache(None)
    def rank(mask):
        chosen = [i for i in range(n) if mask & (1 << i)]
        if len(chosen) >= 2:
            return min(linear_rank(arc(chosen[i], chosen[(i + 1) % len(chosen)]))
                       for i in range(len(chosen)))
        if len(chosen) == 1:
            i = chosen[0]
            options = []
            for c in range(q):
                values = [min(linear_rank(arc(i, j)), linear_rank(arc(j, i)))
                          for j in range(n) if j != i and word[j] == c]
                if not values:
                    return 0
                options.append(max(values))
            return 1 + min(options)
        options = []
        for c in range(q):
            values = [rank(1 << i) for i in range(n) if word[i] == c]
            if not values:
                return 0
            options.append(max(values))
        return 1 + min(options)

    return rank, rank(0)


def standard_representative(word):
    n = len(word)
    return min(word[i:] + word[:i] for i in range(n))


def run():
    tested = 0
    for q, limit in ((1, 11), (2, 8), (3, 6)):
        for n in range(limit + 1):
            for word in product(range(q), repeat=n):
                a, ra = direct_rank_with_palette(word, q)
                b, rb = formula_rank_with_palette(word, q)
                assert ra == rb, (q, word, ra, rb)
                # This checks marked (not only empty) relative ranks.
                for mask in range(1 << n):
                    assert a(mask) == b(mask), (q, word, mask, a(mask), b(mask))
                bound = 0 if n < q else 1 + (n // q).bit_length() - 1
                assert ra <= bound, (q, word, ra, bound)
                tested += 1
    print('GAME_FORMULA_COMPARISONS_OK', tested)

    # Exact optimal thresholds using a genuinely independent game evaluator.
    for q in range(1, 5):
        for t in range(1, 4):
            n = q * (2 ** (t - 1))
            if n > 16:
                continue
            word = tuple(list(range(q)) * (2 ** (t - 1)))
            _, rank = direct_rank_with_palette(word, q)
            assert rank >= t, (q, t, rank)
    print('PERIODIC_OPTIMAL_WITNESSES_OK')

    # Exhaust the complete four-of-each binary stratum at the first
    # nontrivial colored-cyclic threshold.
    n = 8
    good = set()
    bad = set()
    for zero_positions in combinations(range(n), 4):
        word = tuple(0 if i in zero_positions else 1 for i in range(n))
        _, rank = direct_rank_with_palette(word, 2)
        if rank >= 3:
            good.add(word)
        else:
            bad.add(word)
    reps = {standard_representative(w) for w in good}
    assert len(good) == 62
    assert len(bad) == 8
    assert len(reps) == 9
    assert {standard_representative(w) for w in bad} == {tuple([0] * 4 + [1] * 4)}
    orbit_sizes = sorted(len({w[i:] + w[:i] for i in range(n)}) for w in reps)
    assert orbit_sizes == [2, 4] + [8] * 7
    # Fully explicit, human-readable witness certificate (first index;
    # responding index for challenged colour 0, then colour 1).
    witness = {
        "00010111": ((1, 4, 5), (6, 1, 3)),
        "00011011": ((1, 5, 4), (4, 0, 7)),
        "00011101": ((1, 6, 4), (4, 0, 7)),
        "00100111": ((1, 4, 5), (6, 1, 2)),
        "00101011": ((0, 3, 4), (2, 5, 6)),
        "00101101": ((0, 3, 4), (2, 6, 5)),
        "00110011": ((0, 4, 3), (2, 5, 6)),
        "00110101": ((0, 4, 3), (2, 6, 5)),
        "01010101": ((0, 4, 3), (1, 4, 5)),
    }
    assert set(witness) == {''.join(map(str, w)) for w in reps}
    for name, choices in witness.items():
        for first_color, (i, j0, j1) in enumerate(choices):
            assert int(name[i]) == first_color
            for challenge, j in enumerate((j0, j1)):
                assert int(name[j]) == challenge and j != i
                first = []
                k = (i + 1) % n
                while k != j:
                    first.append(int(name[k]))
                    k = (k + 1) % n
                other = []
                k = (j + 1) % n
                while k != i:
                    other.append(int(name[k]))
                    k = (k + 1) % n
                assert set(first) == set(other) == {0, 1}
    print('BINARY_EIGHT_POINT_CENSUS_OK', len(good), len(reps), orbit_sizes)


if __name__ == '__main__':
    run()
