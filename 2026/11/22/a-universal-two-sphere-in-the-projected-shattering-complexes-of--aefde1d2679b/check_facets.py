"""Check the all-parameter four-facet nerve pattern on small double stars."""
from itertools import combinations

def check(a,b):
    assert a>=1 and b>=1
    A=set(range(2,2+a)); B=set(range(2+a,2+a+b)); u,v=0,1
    facets=[A|B|{u},A|B|{v},A|{u,v},B|{u,v}]
    # Facets pairwise incomparable.
    assert all(not (facets[i]<=facets[j]) for i in range(4) for j in range(4) if i!=j)
    intersections={}
    for k in range(1,5):
        for I in combinations(range(4),k):
            inter=set.intersection(*(facets[i] for i in I))
            intersections[I]=len(inter)
            assert (len(inter)>0)==(k<=3),(a,b,I,inter)
    # Every face must belong to one of these four facets, and vice versa.
    n=a+b+2
    for mask in range(1<<n):
        S={i for i in range(n) if mask>>i&1}
        permitted=not ({u,v}<=S and S&A and S&B)
        assert permitted==any(S<=f for f in facets)
    return tuple(len(x) for x in facets)

if __name__=='__main__':
    for a in range(1,6):
        for b in range(1,6):
            check(a,b)
    for a,b in ((1,1),(1,3),(2,4),(5,5)):
        print(f'D_{{{a},{b}}}: facet cardinalities {check(a,b)}')
    print('PASS: all 25 tested double stars have tetrahedral-boundary facet nerve')
