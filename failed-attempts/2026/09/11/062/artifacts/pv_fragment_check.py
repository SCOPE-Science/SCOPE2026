"""Bounded recovery test: generic K-theory fragments relevant to lane-853 target.
No original claim; only checks what can be pinned without the named model's maps.
Replay: python3 pv_fragment_check.py -> prints VERIFY lines.
Uses stdlib only.
"""
import math
from itertools import combinations

def snf_coker_3x3(M):
    entries = [abs(x) for r in M for x in r if x != 0]
    d1 = math.gcd(*entries) if entries else 0
    minors = []
    for rs in combinations(range(3), 2):
        for cs in combinations(range(3), 2):
            d = M[rs[0]][cs[0]]*M[rs[1]][cs[1]] - M[rs[0]][cs[1]]*M[rs[1]][cs[0]]
            minors.append(abs(d))
    g2 = math.gcd(*minors) if any(m != 0 for m in minors) else 0
    return d1, g2, minors

# (a) I-P for 3-cycle permutation on Z^3 (finite-stage toy, NOT the target model)
M = [[1,0,-1],[-1,1,0],[0,-1,1]]
d1, g2, minors = snf_coker_3x3(M)
print("toy I-P: gcd entries =", d1, "; gcd 2x2 minors =", g2)
print("toy coker = Z (SNF diag 1,1,0)); ker = Z")
assert d1 == 1 and g2 == 1

# (b) Generic PV fragment for ANY automorphism of Z itself:
# K0(Z)=Z, K1(Z)=0, automorphism acts trivially on K0, so id-alpha_*=0.
# PV then forces K0(Z rtimes_alpha Z)=Z, K1=Z, torsion-free.
# Hence Z/3 torsion in Z rtimes_gamma Z/3 (finite-group crossed product)
# cannot come from this PV route; it needs the unstated equivariant/
# finite-stage connecting maps. With those maps absent, torsion is unpinned.
print("generic PV-for-Aut(Z): K0(cross x Z)=Z, K1=Z, no torsion")
print("conclusion: finite-group torsion value unpinned without named maps")
print("VERIFY_OK")
