"""Independent exhaustive check of zero forcing on labelled crown graphs.

Usage: python verify_crown.py
The exhaustive portion checks all vertex subsets for crown orders 3 through 9.
"""
from collections import Counter
from math import comb


def neighbours(n):
    return [sum(1 << (n + j) for j in range(n) if j != i)
            for i in range(n)] + [sum(1 << j for j in range(n) if j != i)
                                 for i in range(n)]


def forces_all(n, chosen, nb):
    """Apply one legal force at a time until success or no force exists."""
    target = (1 << (2 * n)) - 1
    state = chosen
    while state != target:
        moved = False
        for vertex in range(2 * n):
            if (state >> vertex) & 1:
                white_neighbours = nb[vertex] & (target ^ state)
                if white_neighbours and not (white_neighbours & (white_neighbours - 1)):
                    state |= white_neighbours
                    moved = True
                    break
        if not moved:
            return False
    return True


def predicted(n, chosen):
    full = (1 << n) - 1
    white_a = full ^ (chosen & full)
    white_b = full ^ ((chosen >> n) & full)
    a, b = white_a.bit_count(), white_b.bit_count()
    return a <= 2 and b <= 2 and not (a == 2 and b == 2 and white_a == white_b)


def expected_polynomial(n):
    # Coefficient indexed by number of blue vertices.
    c = comb(n, 2)
    ans = Counter()
    for a in range(3):
        for b in range(3):
            ans[2*n-a-b] += comb(n,a)*comb(n,b)
    ans[2*n-4] -= c
    return ans


def main():
    total_subsets = total_minimal = 0
    for n in range(3,10):
        nb = neighbours(n)
        successes = set()
        coeff = Counter()
        for chosen in range(1 << (2*n)):
            direct = forces_all(n, chosen, nb)
            assert direct == predicted(n, chosen), (n, chosen, direct)
            if direct:
                successes.add(chosen)
                coeff[chosen.bit_count()] += 1
        assert coeff == expected_polynomial(n), (n, coeff)
        minimal = [s for s in successes if all(s ^ (1 << v) not in successes
                     for v in range(2*n) if (s >> v) & 1)]
        c = comb(n, 2)
        assert len(minimal) == c*(c-1)
        assert all(s.bit_count() == 2*n-4 for s in minimal)
        total_subsets += (1 << (2*n))
        total_minimal += len(minimal)
    for n in range(3,101):
        assert expected_polynomial(n)[2*n-4] == comb(n,2)*(comb(n,2)-1)
        assert expected_polynomial(n)[2*n-3] == 2*n*comb(n,2)
        assert expected_polynomial(n)[2*n-2] == n*n+2*comb(n,2)
        assert expected_polynomial(n)[2*n-1] == 2*n
        assert expected_polynomial(n)[2*n] == 1
    print(f'VERIFY_OK orders=3..9 subsets={total_subsets} minimal_sets={total_minimal} '
          f'direct_sequential_forces=PASS white_profile=PASS zero_forcing_polynomials=PASS '
          f'inclusion_minimality=PASS symbolic_counts=3..100 PASS')

if __name__ == '__main__':
    main()
