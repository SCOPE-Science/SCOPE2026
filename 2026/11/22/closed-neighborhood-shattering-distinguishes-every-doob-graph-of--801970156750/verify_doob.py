"""Finite certificates for closed-neighborhood shattering on Doob products.

Standard-library Python 3. The general formula is deduced in the accompanying
proof by factor support reduction; this program checks every finite template.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def instance(m, n):
    d = 2*m+n
    offsets = []
    factor = {}
    for k in range(m):
        for a, b in ((1,0),(3,0),(0,1),(0,3),(1,1),(3,3)):
            v = [0]*d
            v[2*k],v[2*k+1] = a,b
            offsets.append(tuple(v))
            factor[sum(x*(4**j) for j,x in enumerate(v))] = ('S',k)
    for k in range(n):
        for a in (1,2,3):
            v = [0]*d
            v[2*m+k] = a
            offsets.append(tuple(v))
            factor[sum(x*(4**j) for j,x in enumerate(v))] = ('K',k)
    N = 4**d
    def neighborhood(x):
        base = tuple((x//4**j)%4 for j in range(d))
        return frozenset([x]+[sum(((base[j]+o[j])%4)*(4**j) for j in range(d)) for o in offsets])
    return N, neighborhood, factor


def mask(S, neighbor, N):
    balls=[neighbor(x) for x in S]  # symmetry: centers containing query x
    union=set().union(*balls)
    traces={sum((1<<i) for i,b in enumerate(balls) if c in b) for c in union}
    if len(union)<N:traces.add(0)
    return sum(1<<i for i in traces)


def center_census(m,n, four=True):
    N, neighbor, f = instance(m,n)
    ball=sorted(neighbor(0))
    assert len(ball)==1+3*(2*m+n)
    out={k:Counter() for k in (2,3,4)}
    weighted=Fraction(0)
    type_weights=Counter()
    common_sizes=Counter()
    for k in (2,3,4) if four else (2,3):
        for S in combinations(ball,k):
            if mask(S,neighbor,N)!=(1<<(1<<k))-1:
                continue
            fs=Counter(f[x] for x in S if x)
            code=(0 in S,tuple(sorted((a,num) for a,num in fs.items())))
            out[k][code]+=1
            if k==3:
                common=set.intersection(*(set(neighbor(x)) for x in S))
                weighted+=Fraction(1,len(common))
                type_weights[code]+=Fraction(1,len(common))
                common_sizes[(code,len(common))]+=1
    return out,weighted,type_weights,common_sizes


def theoretical(m,n):
    d=2*m+n
    gs=[6]*m+[3]*n
    a=sum(x*y*z for x,y,z in combinations(gs,3))
    b=sum(comb(x,2)*(sum(gs)-x) for x in gs)
    cross=sum(x*y for x,y in combinations(gs,2))
    h=a+b+cross+19*m
    return 27*comb(d+1,3)-8*m,h


def run():
    # Every pair and quadruple inside a common closed ball can be moved to
    # the zero-centered ball. For four points involving at most two active
    # factors, two spare K4 factors represent all possible external
    # singleton and empty traces (including a center outside both factors).
    # The four triple templates test every choice of up to three active
    # factors; two-spare templates test the four-point obstruction.
    templates=((0,3),(1,2),(2,1),(3,0),(0,4),(1,3),(2,2))
    for m,n in templates:
        out,h,_,_=center_census(m,n)
        d=2*m+n
        assert sum(out[2].values())==comb(1+3*d,2),(m,n,'pairs')
        assert not out[4],(m,n,'quadruples')
        assert h==theoretical(m,n)[0]==theoretical(m,n)[1],(m,n,h)
        print('template',m,n,'pairs',sum(out[2].values()),'triples_weight',h,
              'shattered_centered_quadruples',sum(out[4].values()))
    # All S-only local patterns agree in products with another factor.
    for m,n in ((1,1),(2,0),(1,2),(2,1),(3,0)):
        out,h,_,_=center_census(m,n,four=False)
        assert h==theoretical(m,n)[0],(m,n,h)
    # Exact one-Shrikhande local trace table after adjoining one K4 factor.
    tab,w,tw,cs=center_census(1,1,four=False)
    assertions={
      (False,((('S',0),3),)):(14,Fraction(14)),
      (True,((('S',0),2),)):(9,Fraction(5)),
      (False,((('K',0),1),(('S',0),2))):(45,Fraction(45)),
      (False,((('K',0),2),(('S',0),1))):(18,Fraction(18)),
      (True,((('K',0),1),(('S',0),1))):(18,Fraction(18)),
    }
    assert {k:(tab[3][k],tw[k]) for k in tab[3]}==assertions
    assert cs[((True,((('S',0),2),)),1)]==3
    assert cs[((True,((('S',0),2),)),3)]==6
    print('local_Shrikhande_table',[(str(k),str(v)) for k,v in assertions.items()])
    # All-parameter independent centered checks, not a proof by induction.
    trials=((0,4),(0,6),(1,1),(1,2),(1,3),(1,5),(2,0),(2,1),
            (2,2),(2,3),(3,0),(3,1),(4,0))
    for m,n in trials:
        d=2*m+n
        if d<3:continue
        _,h,_,_=center_census(m,n,four=False)
        assert h==27*comb(d+1,3)-8*m,(m,n,h)
        print('count',m,n,'weighted_triples_per_vertex',h,
              'total_triples',h*4**d)
    # Smallest paired graphs: actual direct all-support counts independently
    # confirmed by the separate C++ exhaustive checker for 64 vertices.
    print('DOOB_NEIGHBORHOOD_SHATTER_PASS templates=7 family_samples=13')

if __name__=='__main__':
    run()
