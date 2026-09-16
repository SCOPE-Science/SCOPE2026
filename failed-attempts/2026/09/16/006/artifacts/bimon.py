import itertools
from flipsearch import check_valid, strand_of_facets
from math import comb
def C(n,r): return comb(n,r) if 0<=r<=n else 0
def formula(d,k,i): return (k-2)*C(d*(k-1),i+1)-(k-1)*C(d*(k-2),i+1)+d*(k-1)*C(d*(k-2),i-1)

# Bipartite-pillow graphs: color class 0 has {a1,a2,a3}, class 1 {b1,b2,b3}, classes 2,3 pairs.
# Consider Delta = Gamma with one extra cross edge e={a1,b1} added (2 more facets? adding edge = filling a missing cross pair = stellar subdivision inverse...). Validity: adding edge {a1,b1} requires subdividing? Edge addition to 1-skeleton while keeping facets: just add all rainbow triangles containing e that keep ridges x2? The balanced analogue of "stacking" adds a vertex; edge-filling changes f0? no.
# Direct approach: search ALL balanced pseudomanifolds on 12 verts with partition (3,3,3,3)? Space = subsets of 81 rainbow quads with ridge-x2: 2^81 too big. Restrict: start from Gamma, apply "edge-fill + facet-surgery" moves.
# Move: pick missing cross edge e={x,y} with link L = {z: {x,y,z} in some facet-contained triangle}... For edge already in complex, link is a cycle. For missing edge, consider S_x = facets containing x, S_y containing y. Fill: add facets {x,y} U R for ridges R shared between link(x) and link(y)? link(x), link(y) are 2-spheres (balanced, colors minus cx). Shared ridges (edges avoiding colors cx,cy): for each shared edge R, add facet {x,y}|R. Ridge check: R was in facets x|R (in S_x) and y|R (S_y); new facets x|y|R replace?? Without removing, ridges {x}|R... wait ridges of new facet {x,y,r1,r2}: {y,r1,r2} (was in y|R facet? {y,r1,r2} subset of facet y|R'? need R' containing...). This is exactly the "fold" (edge identification)? messy.
# ALTERNATIVE STRATEGY: prove upper bound instead. Let's test the STRONGEST plausible structural claim computationally: is beta_{i,i+1}(Delta) <= max over partitions of mono-bound + cross terms? Just brute-force compare MANY random valid complexes.
# Random valid complexes: use "balanced connected sums of joins/suspensions"? Or random cross-polytope gluings: glue t=cross-polytopes along DIFFERENT facets (tree-like) = all in ST^x (stacked) by definition.
# Non-stacked: glue cross-polytopes in a CYCLE (handlebody, not sphere -> not normal pseudo? loop gluing gives manifold with handle: still normal pseudomanifold? Normality = links connected; handlebody triangulation is a manifold with... closed handlebody has boundary, not pseudomanifold without boundary. Gluing cycle of polytopes along facets gives closed manifold (connected sum with S^2xS^1-like / handle): links still spheres? The gluing is along facets like connected sum; a cyclic gluing yields a closed 3-manifold triangulation, hence normal pseudomanifold! Balanced if colorings match.
# Build: 3 cross-polytope boundaries glued in triangle: A-B, B-C, C-A along distinct facet pairs. Each gluing removes 2 facets, identifies 4+4-4=... vertices: n = 8*3 - 4*3 = 12. f0=12! d=4,k=3. VALID?
def xpoly(offset, colmap):
    # full boundary as id-facets + coloring
    import itertools as it
    verts=[[offset+2*c+s for s in (0,1)] for c in range(4)]
    F=[frozenset(p) for p in it.product(*verts)]
    return F, verts
def glue_cycle():
    # three blocks; block s has left/right glue facets on disjoint vertex sets? Each block needs TWO glue facets (to prev and next). Use F_left = all-0 facet, F_right = all-1 facet (disjoint). Chain A-B-C-A: A's right glued to B's left, B's right to C's left, C's right to A's left.
    F=[]; col={}
    # assign: block A: aL[c], aR[c]; B: bL[c],bR[c]; C: cL[c],cR[c]; identifications: aR=bL, bR=cL, cR=aL.
    ids={}; nx=[0]
    def g(k):
        if k not in ids: ids[k]=nx[0]; nx[0]+=1
        return ids[k]
    blocks=[]
    for tag in 'ABC':
        L={c:g((tag,'L',c)) for c in range(4)}
        R={c:g((tag,'R',c)) for c in range(4)}
        blocks.append((L,R))
    # identify: A_R=B_L, B_R=C_L, C_R=A_L
    import itertools as it
    mp={}
    (AL,AR),(BL,BR),(CL,CR)=blocks
    for c in range(4):
        mp[BR[c]]=BL[c] if False else None
    # simpler: union-find
    parent={}
    def find(x):
        while parent.get(x,x)!=x: x=parent[x]
        return x
    def union(x,y):
        parent[find(x)]=find(y)
    for c in range(4):
        union(AR[c],BL[c]); union(BR[c],CL[c]); union(CR[c],AL[c])
    # canonical id per root
    roots={}
    canon={}
    for k,i in ids.items():
        r=find(i)
        if r not in roots: roots[r]=len(roots)
        canon[i]=roots[r]
    N=len(roots)
    print('n verts:',N)
    colors=[None]*N
    for k,i in ids.items():
        colors[canon[i]]=k[2]
    facets=[]
    for (L,R) in blocks:
        FL=frozenset(canon[L[c]] for c in range(4))
        FR=frozenset(canon[R[c]] for c in range(4))
        for ch in it.product([0,1],repeat=4):
            F=frozenset((canon[L[c]] if ch[c]==0 else canon[R[c]]) for c in range(4))
            if F==FL or F==FR: continue
            facets.append(F)
    # dedupe (glued facets removed; remaining distinct?)
    facets=list(set(facets))
    return facets,colors,N
facets,colors,N=glue_cycle()
print('nfacets',len(facets),'valid',check_valid(facets,4,colors))
beta=strand_of_facets(facets,N)
print('strand',beta)
print('formula',[formula(4,3,i) for i in range(N+1)])
print('excess',[b-formula(4,3,i) for i,b in enumerate(beta)])
