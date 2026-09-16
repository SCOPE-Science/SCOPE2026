import itertools
from flipsearch import stacked_chain, faceset_of, check_valid, strand_of_facets, graph_edges, link_of
from math import comb
def C(n,r): return comb(n,r) if 0<=r<=n else 0
def formula(d,k,i): return (k-2)*C(d*(k-1),i+1)-(k-1)*C(d*(k-2),i+1)+d*(k-1)*C(d*(k-2),i-1)

d=4; t=2
facets,colors,n=stacked_chain(d,t)
faces=faceset_of(facets)
# candidate quad handle: two disjoint rainbow facets F1,F2; Delta' = facets minus {F1,F2} + 4 cross facets
# enumerate disjoint facet pairs up to symmetry: fix F1 = facet 0? Use orbit reps by intersection profile is overkill; just try all pairs (435) with validity check.
Fx=[set(F) for F in facets]
cands=[]
for i in range(len(Fx)):
    for j in range(i+1,len(Fx)):
        if Fx[i]&Fx[j]: continue
        F1=sorted(Fx[i]); F2=sorted(Fx[j])
        cross=[]
        for v in F1:
            G=set(F2); G.discard(F2[colors[v]])
            G.add(v); cross.append(frozenset(G))
        new=[F for k,F in enumerate(facets) if k!=i and k!=j]+cross
        ok,msg=check_valid(new,d,colors)
        if ok:
            cands.append((i,j,F1,F2,cross))
print('valid handles:',len(cands))
for (i,j,F1,F2,cross) in cands[:4]:
    beta=strand_of_facets(new if False else ([F for k,F in enumerate(facets) if k!=i and k!=j]+cross),n)
    ex=[b-formula(d,3,ii) for ii,b in enumerate(beta)]
    print('pair',F1,F2,'strand',beta,'excess',ex)
