#!/usr/bin/env python3
"""Exact independent enumeration and factorization checks for a 3-state Potts cluster."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product

N = 11
COLORS = range(3)
# v_i = i, u_i = 5+i, apex = 10, indices mod 5.
E = sorted({tuple(sorted(e)) for i in range(5) for e in (
    (i, (i+1) % 5), (5+i, (i-1) % 5), (5+i,(i+1)%5), (5+i,10))})
assert len(E) == 20 and len(set(E)) == 20
EXPECTED = [(4,10),(3,160),(1,30),(1,240),(1,310),(1,80),
            (2,60),(4,40),(7,40),(11,20),(15,2),(20,1)]
CROSSING = [(Fraction(-3,2), 40), (Fraction(0),660),
            (Fraction(1),140), (Fraction(2),100),
            (Fraction(3),80), (Fraction(4),62), (Fraction(5),3)]

def direct_histogram():
    hist = Counter()
    single_edge = Counter()
    # direct assignment of each of the 11 independently specified vertices
    for conf in product(COLORS, repeat=N):
        k = conf.count(0)
        bad = [e for e in E if conf[e[0]] == conf[e[1]]]
        hist[k,len(bad)] += 1
        if len(bad) == 1:
            single_edge[bad[0]] += 1
    return hist, single_edge

def factored_histogram():
    hist=Counter()
    # Exact generating-function coefficient extraction by eliminating the five u_i.
    for v in product(COLORS, repeat=5):
        n_base = v.count(0)
        f_base = sum(v[i]==v[(i+1)%5] for i in range(5))
        for apex in COLORS:
            poly=Counter({(n_base+int(apex==0),f_base): 1})
            for i in range(5):
                local=Counter()
                for u in COLORS:
                    local[(int(u==0), int(u==apex)+int(u==v[(i-1)%5])
                        +int(u==v[(i+1)%5]))] += 1
                updated=Counter()
                for (k,f),a in poly.items():
                    for (dk,df),b in local.items():
                        updated[k+dk,f+df]+=a*b
                poly=updated
            hist.update(poly)
    return hist

def minima(hist):
    return [(min(f for (kk,f) in hist if kk==k),
             sum(n for (kk,f),n in hist.items() if kk==k and f==min(ff for (kk2,ff) in hist if kk2==k)))
            for k in range(N+1)]

def main():
    d, bad = direct_histogram()
    p = factored_histogram()
    assert d == p, 'independent generating-polynomial coefficients disagree'
    assert sum(d.values()) == 3**N == 177147
    table = minima(d)
    assert table == EXPECTED, table
    assert sum(bad.values()) == 660
    # Each of five C5 edges supports 42 single-defect assignments; the
    # ten shadow edges and five apex spokes each support 30.
    for e in E:
        if e[0] < 5 and e[1] < 5:
            assert bad[e] == 42, (e,bad[e])
        else:
            assert bad[e] == 30, (e,bad[e])
    # Evaluate envelope using exact rational arithmetic at every intersection
    # of sector lines (and at all open intervals between those intersections).
    slopes=range(N+1)
    mins=[v for v,_ in table]
    intersections=sorted(set(Fraction(mins[i]-mins[j],i-j) for i in slopes for j in range(i)))
    for x,deg in CROSSING:
        energy=min(Fraction(mins[k])-k*x for k in slopes)
        act=[k for k in slopes if Fraction(mins[k])-k*x==energy]
        assert sum(table[k][1] for k in act)==deg,(x,act,deg)
    phases=[]
    for low,high in zip([None]+intersections, intersections+[None]):
        x=(high-1 if low is None else low+1 if high is None else (low+high)/2)
        energy=min(Fraction(mins[k])-k*x for k in slopes)
        active=[k for k in slopes if Fraction(mins[k])-k*x==energy]
        assert len(active)==1
        if not phases or phases[-1]!=active[0]: phases.append(active[0])
    assert phases==[0,2,5,6,7,8,10,11],phases
    print('VERIFIED: independent full 3^11 enumeration and 3^6 factorization agree')
    print('SECTORS k: (minimal frustrated edges, multiplicity)')
    for k,entry in enumerate(table):print(k,entry)
    print('GROUND OCCUPANCIES:',phases)
    print('TRANSITIONS:',[(str(x),d) for x,d in CROSSING])
    print('ZERO_FIELD_EDGE_ORBITS: ring 5*42=210, cross 10*30=300, spoke 5*30=150')
    print('OK')

if __name__ == '__main__':main()
