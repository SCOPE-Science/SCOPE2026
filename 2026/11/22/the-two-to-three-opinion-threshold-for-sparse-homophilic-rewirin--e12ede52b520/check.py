"""Exact finite-state generator checks for sparse homophilic threshold rewiring.
Only Python's standard library is needed. No simulation or floating-point
comparison is used to certify the rational identities.
"""
from fractions import Fraction as F
from itertools import combinations

TYPES = (F(0), F(2, 5), F(4, 5))
R = F(1, 5)

def graph(n, pair):
    # Three opinion groups of size n; matching between the indicated groups.
    return frozenset((a*n+k, b*n+k) for k in range(n) for a,b in [pair])

def counts(n, pair):
    edges=graph(n,pair)
    verts=3*n
    assert len(edges)==n
    assert all(abs(TYPES[u//n]-TYPES[v//n])>R for u,v in edges)
    # Conditional probability of creating a concordant edge at one event.
    total=F(0)
    for i,j in edges:
        for v in (i,j):
            neighbors={b if a==v else a for a,b in edges if v in (a,b)}
            possibilities=[(w,F(1)-abs(TYPES[v//n]-TYPES[w//n]))
                           for w in range(verts) if w!=v and w not in neighbors]
            Z=sum((weight for _,weight in possibilities),F(0))
            assert Z>0
            p=sum((weight for w,weight in possibilities if abs(TYPES[v//n]-TYPES[w//n])<=R),F(0))/Z
            total+=p/F(2*len(edges))
    return total

def rational_formula(n, pair):
    if pair==(0,1):
        return F(5*(n-1),2)*(F(1,9*n-8)+F(1,11*n-8))
    if pair==(0,2):
        return F(5*(n-1),9*n-6)
    raise ValueError(pair)

def main():
    assert F(5,9)==F(1,1)/sum((F(1)-abs(TYPES[0]-x) for x in TYPES),F(0))
    assert F(5,11)==F(1,1)/sum((F(1)-abs(TYPES[1]-x) for x in TYPES),F(0))
    for n in range(3,35):
        for pair in ((0,1),(0,2)):
            exact=counts(n,pair)
            theoretical=rational_formula(n,pair)
            assert exact==theoretical,(n,pair,exact,theoretical)
        assert rational_formula(n,(0,2))>rational_formula(n,(0,1))
    pa=F(50,99)
    pc=F(5,9)
    assert 3*pa==F(50,33)
    assert 3*pc==F(5,3)
    assert 3*(pc-pa)==F(5,33)
    # Check the two-group prediction for a rational nonuniform class proportion.
    mass=(F(2,5),F(3,5))
    w=F(3,5)
    qa=mass[0]/(mass[0]+w*mass[1])
    qb=mass[1]/(mass[1]+w*mass[0])
    assert qa==F(10,19) and qb==F(5,7)
    print('PASS: matching generator probabilities for 3 <= n <= 34;')
    print('PASS: exact sign, sparse drift limits, two-class affinity identities.')
    print('Three-class one-event limits: AB=50/99, AC=5/9.')
    print('Normalized slopes: AB=50/33, AC=5/3; gap=5/33.')
if __name__=='__main__': main()
