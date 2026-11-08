"""Exact verification of isolated-vertex/overlap-pair covariance identities.

Uses only the Python standard library.  This checks finite examples and exact
arithmetic identities; the proof of the infinite sign classification is in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def falling(a, m):
    z = 1
    for j in range(m):
        z *= a-j
    return z


def cov_formula(n, r, t, m):
    total = comb(n, r)
    avoiding = comb(n-1, r)
    union = 2*r-t
    pairs = total * comb(r, t) * comb(n-r, r-t) // 2
    ex_i = Fraction(n * falling(avoiding, m), falling(total, m))
    ex_t = Fraction(pairs * falling(m, 2), falling(total, 2))
    ratio = Fraction((n-union)*total*(total-1), n*avoiding*(avoiding-1)) - 1
    return ex_i, ex_t, ex_i * ex_t * ratio


def cov_enumeration(n, r, t, m):
    edges = list(combinations(range(n), r))
    edge_masks = [sum(1<<v for v in edge) for edge in edges]
    total = 0
    sumi = sumt = sumit = 0
    for chosen in combinations(range(len(edges)), m):
        present = [edge_masks[a] for a in chosen]
        used = 0
        for mask in present:
            used |= mask
        isolated = n-used.bit_count()
        overlaps = sum((a&b).bit_count()==t for a,b in combinations(present, 2))
        total += 1
        sumi += isolated
        sumt += overlaps
        sumit += isolated*overlaps
    return Fraction(sumi,total), Fraction(sumt,total), Fraction(sumit,total)-Fraction(sumi*sumt,total**2)


def check_all():
    assertions = 0
    enumerations = 0
    for r,n,mvals in [(3,5,[2,3,4]),(3,6,[2,3]),(3,7,[2,3]),
                       (3,8,[2]),(3,9,[2]),(4,6,[2]),
                       (4,7,[2]),(4,8,[2]),(4,9,[2])]:
        for t in range(1,r):
            if n<2*r-t: continue
            for m in mvals:
                if m>comb(n-1,r):continue
                expected = cov_formula(n,r,t,m)
                actual = cov_enumeration(n,r,t,m)
                assert expected == actual, (n,r,t,m,expected,actual)
                assertions += 3
                enumerations += 1
    for r in range(3,28):
        for t in range(1,r):
            s = r-t
            for n in range(max(2*r-t,r+2), max(2*r-t,r+2)+45):
                N = comb(n,r)
                M = comb(n-1,r)
                sign_num = (n*t-r*r)*N+n*s
                assert M>=2
                assert (sign_num>0) == (n*t>=r*r), (n,r,t,sign_num)
                assert sign_num!=0
                assertions += 3
                for m in [2, min(3,M)]:
                    ei,ep,cov=cov_formula(n,r,t,m)
                    assert ei>0 and ep>0
                    assert (cov>0) == (n*t>=r*r)
                    assertions+=2
    print(f'PASS {assertions} exact arithmetic assertions; {enumerations} exhaustive finite sample spaces')

if __name__=='__main__':
    check_all()
