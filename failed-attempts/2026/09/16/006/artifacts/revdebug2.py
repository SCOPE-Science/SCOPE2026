import itertools
from flipsearch import stacked_chain, faceset_of, find_moves, apply_rev, check_valid
d=4; t=2
facets,colors,n=stacked_chain(d,t)
print('colors:',colors)
faces=faceset_of(facets)
fwd,rev=find_moves(facets,faces)
for (B,A) in rev[:6]:
    print('B=',sorted(B),'colorsB=',sorted(colors[v] for v in B),'A=',sorted(A),'colorsA=',sorted(colors[v] for v in A))
# reverse move adds edge between link apexes and removes all facets containing triangle B.
# Balance of new facets A|e: colors must be all-distinct. A has 2 verts; e has 2 verts. Need color(A)+color(e) = 4 distinct.
# B has 3 verts (3 distinct colors, missing color m). Link apexes a1,a2: facets a1|B, a2|B exist => a1,a2 both have color m. So A is MONOCHROMATIC pair!
# New facet A|e has colors {m,m}+2 colors => repeated color => UNBALANCED always. So reverse bistellar-II move can NEVER preserve balancedness.
# And forward move: edge A with triangle link: A={x,y} with x,y different colors? link triangle B must avoid colors of A => only 2 colors left, triangle needs 3 distinct => impossible.
# CONCLUSION: balanced 3-manifold triangulations admit NO interior bistellar 2-moves at all (edge-triangle flips break balancedness).
