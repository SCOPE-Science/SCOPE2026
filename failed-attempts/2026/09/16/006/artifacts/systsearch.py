import itertools, sys, random
sys.path.insert(0,'output/artifacts')
from flipsearch import check_valid, strand_of_facets
from math import comb
def C(n,r): return comb(n,r) if 0<=r<=n else 0
def formula(d,k,i): return (k-2)*C(d*(k-1),i+1)-(k-1)*C(d*(k-2),i+1)+d*(k-1)*C(d*(k-2),i-1)

def all_quads(part):
    d=len(part)
    return [frozenset(p) for p in itertools.product(*part)]

def ridge_count_ok(facets):
    from collections import Counter
    c=Counter()
    for F in facets:
        for v in F: c[F-frozenset((v,))]+=1
    return all(v==2 for v in c.values())

def random_glue_target(n_blocks=4, seed=0):
    # random tree-gluing of cross-polytopes (stacked, sanity) vs random pairings allowing cycles (manifolds w/ handles)
    rng=random.Random(seed)
    parts=[[0,1,2],[3,4,5],[6,7,8],[9,10,11]]
    Q=all_quads(parts)
    # random balanced pseudo: greedy random facet set with ridge<=2 then check =2? Use simulated approach: start from Gamma-like stacked, apply random "quad swaps" that preserve validity (found 0 before). Instead: random pair gluings of TWO stacked spheres along 2 facet pairs (handle addition on sphere = genus, still manifold).
    return None

# Handle addition on Gamma: remove 2 disjoint facets F1,F2 and glue their boundaries via color-preserving bijection (4! = 24 choices). Each gives closed 3-manifold (S^2xS^1-like or nonorientable handle), balanced, same vertex set, f0=12. Ridge check needed: identified ridges must match counts.
sys.path.insert(0,'output/artifacts')
from flipsearch import stacked_chain, faceset_of
facets,colors,n=stacked_chain(4,2)
Fx=[frozenset(F) for F in facets]
import math
tested=0; valids=[]
pairs=[]
for i in range(len(Fx)):
    for j in range(i+1,len(Fx)):
        if Fx[i]&Fx[j]:
            pairs.append((i,j))
print('disjoint facet pairs:',len(pairs))
# For each pair, try color-preserving bijections sigma: F1->F2 (2 per color-pair choice... F1,F2 rainbow: bijections preserving color: for each color c, F1[c]->F2[c]: unique). Nontrivial gluings need color-SHIFTING maps but those break balancedness? The quotient coloring: identify x~sigma(x); quotient has coloring iff sigma preserves colors. So sigma unique! Only 1 gluing per pair. Alternatively remove facets and DON'T identify verts but add tube facets (handle.py tried cross-set, failed ridges). Hmm: identifying F1,F2 via the unique color-preserving sigma: verts drop by 4 -> n=8, wrong class. So handle-addition changes f0. Not our class.
# => To stay in class (n=12), need different construction. Cyclic chain (bimon) worked (n=12 manifold, low strand).
# What about RP-like quotients or lens spaces? Balanced quotients need fixed-point-free color-preserving involutions. Cross-polytope boundary has antipodal map (color-preserving? antipode swaps within color: yes preserves colors!). Quotient of S^3 by antipodal = RP^3 (manifold, normal pseudo). Balanced? Quotient verts: 6 pairs... n=12 Gamma has free involution? Gamma = connected sum: antipodal on each summand, gluing must be equivariant. Probably exists with n=12 -> RP^3-like balanced manifold with n=12? RP^3 minimal balanced triangulation? Its strand could be large (fewer edges? quotient identifies verts: n drops. To keep n=12 need bigger cover. E.g., quotient of join C6*C6 (n=12) by antipodal (free?) -> n=6, wrong class.
print('handle analysis: color-preserving facet identification forces unique sigma and drops n by 4; quotients drop n. Both leave the (d=4,k=3) class. Cyclic-chain handles keep n but gave LOW strand.')
