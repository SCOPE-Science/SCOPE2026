import itertools
from flipsearch import stacked_chain, faceset_of, check_valid, strand_of_facets
from math import comb
def C(n,r): return comb(n,r) if 0<=r<=n else 0
def formula(d,k,i): return (k-2)*C(d*(k-1),i+1)-(k-1)*C(d*(k-2),i+1)+d*(k-1)*C(d*(k-2),i-1)

d=4; t=2
facets,colors,n=stacked_chain(d,t)
faces=faceset_of(facets)
# pillows: pairs of facets sharing a ridge (differ in one vertex); subdivide both by new apex of the shared color? That adds a vertex -> n=13, wrong class.
# Instead CROSS-FLIP within same vertex set: replace {F1,F2} sharing ridge R by the OTHER pair {G1,G2} on same 5 vertices? For balancedness both pairs must be rainbow: 5 verts = colors {c,c,a,b,e}? two share color c. Other rainbow pair: {x1,a,b,e},{x2,a,b,e} = same pair. No alternative.
# Try: find 5-vertex sets supporting 2 disjoint rainbow facets? e.g. F1,F2 disjoint share no verts - union is 8 verts. Cross-swap colors: F1' = {F1[c] for c in S} U {F2[c] for c not in S}. Any such swap keeps facets rainbow. Take two disjoint facets and swap one color -> new pair still disjoint rainbow. Replacing {F1,F2} by swapped pair: check ridges.
Fx=[set(F) for F in facets]
found=0; tested=0
for i in range(len(Fx)):
    for j in range(i+1,len(Fx)):
        if Fx[i]&Fx[j]: continue
        F1=sorted(Fx[i],key=lambda v:colors[v]); F2=sorted(Fx[j],key=lambda v:colors[v])
        # F1[c],F2[c] sorted by color already since facets rainbow and sorted by color key
        for S in [frozenset((0,)),frozenset((0,1)),frozenset((0,1,2))]:
            G1=set(F1[c] if c in S else F2[c] for c in range(4))
            G2=set(F2[c] if c in S else F1[c] for c in range(4))
            g1,f1=frozenset(G1),frozenset(F1); g2,f2=frozenset(G2),frozenset(F2)
            if g1==f1 or g1==f2: continue
            new=[F for k,F in enumerate(facets) if k!=i and k!=j]+[g1,g2]
            ok,msg=check_valid(new,d,colors)
            tested+=1
            if ok:
                found+=1
                if found<=3:
                    beta=strand_of_facets(new,n)
                    print('swap',S,'strand',beta,'excess',[b-formula(d,3,ii) for ii,b in enumerate(beta)])
print('tested',tested,'valid',found)
