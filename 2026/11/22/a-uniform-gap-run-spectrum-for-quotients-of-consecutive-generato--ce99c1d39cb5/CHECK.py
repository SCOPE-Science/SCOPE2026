#!/usr/bin/env python3
"""Finite independent check of the quotient-semigroup maximal gap-run law.
The proof for arbitrary parameters is in RESULT.md. Standard library only.
"""
from collections import Counter


def in_quotient(n, p, k):
    a = p * k + 1
    b = a + 1
    target = p * n
    # Since b is 1 modulo a, a representation has y congruent to target
    # modulo a; least nonnegative y works if and only if any works.
    least_b_coins = target % a
    return least_b_coins * b <= target


def test_pair(p, k):
    h = (p + 1) // 2
    expected_frobenius = p*k*k - (p//2 - 1)*k - 1
    expected_genus = h*k + p*k*(k-1)//2
    expected = Counter({h*k: 1})
    for length in range(1, k):
        expected[length] += p
    runs = []
    start = None
    for n in range(1, expected_frobenius + p*k + 2*p + 15):
        if not in_quotient(n,p,k):
            if start is None:
                start = n
        elif start is not None:
            runs.append((start,n-1))
            start = None
    assert start is None, (p,k,start)
    observed = Counter(b-a+1 for a,b in runs)
    assert observed == expected, (p,k,observed,expected)
    assert runs[0] == (1,h*k), (p,k,runs[0])
    assert runs[-1][1] == expected_frobenius, (p,k,runs[-1],expected_frobenius)
    assert sum(b-a+1 for a,b in runs) == expected_genus, (p,k)
    assert len(runs) == 1+p*(k-1), (p,k)
    return len(runs)


def main():
    total_runs = 0
    pairs = 0
    for p in range(2, 41):
        for k in range(1, 26):
            total_runs += test_pair(p, k)
            pairs += 1
    print(f'PASS: {pairs} independent direct-modular exhaustive semigroup checks')
    print(f'      {total_runs} complete maximal missing-number runs checked')
    print('      Each test checks whole gap range plus a nontrivial tail')
    print('      Unbounded parameter theorem follows from interval proof, not tests')

if __name__ == '__main__':
    main()
