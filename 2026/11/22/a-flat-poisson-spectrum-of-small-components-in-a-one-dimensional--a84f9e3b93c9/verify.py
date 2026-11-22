#!/usr/bin/env python3
"""Exact checks of conditional component-size composition laws."""
from itertools import combinations, product
from math import comb
from fractions import Fraction
from collections import Counter


def dist_by_cuts(n, c):
    if not (1 <= c <= n):
        return Counter()
    out = Counter()
    for cuts in combinations(range(1, n), c - 1):
        ends = (0,) + cuts + (n,)
        sizes = tuple(ends[i+1]-ends[i] for i in range(c))
        out[sum(x == 1 for x in sizes)] += 1
    return out


def theo(n, c, j):
    den = comb(n-1, c-1)
    if n == c:
        return Fraction(int(j == c), 1)
    if j < 0 or j >= c: return Fraction(0)
    N, K = n-c-1, c-j-1
    if not (0 <= K <= N): return Fraction(0)
    return Fraction(comb(c, j) * comb(N, K), den)


def p_pattern(n, s, radius):
    m = n-1
    return sum(((-1)**k) * comb(m-s, k) * max(Fraction(0), 1-(s+k)*radius)**n for k in range(m-s+1))


def n_isolates(bits):
    return bits[0]+bits[-1]+sum(bits[i]*bits[i+1] for i in range(len(bits)-1))


def main():
    assertions=0
    for n in range(2, 12):
        for c in range(1, n+1):
            d = dist_by_cuts(n,c)
            total = sum(d.values())
            assert total == comb(n-1,c-1); assertions+=1
            for j in range(n+1):
                assert Fraction(d[j], total) == theo(n,c,j), (n,c,j)
                assertions+=1
            mu = Fraction(sum(j*k for j,k in d.items()),total)
            assert mu == Fraction(c*(c-1), n-1); assertions+=1
            if n>=3:
                factorial2=Fraction(sum(j*(j-1)*k for j,k in d.items()),total)
                assert factorial2 == Fraction(c*(c-1)**2*(c-2),(n-1)*(n-2));assertions+=1
        for radius in (Fraction(1,7), Fraction(1,3), Fraction(2,5), Fraction(3,5)):
            m = n-1
            probability=Fraction(0)
            for bits in product((0,1), repeat=m):
                s=sum(bits)
                probability+=p_pattern(n,s,radius)
            assert probability == 1,(n,radius,probability);assertions+=1
            for s in range(m+1):
                w=p_pattern(n,s,radius)
                assert w>=0,(n,radius,s,w);assertions+=1
                for j in range(n+1):
                    brute = sum(w for bits in product((0,1),repeat=m)
                                if sum(bits)==s and n_isolates(bits)==j)
                    formula = w * comb(m,s) * theo(n,s+1,j)
                    assert brute == formula,(n,radius,s,j,brute,formula)
                    assertions+=1
    print('PASS', assertions, 'exact rational and combinatorial assertions')

if __name__ == '__main__':main()

# Supplementary exact mixed-factorial checks for the full composition spectrum.
# Executed after the independent checks above, as a separate verification pass.
def compositions(n, c):
    for cuts in combinations(range(1,n),c-1):
        a=(0,)+cuts+(n,)
        yield tuple(a[i+1]-a[i] for i in range(c))

def poscomp_count(n,c):
    if n==0 and c==0: return 1
    if n>=c>=1: return comb(n-1,c-1)
    return 0

def falling(x,k):
    v=1
    for i in range(k):v*=x-i
    return v

def check_mixed():
    assertions=0
    for n in range(2,11):
        for c in range(1,n+1):
            comps=list(compositions(n,c))
            den=poscomp_count(n,c)
            for aa in product(range(3),repeat=3):
                A=sum(aa);S=sum((i+1)*t for i,t in enumerate(aa))
                rhs=Fraction(falling(c,A)*poscomp_count(n-S,c-A),den)
                lhs=Fraction(sum(__import__('math').prod(falling(counts.get(i+1,0),aa[i]) for i in range(3))
                                 for counts in (Counter(co) for co in comps)),den)
                assert lhs==rhs,(n,c,aa,lhs,rhs)
                assertions+=1
    print('PASS supplementary',assertions,'exact mixed-factorial assertions')

if __name__=='__main__':check_mixed()

# Dirichlet-threshold moment identity and negative pairwise dependence.
def check_cut_variances():
    assertions = 0
    for n in range(2,70):
        m=n-1
        for r in (Fraction(1,100),Fraction(1,9),Fraction(1,3),Fraction(2,3)):
            q=(1-r)**n
            q2=max(Fraction(0),1-2*r)**n
            assert q2<=q*q
            var=m*q*(1-q)+m*(m-1)*(q2-q*q)
            assert 0<=var<=m*q
            assertions+=2
    print('PASS supplementary',assertions,'Dirichlet cut-variance assertions')
if __name__=='__main__':check_cut_variances()
