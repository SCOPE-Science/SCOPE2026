"""Exact integer Smith census of balanced cuts of the Fano incidence graph.
Requires Python 3.10+ and sympy 1.12+. Run: python verify_smith.py
"""
from collections import Counter
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

LINES = [frozenset(((s)%7, (s+1)%7, (s+3)%7)) for s in range(7)]
assert len(set(LINES)) == 7
assert all(sum(a in L for L in LINES) == 3 for a in range(7))
assert all(sum(a in L and b in L for L in LINES) == 1
           for a in range(7) for b in range(a+1,7))
A = [[0]*14 for _ in range(14)]
for i in range(7):
    for j,L in enumerate(LINES):
        A[i][j+7] = A[j+7][i] = int(i in L)

smith_hist = Counter()
rank_hists = {p: Counter() for p in (2,3,5,7,11,101)}
mod3_defects = set()
for S in combinations(range(14), 7):
    if 0 not in S: continue  # one cut per complementary unordered pair
    C = [i for i in range(14) if i not in S]
    M = Matrix([[A[i][j] for j in C] for i in S])
    SNF = smith_normal_form(M, domain=ZZ)
    invariants = tuple(int(abs(SNF[i,i])) for i in range(7) if SNF[i,i])
    smith_hist[invariants] += 1
    for p in rank_hists:
        rank_hists[p][sum(d%p != 0 for d in invariants)] += 1
    if sum(d%3 != 0 for d in invariants) != len(invariants):
        mod3_defects.add(frozenset(S))

EXPECTED_SMITH = {
    (1,1,1,1):21,
    (1,1,1,1,1):273,
    (1,1,1,1,1,1):476,
    (1,1,1,1,1,1,1):336,
    (1,1,1,1,1,2):196,
    (1,1,1,1,2,2):28,
    (1,1,1,1,1,1,2):252,
    (1,1,1,1,1,1,4):84,
    (1,1,1,1,1,2,4):21,
    (1,1,1,1,1,1,6):28,
    (1,1,1,1,2,2,6):1,
}
assert dict(smith_hist) == EXPECTED_SMITH
assert sum(smith_hist.values()) == 1716
assert len(mod3_defects) == 29

# Geometric description: one point-versus-line cut and a cut for
# each Fano noncollinear triangle T: four points outside T and
# three Fano lines joining pairs of T.
canonical = frozenset(range(7))
assert canonical in mod3_defects
triangle_cuts = set()
for Ttuple in combinations(range(7),3):
    T = set(Ttuple)
    if any(T.issubset(L) for L in LINES): continue
    side_lines = [7+j for j,L in enumerate(LINES) if len(L & T)==2]
    assert len(side_lines)==3
    S = frozenset((set(range(7)) - T) | set(side_lines))
    if 0 not in S: S = frozenset(set(range(14))-S)
    triangle_cuts.add(S)
assert len(triangle_cuts) == 28
assert mod3_defects == triangle_cuts | {canonical}
assert dict(rank_hists[2]) == {4:50,5:490,6:840,7:336}
assert dict(rank_hists[3]) == {4:21,5:273,6:729,7:693}
for p in (5,7,11,101):
    assert dict(rank_hists[p]) == {4:21,5:273,6:700,7:722}
print('PASS: 1716 unordered cuts; 11 complete integer Smith classes')
print('Smith histogram:', sorted(smith_hist.items()))
print('Rank histograms:', {p:dict(sorted(h.items())) for p,h in rank_hists.items()})
print('Characteristic-three exceptional cuts: canonical + 28 noncollinear triangles')
