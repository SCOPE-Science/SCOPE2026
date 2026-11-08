"""Exact rational verification of two-coupon label-recovery formulas.

No external dependencies. Run: python verify.py
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


def moment(n, r):
    if r == 0:
        return Fraction(1)
    N = n - 2*r
    b = comb(n, 2) - comb(N, 2) - r
    assert n >= 3 and 1 <= r <= n//2 and b > 0
    s = sum((Fraction((-1)**(j+l)*comb(r,j)*comb(N,l),
                      b+j+comb(N,2)-comb(N-l,2))
             for j in range(r+1) for l in range(N+1)), Fraction(0))
    return Fraction(factorial(n),factorial(N)*2**r)*b*s


def distribution(n):
    fm = [moment(n, r) for r in range(n//2+1)]
    p = [sum((Fraction((-1)**(r-y),factorial(y)*factorial(r-y))*fm[r]
              for r in range(y,n//2+1)),Fraction(0))
         for y in range(n//2+1)]
    assert sum(p) == 1 and min(p) >= 0
    return p


def extra_means(n):
    E = comb(n,2)
    h=[Fraction(0)]
    for r in range(1,n//2+1):
        s=Fraction(r-1,n-r-1)
        h.append(Fraction(E,2*r*(n-r-1))+(1-s)*h[r-1]
                 +(s*h[r-2] if r>=2 else 0))
    return h


def coverage_mean(n):
    E=comb(n,2)
    return sum((Fraction((-1)**(j+1)*comb(n,j)*E,
                         E-comb(n-j,2)) for j in range(1,n+1)), Fraction(0))


def exact_total(n):
    return coverage_mean(n) + sum((x*y for x,y in zip(distribution(n),extra_means(n))), Fraction(0))


def direct_graph_process(n):
    # Ignore repeats for the stopping graph: every new edge is uniform among absent edges.
    edges=[(a,b) for a in range(n) for b in range(a+1,n)]
    E=len(edges)
    vertex_masks=[sum(1<<i for i,e in enumerate(edges) if v in e) for v in range(n)]
    def counts(mask):
        d=[(mask&m).bit_count() for m in vertex_masks]
        isolated=sum(x==0 for x in d)
        doubletons=sum(1 for i,(a,b) in enumerate(edges)
                       if (mask & (1<<i)) and d[a]==1 and d[b]==1)
        return isolated,doubletons
    @lru_cache(None)
    def waits(mask):
        i,d=counts(mask)
        if i==0 and d==0: return Fraction(0)
        k=mask.bit_count()
        return Fraction(E,E-k) + sum((waits(mask|(1<<j)) for j in range(E)
                    if not mask&(1<<j)),Fraction(0))/ (E-k)
    # Discrete-time expected waiting until all labels are identified.
    direct_total=waits(0)
    p=[Fraction(0)]*(n//2+1)
    d={0:Fraction(1)}
    for k in range(E+1):
        nd={}
        for mask,weight in d.items():
            i,y=counts(mask)
            if i==0:
                p[y]+=weight
                continue
            for j in range(E):
                if not mask&(1<<j):
                    nxt=mask|(1<<j)
                    nd[nxt]=nd.get(nxt,Fraction(0))+weight/Fraction(E-k)
        d=nd
    return p,direct_total


def run():
    checks=0
    for n in range(3,14):
        p=distribution(n); h=extra_means(n)
        assert sum(p)==1
        for r in range(n//2+1):
            assert sum((factorial(y)//factorial(y-r)*p[y] for y in range(r,len(p))),Fraction(0))==moment(n,r)
            checks+=1
        assert h[0]==0
        checks+=1
        if n<=6:
            q,whole=direct_graph_process(n)
            assert q==p, (n,q,p)
            assert whole==exact_total(n),(n,whole,exact_total(n))
            checks+=len(q)+1
        print('n=%d residual_probabilities=%s full_expectation=%s extra_expectation=%s' %
              (n, [str(x) for x in p], exact_total(n),
               sum((x*y for x,y in zip(p,h)),Fraction(0))))
    print('All %d independent exact-rational checks passed.'%checks)
if __name__=='__main__': run()
