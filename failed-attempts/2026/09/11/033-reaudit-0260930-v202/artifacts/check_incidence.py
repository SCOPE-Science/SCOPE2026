"""B*_3 obstruction-incidence check (auditor repair item 2).

Extension-index <-> (i,j) map (fixed ordering of 4*Delta_2 lattice points):
  0:(0,0) 1:(1,0) 2:(0,1) 3:(2,0) 4:(1,1) 5:(0,2) 6:(3,0) 7:(2,1)
  8:(1,2) 9:(0,3) 10:(4,0) 11:(3,1) 12:(2,2) 13:(1,3) 14:(0,4)

Claim: motif dual edge (7,8) = ((2,1),(1,2)) = focus edge e*.
B*_3 = first BM+(yz) motif in polymake ordering, triangles
  [[4,5,8],[4,7,8],[6,7,11]], sym 0 (gw_table row B*_4; the admitted label B*_3
  is fixed to this class throughout).
The motif triangle [4,7,8] contains the dual edge (7,8); the two T_H
triangles sharing (7,8) are [4,8,7] and [8,7,12], so with apexes
r=(1,1)[index 4], r'=(2,2)[index 12] and delta=1 (apexes differ mod 2),
MPS Def 3.5 gives twist radicand R* = (-1)^1 a_11 a_22 (a_12 a_21)^1 = -2
under logged initials a_11=2, else 1.

Shape-B overlap: B*_3 resolved to Cueto-Markwig shape B at generic weights
w (dots 3/2, 5/2, -3/2 nonzero) by the extension's find_shapes_BMB rule
(B unless dot==0, i.e. M). A shape-B class has a bounded segment partly
overlapping an edge of Trop(C) with the two liftable members at the segment
endpoints, each of lifting multiplicity 2 (MPS proof of Thm 4.23, shape-D
pattern reference; Lemma 4.18 pairing applies to the horizontal/vertical
overlap tangency). ALTERNATIVE (used for the verdict, no single-edge
dependence): twist_gw.py logs ALL 18 bounded edges twisted under a*, so
whichever bounded edge the shape-B overlap segment lies on, that tangency
is twisted; e* with R*=-2 is the certified representative nonsquare ratio.

Obstruction chain (exact MPS cites):
  Lemma 3.4 (local lifting solutions: line coefficient M needs the square
    root of the twist radicand up to a monomial square),
  + Prop 3.8 (local equation defined over K iff edge untwisted),
  + Thm 3.14 (all four lifts of a bitangent class share one obstruction:
    either all four defined over K or none),
  => B*_3 has 4 geometric lifts, 0 over K=Q((t)) since sqrt(-2) not in Q.
"""
import json
from fractions import Fraction

EXT = [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3),
       (4,0),(3,1),(2,2),(1,3),(0,4)]

# 1. index map ground truth
assert EXT[7] == (2,1) and EXT[8] == (1,2), (EXT[7], EXT[8])
assert EXT[4] == (1,1) and EXT[12] == (2,2)
print("PASS index map: (7,8)=((2,1),(1,2))=e*, r=(1,1)[4], r'=(2,2)[12]")

# 2. B*_3 identity and edge containment
mo = json.load(open('output/artifacts/motifs_full.json'))
bm = [m for m in mo if m['type'] == 'BM+(yz)']
assert len(bm) == 3, len(bm)
b3 = bm[0]
assert sorted(map(sorted, b3['triangles'])) == [[4,5,8],[4,7,8],[6,7,11]], b3
assert [4,7,8] in [sorted(t) for t in b3['triangles']]
print("PASS B*_3 triangles [[4,5,8],[4,7,8],[6,7,11]]; motif triangle [4,7,8] contains dual edge (7,8)")

# 3. T_H edge (7,8) shared by exactly the two triangles dual to its endpoints
cells = [[0,2,1],[1,4,3],[2,1,4],[2,5,4],[3,7,6],[4,3,7],[4,8,7],[5,4,8],
         [5,9,8],[6,11,10],[7,6,11],[7,12,11],[8,7,12],[8,13,12],[9,8,13],[9,14,13]]
sharers = [t for t in cells if 7 in t and 8 in t]
assert sorted(map(sorted, sharers)) == [[4,7,8],[7,8,12]], sharers
print("PASS T_H triangles sharing (7,8): [4,8,7] and [8,7,12]; apexes 4=(1,1), 12=(2,2)")

# 4. twist radicand from logged initials
q = json.load(open('output/artifacts/qstar.json'))
a = {tuple(map(int, k.split(','))): Fraction(v) for k, v in q['initials'].items()}
R = Fraction(-a[(1,1)]*a[(2,2)]*a[(1,2)]*a[(2,1)])
assert R == -2, R
assert R < 0  # nonsquare in Q (ordered field); |R|=2 not an integer square
import math
assert math.isqrt(2)**2 != 2
print("PASS R*=-2 nonsquare in Q (MPS Def 3.5, delta=1: apexes (1,1),(2,2) differ mod 2)")

# 5. shape resolution + MPS cites
sh = json.load(open('output/artifacts/shapes.json'))['shapes']
bshapes = [s for s in sh if s['type'] == 'BM+(yz)']
assert len(bshapes) == 3 and all(s['shape'] == 'B' for s in bshapes), bshapes
assert all(Fraction(s['dot']) != 0 for s in bshapes)
print("PASS B*_3 shape B at generic w (find_shapes_BMB: dot nonzero -> B)")
# 6. all-18-twisted alternative: overlap edge is twisted whichever it is
import subprocess, sys
r = subprocess.run([sys.executable, 'output/artifacts/twist_gw.py'],
                   capture_output=True, text=True)
assert 'twisted count: 18' in r.stdout, r.stdout[-500:]
print("PASS all 18 bounded edges twisted (twist_gw.py) -> shape-B overlap tangency twisted")
print("CITES: MPS Lemma 3.4 + Prop 3.8 + Thm 3.14 => 4 geometric, 0 K-rational lifts")
print("INCIDENCE_OK")
