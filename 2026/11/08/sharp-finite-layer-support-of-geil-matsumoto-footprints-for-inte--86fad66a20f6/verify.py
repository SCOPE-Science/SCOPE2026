"""Exact finite checks for an interval-semigroup Geil--Matsumoto footprint theorem.

Run with Python 3, standard library only. This checker does not certify an
infinite theorem; its dynamic-programming semigroup construction is independent
of the interval-layer derivation used in the proof.
"""

def semigroup_table(n, t, limit):
    a = [False] * (limit + 1)
    a[0] = True
    generators = list(range(n, n + t + 1))
    for s in range(1, limit + 1):
        a[s] = any(s >= b and a[s - b] for b in generators)
    return a


def predicted_footprint(n, t, q):
    e = (q - 2) // t + 1  # ceil((q-1)/t)
    K = q + e
    footprint = {0}
    for k in range(1, K):
        footprint.update(range(k*n, min(k*(n+t), K*n-1) + 1))
    for h in range(e):
        for i in range(t + 1):
            lo = (q+h)*n + q*i
            hi = min(lo + h*t, K*n-1)
            footprint.difference_update(range(lo, hi+1))
    return K, footprint


def brute_footprint(n, t, q, limit):
    table = semigroup_table(n, t, limit)
    dilated_generators = [q*(n+i) for i in range(t+1)]
    return {s for s in range(limit+1) if table[s]
            and not any(s >= b and table[s-b] for b in dilated_generators)}


def main():
    tested = 0
    formulas = 0
    for n in range(2, 32):
        for t in range(1, n):
            for q in range(2, 12):
                K, E = predicted_footprint(n,t,q)
                limit = (K+3)*(n+t)
                actual = brute_footprint(n,t,q,limit)
                assert actual == E, ('footprint',n,t,q,sorted(actual^E)[:10])
                assert not any(s >= K*n for s in actual)
                if q==2:
                    assert len(actual)+1 == 3+t+min(t,n//2), ('binary',n,t)
                    formulas += 1
                if q==3 and t>=2:
                    value = (4+3*t+min(3*t,n-1)
                             -max(0,2*t-n+1)-min(t,(n-1)//3))
                    assert len(actual)+1 == value, ('ternary',n,t)
                    formulas += 1
                tested += 1
    witnesses = 0
    for q in range(2, 22):
        for t in range(1, q+2):
            e=(q-2)//t+1
            k=q+e-1
            h=k-q
            n=k*t+q+7
            s=k*n+h*t+1
            K, E=predicted_footprint(n,t,q)
            assert s in E and s < K*n, ('sharp',q,t)
            assert s in brute_footprint(n,t,q,(K+1)*(n+t)), ('directsharp',q,t)
            witnesses += 1
    print('FOOTPRINT_EXACT_DP_OK', 'n=2..31', 'q=2..11', 'cases='+str(tested))
    print('BINARY_TERNARY_EXACT_OK', 'cases='+str(formulas))
    print('SHARP_CUTOFF_WITNESSES_OK', 'cases='+str(witnesses))
    print('VERIFY_OK finite_checks_only=True infinite_proof_separate=True')

if __name__ == '__main__':
    main()
