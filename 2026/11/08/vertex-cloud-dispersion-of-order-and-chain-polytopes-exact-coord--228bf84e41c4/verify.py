"""Independent exact-integer check for vertex-dispersion comparison."""
from itertools import combinations
from collections import Counter


def verify_poset(n, edge_mask):
    pairs = list(combinations(range(n), 2))
    pred = [0] * n
    for bit, (u, v) in enumerate(pairs):
        if (edge_mask >> bit) & 1:
            pred[v] |= 1 << u
    for v in range(n):
        for u in range(v):
            if pred[v] & (1 << u):
                pred[v] |= pred[u]
    ideals = [s for s in range(1 << n)
              if all(not (s >> j & 1) or (s & pred[j]) == pred[j]
                     for j in range(n))]
    N = len(ideals)
    maximal_sets = []
    for s in ideals:
        maximal_sets.append(sum(1 << j for j in range(n)
                                if (s >> j & 1) and not any(
                                    (s >> k & 1) and (pred[k] >> j & 1)
                                    for k in range(j + 1, n))))
    assert len(set(maximal_sets)) == N
    a = [sum((s >> j) & 1 for s in ideals) for j in range(n)]
    b = [sum((s >> j) & 1 for s in maximal_sets) for j in range(n)]
    assert all(0 < a[j] < N and 0 < b[j] < N for j in range(n))
    internal = [j for j in range(n) if pred[j] and any(
        (pred[k] >> j) & 1 for k in range(j+1, n))]
    gaps = [(a[j]-b[j]) * (N-a[j]-b[j]) for j in range(n)]
    assert all(g >= 0 for g in gaps)
    assert all((g > 0) == (j in internal) for j, g in enumerate(gaps))
    # Independent pairwise distance sums, not the theorem's formula.
    order_pair_sum = sum((s ^ t).bit_count() for s in ideals for t in ideals)
    chain_pair_sum = sum((s ^ t).bit_count() for s in maximal_sets for t in maximal_sets)
    assert order_pair_sum - chain_pair_sum == 2 * sum(gaps)
    assert (order_pair_sum == chain_pair_sum) == (len(internal) == 0)
    for j in range(n):
        order_coordinate = sum(((s ^ t) >> j) & 1 for s in ideals for t in ideals)
        chain_coordinate = sum(((s ^ t) >> j) & 1 for s in maximal_sets for t in maximal_sets)
        assert order_coordinate-chain_coordinate == 2*gaps[j]
    return 1


def main():
    count=0
    for n in range(1, 7):
        for edge_mask in range(1 << (n * (n-1)//2)):
            count += verify_poset(n,edge_mask)
    # Explicit sharp boundary: not covariance positive semidefinite.
    ideal_samples = [(0,0,0),(1,0,0),(1,1,0),(1,1,1)]
    antichain_samples = [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
    def covdiff(samples):
        t=[s[0]-s[2] for s in samples]
        return len(t)*sum(z*z for z in t) - sum(t)**2
    assert covdiff(ideal_samples) == 4
    assert covdiff(antichain_samples) == 8
    # Chain n direct all-pairs distributions, for n=3,...,20.
    for n in range(3, 21):
        order = [sum(1<<i for i in range(j)) for j in range(n+1)]
        ant = [0]+[1<<i for i in range(n)]
        qo=sum((s^t).bit_count() for s in order for t in order)
        qc=sum((s^t).bit_count() for s in ant for t in ant)
        assert qo == n*(n+1)*(n+2)//3
        assert qc == 2*n*n
    print('VERTEX_DISPERSION_EXACT_OK',count,'posets; chain checks 18; boundary check PASS')

if __name__=='__main__':
    main()
