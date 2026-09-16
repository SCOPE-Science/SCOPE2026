import itertools
from flipsearch import check_valid, strand_of_facets
from math import comb
def C(n,r): return comb(n,r) if 0<=r<=n else 0
def formula(d,k,i): return (k-2)*C(d*(k-1),i+1)-(k-1)*C(d*(k-2),i+1)+d*(k-1)*C(d*(k-2),i-1)

# balanced 2-sphere base with 9 vertices (3 per color)? Take connected sum of two octahedra along a facet: n=6+6-3=9, colors (3,3,3). Facets: 8+8-2=14.
octA=[frozenset(p) for p in itertools.product([0,1],[2,3],[4,5])]
F0=frozenset((0,2,4))
base=[F for F in octA if F!=F0]
# second octahedron shares facet verts {0,2,4}, new verts 6(col0),7(col1),8(col2)
octB=[frozenset(p) for p in itertools.product([0,6],[2,7],[4,8])]
base += [F for F in octB if F!=F0]
S=list(base)
col={0:0,1:0,6:0, 2:1,3:1,7:1, 4:2,5:2,8:2}
print('base facets',len(S))
# suspension: apices 9 (col3), 10 (col3); facets F+apex for each F. n=11?? Need kd: d=4,n=12 -> base needs 10 verts. Take connected sum of THREE octahedra: n=6+3+... each sum adds 3 verts: 6,9,12? base 2-sphere with 12 verts then suspension gives 14. Wrong.
# Alternative: suspension needs base (d-2)-sphere with kd-2 verts. d=4,k=3: base 2-sphere, 10 verts, color sizes (3,3,4)? Suspension apices same new color: final sizes (3,3,4,2). f0=12. OK valid balanced.
# Base: stacked 2-sphere with 10 verts: connected sums of octahedra: 6 -> 9 -> 12 gives 12, not 10. Stacked 2-sphere vertex counts: 6+3t. 10 impossible as stacked. Use non-stacked balanced 2-sphere with 10 verts: e.g., suspension of C? balanced 2-sphere = suspension of even cycle C_{2m} has 2m+2 verts... C8 susp: 10 verts colors (2,2,6)? colors: cycle colors 0,1, apices color 2: sizes (4,4,2). Then suspend again? Double suspension of C6: S^1->S^2->S^3: verts 6+2+2=10, colors (3,3,2,2), n=10 not 12.
# Simplest: double suspension of C8: n=8+2+2=12, colors (4,4,2,2). dim 3, balanced 3-sphere (suspension of sphere). Normal pseudo yes. f0=12=4*3. VALID CANDIDATE.
def susp(facets,a,b):
    return [F|{a} for F in facets]+[F|{b} for F in facets]
c8=[frozenset((i,(i+1)%8)) for i in range(8)]
s1=susp(c8,8,9)          # 2-sphere, 10 verts
s2=susp(s1,10,11)        # 3-sphere, 12 verts
col2={}
for v in range(8): col2[v]=v%2
col2[8]=2; col2[9]=2; col2[10]=3; col2[11]=3
print('double susp C8: valid',check_valid(s2,4,col2))
beta=strand_of_facets(s2,12)
print('strand',beta)
print('formula',[formula(4,3,i) for i in range(13)])
print('excess',[b-formula(4,3,i) for i,b in enumerate(beta)])
# also double susp C6 + extra: n=10, k not integer; skip. Try triple-stacked-base suspension: base = connected sum of 2 octahedra (9 verts, 333), apices: need total 12 -> 3 apices impossible (suspension adds 2).
# Another: join of C6 with path? must be sphere. Skip.
