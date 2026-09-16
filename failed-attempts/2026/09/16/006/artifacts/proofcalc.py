import itertools
from math import comb
def C(n,r): return comb(n,r) if 0<=r<=n else 0
# Verify formula closed forms: m=d(k-1) vertices after deleting one color class? l=d(k-2).
# beta(Gamma) = (k-2)C(m,i+1)-(k-1)C(l,i+1)+d(k-1)C(l,i-1).
# Claim: this counts: all (i+1)-sets' components in stacked chain graph? Check i=1: beta12 = (k-2)C(m,2)-(k-1)C(l,2)+d(k-1)l.
# Balanced LBT: f1(Gamma) = C(kd,2) - beta12. Known Klee-Novik: f1 = ... trust.
# For the UPPER bound route, attempt: "vertex-deletion induction": pick v, relate beta(Delta) to beta(Delta-v) + link terms?
# Standard exact sequence: 0 -> ... deletion-contraction for linear strand? For edge ideal / SR ideal, beta_{i,i+1}(Delta) with v a vertex: consider Delta' = Delta - v (deletion, not pure) and link. There is a mapping-cone bound: beta_{i,i+1}(Delta) <= beta_{i,i+1}(Delta') + beta_{i-1,i}(link(v)) + C? Let's test numerically on Gamma: delete one vertex from stacked chain (n=12 -> 11 verts, nonpure). Compute strand of deletion and link, check recursion.
import sys
sys.path.insert(0,'output/artifacts')
from flipsearch import stacked_chain, strand_of_facets
facets,colors,n=stacked_chain(4,2)
# deletion of vertex 11 (a side vertex): faces not containing 11. link of 11: {F-{11}}.
v=11
DL=[F for F in facets if v not in F]
LK=[F-{v} for F in facets if v in F]
print('nDL facets',len(DL),'link facets',len(LK))
# strand needs vertex count: deletion on 11 verts (0..10); link on 11 verts but only uses some.
def strand_masks(facets,n):
    nbr=[0]*n
    for F in facets:
        for a,b in itertools.combinations(sorted(F),2):
            nbr[a]|=(1<<b); nbr[b]|=(1<<a)
    beta=[0]*(n+1)
    for mask in range(1,1<<n):
        rem=mask; comp=0
        while rem:
            comp+=1
            u=(rem&(-rem)).bit_length()-1
            stack=(1<<u); seen=0
            while stack:
                w=(stack&(-stack)).bit_length()-1
                stack^=(1<<w)
                if (seen>>w)&1: continue
                seen|=(1<<w)
                stack|=(nbr[w]&mask&~seen)
            rem&=~seen
        if comp>1: beta[bin(mask).count('1')-1]+=(comp-1)
    return beta
print('strand(Delta)      ',strand_of_facets(facets,n))
print('strand(Delta - v)  ',strand_masks(DL,n))
print('strand(link-ish)   ',strand_masks(LK,n))
