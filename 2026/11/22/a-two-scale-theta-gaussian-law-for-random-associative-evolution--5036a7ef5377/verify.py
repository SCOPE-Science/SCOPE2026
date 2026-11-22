#!/usr/bin/env python3
"""Finite exact tests of labelled associative evolution-algebra counts.

All matrices here are labelled relative to a fixed natural basis. No
isomorphism quotient or infinite-case certification is inferred.
"""
from itertools import product
from math import comb


def exact(n,q):
    return [comb(n,s)*(q**(n-s+1)-1)**s for s in range(n+1)]


def satisfy_brute(A,n,q):
    # For each ordered basis triple (i,j,k) compare products of (e_i e_j)e_k
    # and e_i(e_j e_k); the algebra is commutative and mixed basis products vanish.
    for i in range(n):
        for j in range(n):
            for k in range(n):
                left = [0]*n
                right = [0]*n
                if i == j:
                    left = [(A[i*n+k]*A[k*n+t])%q for t in range(n)]
                if j == k:
                    right = [(A[j*n+i]*A[i*n+t])%q for t in range(n)]
                if left != right: return False
    return True


def satisfy_support(A,n):
    return all(A[i*n+j] == 0 or all(A[j*n+k] == 0 for k in range(n))
               for i in range(n) for j in range(n) if i != j)


def check(n,q):
    found = [0]*(n+1)
    joint = [[0]*(n+1) for _ in range(n+1)]
    for A in product(range(q), repeat=n*n):
        p = satisfy_brute(A,n,q)
        assert p == satisfy_support(A,n), (n,q,A)
        if p:
            s = sum(any(A[i*n+j] for j in range(n)) for i in range(n))
            t = sum(A[i*n+i] != 0 for i in range(n))
            found[s] += 1
            joint[s][t] += 1
    required = exact(n,q)
    assert found == required, (n,q,found,required)
    for s in range(n+1):
        for t in range(n+1):
            want = (comb(n,s)*comb(s,t)*((q-1)*q**(n-s))**t*(q**(n-s)-1)**(s-t)) if t <= s else 0
            assert joint[s][t] == want, (n,q,s,t,joint[s][t],want)
    print(f'EXHAUSTIVE_OK n={n} q={q} by_active={found} total={sum(found)}')


def main():
    for n,q in [(1,2),(2,2),(3,2),(4,2),(2,3),(3,3),(2,4)]:
        # GF(4) is used only for count, since brute multiplication above is mod q;
        # the zero/nonzero criterion is field-independent and remains valid.
        if q == 4:
            from itertools import product
            counts=[0]*(n+1)
            for A in product(range(q),repeat=n*n):
                if satisfy_support(A,n):
                    counts[sum(any(A[i*n+j] for j in range(n)) for i in range(n))]+=1
            assert counts==exact(n,q)
            print(f'SUPPORT_OK n={n} q={q} by_active={counts} total={sum(counts)}')
        else:
            check(n,q)
    # Check coordinate-space maximality directly for small n.
    for n in range(1,8):
        def permitted(S):
            return {(i,j) for i in range(n) if i in S
                    for j in range(n) if j == i or j not in S}
        sets=[set(i for i in range(n) if mask>>i&1) for mask in range(1,1<<n)]
        spans=[permitted(S) for S in sets]
        assert len(set(map(frozenset,spans)))==len(sets)
        assert all(not (A <= B) for i,A in enumerate(spans) for j,B in enumerate(spans) if i!=j)
        dim=max(len(x) for x in spans)
        assert dim==(n+1)**2//4
        print(f'COMPONENTS_OK n={n} count={len(spans)} dimension={dim}')
    print('VERIFY_OK')

if __name__=='__main__': main()
