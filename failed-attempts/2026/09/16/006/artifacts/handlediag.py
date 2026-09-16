import itertools
from flipsearch import stacked_chain, faceset_of, check_valid
from collections import Counter
d=4; t=2
facets,colors,n=stacked_chain(d,t)
Fx=[set(F) for F in facets]
tot=0; ridgefail=0; balfail=0
for i in range(len(Fx)):
    for j in range(i+1,len(Fx)):
        if Fx[i]&Fx[j]: continue
        tot+=1
        F1=sorted(Fx[i]); F2=sorted(Fx[j])
        cross=[]
        for v in F1:
            G=set(F2); G.discard(F2[colors[v]]); G.add(v); cross.append(frozenset(G))
        new=[F for k,F in enumerate(facets) if k!=i and k!=j]+cross
        rc=Counter()
        for F in new:
            for v in F: rc[F-frozenset((v,))]+=1
        bad=[v for v in rc.values() if v!=2]
        if bad: ridgefail+=1
        else: balfail+=1
print('disjoint pairs:',tot,'ridgefail:',ridgefail,'balancedfail-but-ridge-ok:',balfail)
