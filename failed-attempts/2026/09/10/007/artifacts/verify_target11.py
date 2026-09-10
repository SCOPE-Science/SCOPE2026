"""Target lemma audit 11 (TARGET phase): exact N diagonalization (removes half the quote).

Proves (exact integer matrix algebra):
 D1. N = [[0,1],[1,-1]] diagonalizes over ZZ: with P = [[1,0],[1,1]]
     (det +1), P^T N P = diag(+1,-1). Exact sympy check below.
     Interpretation: e1 = F+S (square +1), e2 = S (square -1), e1.e2 = 0.
 D2. Hence charitable Q_X = -E8 (+) N is EXACTLY (over ZZ) -E8 (+) <+1> (+) <-1>
     (block-explicit congruence). Full 10-form stays indefinite odd
     (rank 10, det -1, sig -8) => Serre indefinite classification (quoted)
     gives Q_X ~= diag(+1,-1^9). The quoted step is now isolated to the
     indefinite full-rank statement only; the N-block identification is exact.
 D3. K_X = -F in the diagonalized block: F = e1 - e2, so K = -e1 + e2,
     K^2 = (+1) + (-1) - 0 = 0 (exact). Characteristic recheck in N-block:
     K.F = 0 = F^2 mod 2; K.S = -1 = S^2 mod 2 (exact).
"""
import json
import sympy as sp

out = {"lemmas": {}, "checks": {}}
N = sp.Matrix([[0, 1], [1, -1]])
P = sp.Matrix([[1, 0], [1, 1]])
assert int(P.det()) == 1
D = P.T * N * P
out["lemmas"]["D1"] = {"P": [[1, 0], [1, 1]], "det_P": int(P.det()),
    "P^TNP": [[int(D[i, j]) for j in range(2)] for i in range(2)],
    "e1": "F+S, e1^2=+1", "e2": "S, e2^2=-1", "e1.e2": int(D[0, 1])}
out["checks"]["D1_diag_1_minus1"] = (D == sp.diag(1, -1))

# D2: full block congruence
E8 = sp.Matrix([[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,0],
                [0,0,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,-1],[0,0,0,0,-1,2,-1,0],
                [0,0,0,0,0,-1,2,0],[0,0,0,0,-1,0,0,2]])
G = sp.zeros(10); G[:8,:8] = -E8; G[8,8]=0; G[8,9]=1; G[9,8]=1; G[9,9]=-1
Q = sp.zeros(10); Q[:8,:8] = -E8; Q[8,8]=1; Q[9,9]=-1
B = sp.eye(10); B[8:10, 8:10] = P
assert int(B.det()) == 1
QT = B.T * G * B
out["lemmas"]["D2"] = {"block_congruence": "B^T G B = -E8(+)<+1>(+)<-1>",
    "exact": bool(QT == Q), "det_B": int(B.det()),
    "quoted_remainder": "Serre indefinite odd (rank10/det-1/sig-8) => ~= diag(+1,-1^9)"}
out["checks"]["D2_exact"] = bool(QT == Q)

# D3: K in diagonalized block
K = sp.Matrix([0]*8 + [-1, 0])  # -F in (F,S) coords
Kd = B.inv() * K  # coords in (e1,e2) basis: F=e1-e2 => -F=-e1+e2
Kd = [int(v) for v in Kd]
K2 = int((K.T*G*K)[0])
F = sp.Matrix([0]*8 + [1, 0]); S = sp.Matrix([0]*8 + [0, 1])
KF = int((K.T*G*F)[0]); KS = int((K.T*G*S)[0])
F2 = int((F.T*G*F)[0]); S2 = int((S.T*G*S)[0])
out["lemmas"]["D3"] = {"K_diag_block_coords": Kd, "expect": "[0]*8+[-1,+1]",
    "K^2": K2, "K.F": KF, "F^2": F2, "K.S": KS, "S^2": S2,
    "char_mod2": (KF % 2 == F2 % 2 and KS % 2 == S2 % 2)}
out["checks"]["D3"] = (Kd == [0]*8 + [-1, 1] and K2 == 0
                       and KF % 2 == F2 % 2 and KS % 2 == S2 % 2)
out["checks"]["target_closed"] = False

with open("output/artifacts/target_audit11.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
print("ARTIFACT_WROTE output/artifacts/target_audit11.json")
