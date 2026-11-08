"""Independent finite checks on K4 and K3,3, including exact boundary counts.

Graph definitions are edge lists; all 3**|E| spin states are enumerated.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations,product

def audit_graph(name,n,edges):
    m=len(edges)
    assert m==3*n//2 and all(sum(v in edge for edge in edges)==3 for v in range(n))
    pairs=[(i,j) for i in range(m) for j in range(i+1,m)
           if len(set(edges[i]+edges[j]))==3]
    assert len(pairs)==3*n
    configurations=Counter()
    for spins in product((-1,0,1),repeat=m):
        configurations[(sum(spins[i]*spins[j] for i,j in pairs),
                        sum(s*s for s in spins),sum(spins))]+=1
    witnesses=[(Fraction(2),Fraction(1,4)),
               (Fraction(3,2),Fraction(5,2)),
               (Fraction(1,2),Fraction(1,4)),
               (Fraction(1),Fraction(4)),
               (Fraction(-1),Fraction(1)),
               (Fraction(-1),Fraction(8)),
               (Fraction(1),Fraction(0)),
               (Fraction(-1),Fraction(4))]
    counts=[]
    for d,b in witnesses:
        all_E={c+d*q-b*M:c0 for (c,q,M),c0 in configurations.items()}
        minimum=min(all_E)
        counts.append(sum(v for (c,q,M),v in configurations.items()
                          if c+d*q-b*M==minimum))
    print(name,'full states',3**m,'degeneracy sequence',counts)
    if name=='K4': assert counts==[1,3,6,3,3,1,7,10]
    if name=='K33': assert counts==[1,6,12,6,6,1,31,34]

audit_graph('K4',4,tuple(combinations(range(4),2)))
audit_graph('K33',6,tuple((u,v) for u in range(3) for v in range(3,6)))
print('OTHER_CUBIC_GRAPHS_OK')
