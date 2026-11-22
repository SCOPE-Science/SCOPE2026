"""Independent exact matching-bitset certificate for rate response on G(8,3).

Run: python3 verify_matchings.py
Requires only Python's standard library.
"""
from fractions import Fraction
from functools import lru_cache

# Construct the graph via three edge generators, interleaving types.
N = 8
EDGES = []
for j in range(N):
    EDGES += [tuple(sorted((j, (j+1)%N))),
              tuple(sorted((j, N+j))),
              tuple(sorted((N+j, N+(j+3)%N)))]
assert len(EDGES) == len(set(EDGES)) == 24
EDGE_ENDS = [((1<<u)|(1<<v)) for u,v in EDGES]
P = Fraction(903422, 3840375)
C_RING = Fraction(276830066540632837, 4793798789772300000)
C_SPOKE = -Fraction(561926341371011, 43579988997930000)


def jet(mark_type):
    assert mark_type in ("ring", "spoke")
    marked = [((u < N and v < N) if mark_type == "ring"
               else (u < N and v >= N)) for (u,v) in EDGES]

    @lru_cache(None)
    def recurrence(chosen_edges):
        # State here is the set of deposited EDGES, not occupied vertices.
        occupied = 0
        number = 0
        for i, bitmask in enumerate(EDGE_ENDS):
            if chosen_edges & (1<<i):
                assert not (occupied & bitmask)
                occupied |= bitmask
                number += 1
        options = [i for i, bitmask in enumerate(EDGE_ENDS) if not (occupied & bitmask)]
        if not options:
            return Fraction(int(number == N)), Fraction(0), Fraction(0)
        k = len(options)
        a = sum(marked[i] for i in options)
        total0 = total1 = total2 = Fraction(0)
        for j in options:
            p, d, dd = recurrence(chosen_edges | (1<<j))
            b = int(marked[j])
            total0 += p
            total1 += d + b*p
            total2 += dd + 2*b*d
        p = total0/k
        d = (total1-a*p)/k
        dd = (total2-2*a*d)/k
        return p, d, dd
    result = recurrence(0)
    assert recurrence.cache_info().currsize == 11068
    return result


def main():
    for label, expected in (("ring", C_RING), ("spoke", C_SPOKE)):
        result = jet(label)
        assert result == (P, Fraction(0), expected)
        print(label, tuple(map(str, result)))
    assert C_RING > 0 and C_SPOKE < 0
    print("MATCHING_STATE_EXACT_OK")

if __name__ == "__main__":
    main()
