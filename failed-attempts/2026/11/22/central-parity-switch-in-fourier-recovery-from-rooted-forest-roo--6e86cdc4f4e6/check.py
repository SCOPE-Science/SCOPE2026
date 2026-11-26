"""Exact integer verification for rooted-forest root-set Fourier spectra.
No external dependencies. Run: python check.py
"""
from itertools import product
from math import comb


def bareiss(M):
    a = [row[:] for row in M]
    size = len(a)
    sign, prev = 1, 1
    for k in range(size-1):
        if not a[k][k]:
            swap = next((i for i in range(k+1,size) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        piv = a[k][k]
        for i in range(k+1,size):
            for j in range(k+1,size):
                numerator = a[i][j]*piv - a[i][k]*a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
        for i in range(k+1,size):
            a[i][k] = 0
        prev = piv
    return sign*a[-1][-1]


def exact_multiplier(n,p,q):
    # Fractions avoided by expanding the rank-one Schur complement:
    # det=product A*product B - (sum A minors)*(sum B minors).
    plus, minus = n+1, n-1
    A = plus**(n-p)*minus**p
    B = plus**(n-q)*minus**q
    UA = (n-p)*plus**(n-p-1)*minus**p if p<n else 0
    if p: UA += p*plus**(n-p)*minus**(p-1)
    UB = (n-q)*plus**(n-q-1)*minus**q if q<n else 0
    if q: UB += q*plus**(n-q)*minus**(q-1)
    return A*B-UA*UB


def determinant_multiplier(n,p,q):
    epsilon = [-1]*p+[1]*(n-p)
    delta = [-1]*q+[1]*(n-q)
    m = 2*n
    L = [[0]*m for _ in range(m)]
    for i in range(n):
        L[i][i] = n+epsilon[i]
    for j in range(n):
        L[n+j][n+j] = n+delta[j]
    for i in range(n):
        for j in range(n):
            L[i][n+j] = L[n+j][i] = -1
    return bareiss(L)


def roots_by_forest(n):
    m = 2*n
    edges = [(i,n+j) for i in range(n) for j in range(n)]
    histogram = [0]*(1<<m)
    for edge_mask in range(1<<len(edges)):
        if edge_mask.bit_count()>=m:
            continue
        par = list(range(m))
        def find(x):
            while par[x]!=x:
                x=par[x]
            return x
        valid = True
        for k,(u,v) in enumerate(edges):
            if edge_mask>>k &1:
                ru,rv=find(u),find(v)
                if ru==rv:
                    valid=False
                    break
                par[ru]=rv
        if not valid:continue
        components = {}
        for v in range(m):
            r=find(v)
            components.setdefault(r,[]).append(v)
        for picked in product(*components.values()):
            mask = sum(1<<v for v in picked)
            histogram[mask]+=1
    return histogram


def walsh(a):
    a=a[:]
    d=1
    while d<len(a):
        for s in range(0,len(a),2*d):
            for i in range(s,s+d):
                x,y=a[i],a[i+d]
                a[i]=x+y
                a[i+d]=x-y
        d*=2
    return a


def verify():
    checks=0
    # Independent combinatorial enumeration of rooted spanning forests.
    for n in (2,3,4):
        spec = walsh(roots_by_forest(n))
        assert len(spec)==4**n
        for mask, observed in enumerate(spec):
            p=(mask & ((1<<n)-1)).bit_count()
            q=(mask>>n).bit_count()
            assert observed == exact_multiplier(n,p,q), (n,mask)
            checks+=1
    # Exact determinants evaluated independently of the rank-one formula.
    for n in range(2,8):
        for p in range(n+1):
            for q in range(n+1):
                assert determinant_multiplier(n,p,q)==exact_multiplier(n,p,q)
                checks+=1
    # Exhaustive arithmetic zero locus, multiplicities, and n-dependent rank.
    for n in range(2,61):
        nullity=0
        for p in range(n+1):
            for q in range(n+1):
                v=exact_multiplier(n,p,q)
                should_zero=(n%2==1 and p==q==(n-1)//2)
                assert (v==0)==should_zero, (n,p,q,v)
                if v==0:
                    nullity+=comb(n,p)*comb(n,q)
                checks+=1
        expected=comb(n,(n-1)//2)**2 if n%2 else 0
        assert nullity==expected
        checks+=1
    print(f"PASS: {checks} exact comparisons for balanced complete bipartite rooted-forest Fourier convolution")

if __name__ == '__main__':
    verify()
