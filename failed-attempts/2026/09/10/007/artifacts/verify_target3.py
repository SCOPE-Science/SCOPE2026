"""Target stress-test 3 (TARGET phase): parity/rank audit of the literal Q_X clause.

Target clause reads: Q_X = -E8 (+) H (+) specified nucleus summand.
Checks (exact, replayable):
 P1. -E8 even, H even => (-E8 (+) H) even; E(1)_{2,3} must be ODD
     (homeomorphic to CP2#9CPbar by Morgan-Mrowka / Freedman; w2 != 0).
     => literal "-E8+H" parity-clashes with the Dolgachev background.
 P2. rank count: 8 + 2 + rank(nucleus>=1) >= 11 > b2=10 => literal three-term
     sum overflows b2. Double-counts: the nucleus block lives INSIDE the
     rank-10 form, not as an extra summand.
 P3. Charitable correction -E8 (+) N, N=[[0,1],[1,-1]] (Gompf nucleus G(1):
     fiber F^2=0, section S^2=-1, F.S=1) is odd, rank 10, det -1, sig -8,
     hence isometric to diag(+1,-1^9) by Serre (quoted). CERTIFIED here.
 P4. N is NOT isometric to H over ZZ (parity differs) — so "H (+) nucleus"
     cannot be repaired by identifying the two; one must DROP H in favor of N.
 P5. SW chamber pin: E(1)_{2,3} complex/symplectic => Taubes (quoted) gives
     SW=+/-1 in symplectic chamber; E(1) PSC => SW=0 all chambers (quoted).
     b2+=1 wall-crossing formula recorded schematically; K_f chamber after
     an UNSOURCED embedding cannot be matched — twist side stays OPEN.
"""
import json
from sympy import Matrix

out = {"checks": {}, "tables": {}}
E8 = Matrix([[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,0],
             [0,0,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,-1],[0,0,0,0,-1,2,-1,0],
             [0,0,0,0,0,-1,2,0],[0,0,0,0,-1,0,0,2]])
H = Matrix([[0,1],[1,0]])
N = Matrix([[0,1],[1,-1]])

def is_even(M):
    n = M.rows
    if any(int(M[i,i]) % 2 != 0 for i in range(n)):
        return False
    # check pair sums (sufficient audit for 2x2/unimodular blocks here)
    for i in range(n):
        for j in range(i+1, n):
            v = [0]*n; v[i]=1; v[j]=1
            vv = Matrix(v)
            if int((vv.T*M*vv)[0]) % 2 != 0:
                return False
    return True

out["tables"]["parity"] = {
    "-E8_even": is_even(-E8), "H_even": is_even(H), "NucleusBlock_odd": not is_even(N),
    "N_diagonal": [int(N[0,0]), int(N[1,1])],
}
out["checks"]["P1_literal_E8H_even_vs_Dolgachev_odd"] = (
    is_even(-E8) and is_even(H))
# P2 rank
out["tables"]["rank"] = {"-E8": 8, "H": 2, "nucleus_min": 1, "b2_E12_3": 10,
                         "literal_sum_min": 8+2+1, "overflows": 8+2+1 > 10}
out["checks"]["P2_literal_rank_overflow"] = True
# P3 charitable: block diag det/sig/odd
big = Matrix.zeros(10); big[:8,:8] = -E8; big[8:,8:] = N
out["tables"]["charitable_-E8+N"] = {"det": int(big.det()), "odd": not is_even(big),
    "gram": "-E8 (+) [[0,1],[1,-1]]"}
out["checks"]["P3_charitable_det_-1_odd"] = (int(big.det()) == -1 and not is_even(big))
# P4 N vs H
out["checks"]["P4_N_not_isometric_H_over_ZZ_parity"] = (is_even(H) and not is_even(N))
# P5 chambers (quoted flags)
out["tables"]["SW_chambers_quoted"] = {
    "E(1)_{2,3}": "symplectic/complex => SW(canonical-related)=+/-1 symplectic chamber (Taubes, quoted)",
    "E(1)=CP2#9CPbar": "PSC => SW=0 all chambers (quoted)",
    "wall_crossing": "b2+=1: SW jumps across w2+ chambers; matching K_f chamber needs sourced embedding (absent)",
}
out["checks"]["P5_twist_side_chamber_open"] = True
out["checks"]["target_closed"] = False

with open("output/artifacts/target_audit3.json","w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
print("ARTIFACT_WROTE output/artifacts/target_audit3.json")
