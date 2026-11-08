"""Independent finite character-sum checks for rank-one nilpotent Cayley graphs.
Run with Python 3; finite tests are not a substitute for the general proof.
"""
import cmath
import itertools
from collections import Counter


def check(n, p):
    F = range(p)
    vectors = list(itertools.product(F, repeat=n))
    nonzero = [u for u in vectors if any(u)]
    mats = list(itertools.product(F, repeat=n*n))
    def dot(u,v): return sum(a*b for a,b in zip(u,v)) % p
    S = set()
    for u in nonzero:
        for v in nonzero:
            if dot(u,v) == 0:
                S.add(tuple(u[i]*v[j]%p for i in range(n) for j in range(n)))
    k = (p**(n-1)-1)*(p**n-1)//(p-1)
    assert len(S) == k, (n,p,len(S),k)
    for X in S:
        assert sum(X[i*n+i] for i in range(n)) % p == 0
    count = Counter()
    canonical = []
    for B in mats:
        b00 = B[0]
        C = tuple((B[i*n+j] - (b00 if i==j else 0))%p for i in range(n) for j in range(n))
        if B == C:
            canonical.append(B)
    assert len(canonical) == p**(n*n-1)
    root = [cmath.exp(2j*cmath.pi*j/p) for j in F]
    for B in canonical:
        e = 0
        for u in nonzero:
            Bu = tuple(sum(B[i*n+j]*u[j] for j in range(n))%p for i in range(n))
            if any(all(Bu[i]==(t*u[i])%p for i in range(n)) for t in F):
                e += 1
        assert e % (p-1)==0
        e //= (p-1)
        formula = p**(n-1)*e-(p**n-1)//(p-1)
        direct = sum(root[sum(B[j*n+i]*X[i*n+j] for i in range(n) for j in range(n))%p] for X in S)
        assert abs(direct-formula)<1e-6,(n,p,B,e,formula,direct)
        count[formula]+=1
    assert count[k]==1
    assert min(count)==-(p**n-1)//(p-1)
    second=max(v for v in count if v!=k)
    assert second==(p**(n-1)-1)**2//(p-1)
    if n == 2:
        expect = {p*p-1:1, p-1:p*(p*p-1)//2, -1:p*p-1, -(p+1):p*(p-1)**2//2}
        assert count == expect, (count,expect)
    else:
        assert count[second]==(p-1)*(p**n-1)//(p-1)*p**(n-1)
    print(f'n={n}, q={p}, group_order={len(canonical)}, degree={k}, spectrum={sorted(count.items(),reverse=True)}')

for n,p in [(2,2),(2,3),(2,5),(3,2)]:
    check(n,p)
print('NILPOTENT_CAYLEY_FOURIER_CHECKS_OK')
