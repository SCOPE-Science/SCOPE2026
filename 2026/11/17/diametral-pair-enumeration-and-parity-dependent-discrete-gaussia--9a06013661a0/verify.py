"""Brute-force finite checks of diameter pairs for strong-total-cover polytopes.

Run with Python 3.9+; no third-party dependencies. The proof in RESULT.md,
not this finite enumeration, establishes the unrestricted statements.
"""
from itertools import combinations
from math import comb, sqrt


def exact_formula(n):
    assert n >= 3
    by_a = [comb(n, a) * 2 ** (a * (n-a)) for a in range(n+1)]
    by_a[1] -= n
    by_a[-2] -= n
    assert all(v >= 0 for v in by_a)
    return by_a


def brute(n):
    edges = list(combinations(range(n), 2))
    N = n + len(edges)
    by_a = [0] * (n+1)
    complete_pairs = 0
    good_masks = set()
    for mask in range(1 << N):
        bits = [(mask >> i) & 1 for i in range(N)]
        valid = True
        for v in range(n):
            neighbor_e = [bits[n+j] for j,(u,w) in enumerate(edges) if v==u or v==w]
            if not (bits[v] or any(neighbor_e)):
                valid = False; break
        if valid:
            for j,(u,v) in enumerate(edges):
                if not (bits[u] or bits[v] or bits[n+j]):
                    valid = False; break
        if not valid:
            continue
        good_masks.add(mask)
    for mask in good_masks:
        if ( ((1 << N)-1) ^ mask ) in good_masks:
            by_a[sum((mask >> v)&1 for v in range(n))] += 1
    for mask in good_masks:
        if ((((1 << N)-1)^mask) in good_masks) and mask < (((1 << N)-1)^mask):
            complete_pairs += 1
    return by_a, complete_pairs, len(good_masks)


def theta_approx(n, J=20):
    m = n//2
    raw = exact_formula(n)
    total = sum(raw)
    # L1 on all j in [-J,J] plus tails represented by normalization.
    mass = {a-m: v/total for a,v in enumerate(raw)}
    weights = {j: 2.0 ** (-j*j if n%2==0 else -j*(j-1)) for j in range(-J,J+1)}
    s = sum(weights.values())
    return 0.5*sum(abs(mass.get(j,0.0)-weights[j]/s) for j in weights) + 0.5*sum(v for j,v in mass.items() if j not in weights)


def main():
    for n in range(3,6):
        observed, pairs, covers = brute(n)
        expected = exact_formula(n)
        assert observed == expected, (n,observed,expected)
        assert 2*pairs == sum(expected)
        assert pairs > 0
        print('K_{}: {} all covers, {} ordered diametral covers, {} pairs; sizes {}'.format(n,covers,sum(observed),pairs, observed))
    assert exact_formula(3)==[1,9,9,1]
    assert exact_formula(4)==[1,28,96,28,1]
    assert exact_formula(5)==[1,75,640,640,75,1]
    for n in range(3,101):
        w=exact_formula(n)
        assert sum(w)%2==0 and w==list(reversed(w))
    for parity in (0,1):
        samples=[theta_approx(n) for n in range(20+parity,101,2)]
        assert samples[-1] < 0.02
        print('parity {}: TV(20+)={}, TV(100-)={}'.format(parity,samples[0],samples[-1]))
    print('All finite verification assertions passed.')


if __name__=='__main__':
    main()
