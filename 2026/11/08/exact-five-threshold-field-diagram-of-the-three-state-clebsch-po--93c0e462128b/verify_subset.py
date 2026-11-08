"""Exact independent 3-colour Potts enumeration on the folded 5-cube.

Only Python standard library is required.  Every named 3-colouring is
visited exactly once by a partition into colour-0, colour-1, colour-2 sets.
"""
import json
from fractions import Fraction
from pathlib import Path

N = 16
FULL = (1 << N) - 1
GENERATORS = (1, 2, 4, 8, 15)
EXPECTED_MIN = [8, 7, 6, 5, 3, 3, 3, 3, 4, 8, 12, 15, 20, 25, 30, 35, 40]
EXPECTED_COUNT = [10, 160, 800, 2240, 160, 320, 80, 160, 160, 1280,
                  6400, 512, 1920, 1280, 320, 32, 1]
EXPECTED_INDEPENDENCE = [1, 16, 80, 160, 120, 16]
CRITICAL = [Fraction(-5,4), Fraction(0), Fraction(1), Fraction(11,3), Fraction(5)]
BRANCHES = [0, 4, 7, 8, 11, 16]


def verify():
    adj = [sum(1 << (v ^ shift) for shift in GENERATORS) for v in range(N)]
    assert all((adj[v] >> v) & 1 == 0 for v in range(N))
    assert all(adj[v].bit_count() == 5 for v in range(N))
    assert all(((adj[v] >> w) & 1) == ((adj[w] >> v) & 1)
               for v in range(N) for w in range(N))
    assert sum(a.bit_count() for a in adj) == 80
    for v in range(N):
        for w in range(v + 1, N):
            assert (adj[v] & adj[w]).bit_count() == (0 if adj[v] >> w & 1 else 2)

    # Exact edge count for all 2^16 induced subgraphs.
    induced_edges = [0] * (1 << N)
    for mask in range(1, 1 << N):
        bit = mask & -mask
        vertex = bit.bit_length() - 1
        rest = mask ^ bit
        induced_edges[mask] = induced_edges[rest] + (adj[vertex] & rest).bit_count()
    assert induced_edges[FULL] == 40

    minima = [10**9] * (N + 1)
    counts = [0] * (N + 1)
    witnesses = [None] * (N + 1)
    configurations = 0
    # Every labelled configuration corresponds uniquely to S, T, U:
    # colour-0 S; colour-1 T subset of V-S; colour-2 U=V-(S union T).
    for S in range(1 << N):
        rest = FULL ^ S
        k = S.bit_count()
        eS = induced_edges[S]
        T = rest
        while True:
            U = rest ^ T
            penalty = eS + induced_edges[T] + induced_edges[U]
            configurations += 1
            if penalty < minima[k]:
                minima[k] = penalty
                counts[k] = 1
                witnesses[k] = [S, T, U]
            elif penalty == minima[k]:
                counts[k] += 1
            if T == 0:
                break
            T = (T - 1) & rest
    assert configurations == 3**N == 43046721
    assert minima == EXPECTED_MIN and counts == EXPECTED_COUNT

    # Count independence sets directly, independently of the sector census.
    independence = [0] * (N+1)
    for mask in range(1 << N):
        if induced_edges[mask] == 0:
            independence[mask.bit_count()] += 1
    assert independence[:6] == EXPECTED_INDEPENDENCE
    assert all(x == 0 for x in independence[6:])
    assert sum(x * (2**k) for k,x in enumerate(independence)) == 4065

    # Prove the lower envelope exactly for all real x: compare each omitted
    # line at all finitely many knots; between knots, both differences are
    # affine. On the left/right tails slopes yield monotonic differences.
    def energy(k, x):
        return Fraction(minima[k]) - k*x
    for i, x in enumerate(CRITICAL):
        candidates = [energy(k, x) for k in BRANCHES]
        assert min(candidates) == min(energy(k, x) for k in range(N+1))
        assert [k for k in range(N+1) if energy(k,x)==min(candidates)] == (
            [[0,4], [4,5,6,7], [7,8], [8,11], [11,12,13,14,15,16]][i])
    open_tests = [CRITICAL[0]-1] + [(CRITICAL[i]+CRITICAL[i+1])/2 for i in range(4)] + [CRITICAL[-1]+1]
    for x, k in zip(open_tests, BRANCHES):
        assert energy(k,x) < min(energy(j,x) for j in range(N+1) if j!=k)
    assert sum(counts[k] for k in (4,5,6,7))==720
    assert sum(counts[k] for k in range(11,17))==4065
    assert [sum(counts[k] for k in ks) for ks in
            ([0,4],[4,5,6,7],[7,8],[8,11],[11,12,13,14,15,16])] == [170,720,320,672,4065]

    # Materialized data is provided as a readable exact-result cross-check.
    path = Path(__file__).with_name('sector_data.json')
    expected = json.loads(path.read_text(encoding='utf-8'))
    assert expected['min_monochromatic_edges_by_favored_population'] == minima
    assert expected['degeneracy_by_favored_population'] == counts
    assert expected['independence_polynomial_coefficients'] == independence[:6]
    assert expected['exact_witness_color_masks'] == witnesses
    print('VERIFIED: 43,046,721 labelled states; full sector minima/counts; 5 rational critical fields; independence polynomial.')


if __name__ == '__main__':
    verify()
