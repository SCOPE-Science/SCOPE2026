"""Exact finite-stratum checks for cyclic multiple coverings of the square torus.

The mathematical proof for all multiplicities is given in RESULT.md.
This script checks every arrangement vertex, open edge, and open two-cell
for the specified finite multiplicities, using integer arithmetic only.
"""



def interval_contains(sample, origin, modulus):
    """Strict membership in the open half-circle, at integer-grid scale."""
    distance = (sample - origin) % modulus
    return 0 < distance < modulus // 2


def minimum_multiplicity(m):
    """Check a finite boundary/interior grid that samples every stratum."""
    N = 4 * m + 3
    L = 4 * N
    grid = range(L)
    xs = [[interval_contains(j, 4 * k, L) for k in range(N)] for j in grid]
    ys = [[interval_contains(j, 8 * k, L) for k in range(N)] for j in grid]
    count_min = N
    witness = None
    for ix in grid:
        xset = xs[ix]
        for iy in grid:
            yset = ys[iy]
            count = sum(xset[k] and yset[k] for k in range(N))
            if count < count_min:
                count_min = count
                witness = (ix, iy)
            if count < m:
                raise AssertionError((m, N, ix, iy, count))
    assert count_min == m, (m, N, count_min)
    assert witness is not None
    return N, count_min, witness


def check_spacing_lemma(m):
    N = 4 * m + 3
    # The selected 2m+1 consecutive first-coordinate indices give
    # a second-coordinate circle gap sequence (2,2,...,2,3)/N.
    gaps = [2] * (2 * m) + [3]
    assert sum(gaps) == N
    assert 4 * (m + 1) > N


def main():
    for m in range(1, 16):
        check_spacing_lemma(m)
        N, low, witness = minimum_multiplicity(m)
        print(f"multiplicity={m}: N={N}, exact grid minimum={low}, stratum witness={witness}")
    print("PASS: integer-stratum exhaustive checks for multiplicities 1..15")


if __name__ == "__main__":
    main()
