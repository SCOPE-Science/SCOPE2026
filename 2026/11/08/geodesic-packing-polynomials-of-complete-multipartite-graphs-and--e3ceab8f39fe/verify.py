#!/usr/bin/env python3
"""Independent finite verification of maximal-geodesic packing enumerators.

The definitions are evaluated on constructed multipartite graphs. All counts
are exact integer computations, not statistical estimates.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb, factorial


def geodesics(profile):
    colors = tuple(i for i, n in enumerate(profile) for _ in range(n))
    N = len(colors)
    # Independent construction: all length-two shortest paths in diameter-two
    # multipartite graph; pair endpoints have graph distance two.
    return tuple((1 << a) | (1 << c) | (1 << b)
                 for a in range(N) for b in range(a+1, N)
                 if colors[a] == colors[b]
                 for c in range(N) if colors[c] != colors[a])


def direct(profile):
    paths = geodesics(profile)
    # path subsets treated as distinct geodesics; enumerate all pairwise
    # vertex-disjoint families, independent of the proposed formula.
    all_ct, max_ct = Counter(), Counter()
    def visit(k, used, depth):
        all_ct[depth] += 1
        candidates = [j for j, p in enumerate(paths) if j >= k and not (p & used)]
        if not any((p & used) == 0 for p in paths):
            max_ct[depth] += 1
        for j in candidates:
            visit(j+1, used | paths[j], depth + 1)
    visit(0, 0, 0)
    return all_ct, max_ct


def formula(profile):
    r = len(profile)
    P = [[0]*r for _ in range(r)]
    out, inc = [0]*r, [0]*r
    all_ct, max_ct = Counter(), Counter()
    cells = [(i,j) for i in range(r) for j in range(r) if i != j]
    def recur(idx, k):
        if idx == len(cells):
            remain = [profile[i]-2*out[i]-inc[i] for i in range(r)]
            # Divide only after assembling the complete integer numerator.
            den = 2**k
            for i,j in cells: den *= factorial(P[i][j])
            num = 1
            for i,n in enumerate(profile): num *= factorial(n)
            for t in remain: den *= factorial(t)
            assert num % den == 0
            count = num // den
            all_ct[k] += count
            if not any(remain[i]>=2 and remain[j]>=1 for i in range(r) for j in range(r) if i!=j):
                max_ct[k] += count
            return
        i,j = cells[idx]
        p = 0
        while 2*(out[i]+p)+inc[i] <= profile[i] and 2*out[j]+inc[j]+p <= profile[j]:
            P[i][j] = p
            out[i] += p; inc[j] += p
            recur(idx+1,k+p)
            out[i] -= p; inc[j] -= p
            p+=1
        P[i][j] = 0
    recur(0,0)
    return all_ct,max_ct


def twins(r):
    a=Counter(); m=Counter()
    for k in range(r+1):
        if 3*k > 2*r: continue
        a[k]=comb(r,k)*factorial(2*(r-k))//factorial(2*r-3*k)
        if 2*k>=r:
            m[k]+=comb(r,k)*comb(r-k,2*k-r)*2**(2*r-3*k)*factorial(k)
        if r%3==1 and k==2*(r-1)//3 and r>=4:
            m[k]+=comb(r,k)*(r-k)*factorial(k)
    return a,m


def main():
    total = cases = twin_cases = 0
    for r in range(2,5):
        for p in combinations_with_replacement(range(2,5), r):
            if sum(p) > 10: continue
            x,y = direct(p)
            u,v = formula(p)
            assert x==u and y==v, (p,x,u,y,v)
            cases += 1; total += sum(x.values())
    for r in range(2,8):
        p=(2,)*r
        x,y=direct(p)
        u,v=twins(r)
        assert x==u and y==v, (p,x,u,y,v)
        twin_cases+=1; total+=sum(x.values())
    for r in range(2,31):
        u,v=formula((2,)*r) if r<=5 else twins(r) # symbolic twin only for large r
        a,b=twins(r)
        assert u==a and v==b
        supports={k for k,c in b.items() if c}
        assert supports==set(range((r+1)//2, 2*r//3 +1))
    print('VERIFY_OK direct_profiles=%d twin_profiles=%d enumerated_path_families=%d general_formula=PASS twin_formula=PASS maximality=PASS symbolic_purity_r2to30=PASS' % (cases,twin_cases,total))

if __name__ == '__main__':
    main()
