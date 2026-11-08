"""Independent finite trace and adaptive-tree checks for coloring-incidence ranks.

Run with Python 3.10+; no third-party dependencies. Finite tests corroborate,
but do not substitute for, the universal arguments in RESULT.md.
"""
from itertools import product
from functools import lru_cache
from collections import Counter
from math import comb


def colorings(m, n, q):
    return [c for c in product(range(q), repeat=m+n)
            if not set(c[:m]).intersection(c[m:])]


def predicted_poly(m, n):
    out = [0] * (m+n+1)
    out[0] = 1
    for k in range(1, m+n+1):
        for side in (m,n):
            if k <= side:
                out[k] += 3 * (2**k - 1) * comb(side,k)
        if k>=2:
            if k-1<=m:
                out[k] += 6*n*comb(m,k-1)
            if k-1<=n:
                out[k] += 6*m*comb(n,k-1)
            if k==2:
                out[k] -= 6*m*n
    return out


def exact_poly(m, n):
    cs = colorings(m,n,3)
    counts = Counter()
    for choices in product(range(4), repeat=m+n):
        tests = [(v,a) for v,a in enumerate(choices) if a<3]
        k=len(tests)
        patterns=set()
        for c in cs:
            patterns.add(sum((1<<i) for i,(v,a) in enumerate(tests) if c[v]==a))
            if len(patterns)==(1<<k):
                counts[k]+=1
                break
    return [counts[j] for j in range(m+n+1)]


def exact_ldim(m, n, q):
    cs = colorings(m,n,q)
    total=len(cs)
    query_bits=[]
    for v in range(m+n):
        for a in range(q):
            bits=sum(1<<i for i,c in enumerate(cs) if c[v]==a)
            if bits not in (0,(1<<total)-1):query_bits.append(bits)
    query_bits=list(dict.fromkeys(query_bits))
    @lru_cache(None)
    def depth_possible(state, depth):
        if depth==0:return state!=0
        if state.bit_count()<1<<depth:return False
        for b in query_bits:
            positive=state&b
            negative=state^positive
            if (positive.bit_count() >= 1<<(depth-1) and
                negative.bit_count() >= 1<<(depth-1) and
                depth_possible(positive,depth-1) and
                depth_possible(negative,depth-1)):
                return True
        return False
    ans=0
    for depth in range(1,m+n+1):
        if not depth_possible((1<<total)-1,depth):break
        ans=depth
    return ans


def full_support_shattered(m,n,q):
    cs=colorings(m,n,q)
    # For q >= 4, two distinct tested colors on the two parts.
    tests=[(v,0 if v<m else 2) for v in range(m+n)]
    return len({sum(1<<i for i,(v,a) in enumerate(tests) if c[v]==a)
                for c in cs}) == (1<<(m+n))


def main():
    poly_cases=0
    for m,n in ((1,1),(1,2),(1,3),(2,2),(2,3),(3,3),(3,4),(4,4)):
        expect=predicted_poly(m,n)
        observed=exact_poly(m,n)
        assert observed==expect, (m,n,expect,observed)
        assert max(i for i,v in enumerate(observed) if v>0) == max(m,n)+1
        poly_cases+=1
    adaptive_cases=0
    for q,m,n in ((2,1,1),(2,1,3),(2,2,3),
                  (3,1,1),(3,1,3),(3,2,2),(3,2,3),(3,3,3),
                  (4,1,1),(4,2,2),(4,2,3),(4,3,3),
                  (5,1,1),(5,2,2),(5,2,3)):
        expectation=(1 if q==2 else max(m,n)+1 if q==3 else m+n)
        observed=exact_ldim(m,n,q)
        assert observed==expectation,(q,m,n,expectation,observed)
        if q>=4:assert full_support_shattered(m,n,q)
        adaptive_cases+=1
    print('PROPER_COLORINGS_BICLIQUE_SHATTERING_PASS',
          'poly_cases='+str(poly_cases),
          'adaptive_cases='+str(adaptive_cases),
          'largest_poly_grid=4x4')


if __name__=='__main__':
    main()
