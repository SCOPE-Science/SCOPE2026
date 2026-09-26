"""Corrected negative-definite star plumbing P for Y=Sigma(2,3,11).

Seifert data (oriented as integer homology sphere with e=-1/66):
  Y = M(-2; 1/2, 2/3, 9/11).
Legs (Hirzebruch-Jung): 2/1=[2], 3/2=[2,2], 11/9=[2,2,2,2,3].
Vertices (9): c0(-2); a1(-2); b1(-2)-b2(-2); c1(-2)-...-c4(-2)-c5(-3).
Checks: det(QP)=-1 (|H1|=1, homology sphere), negative-definite (sig=-9),
Seifert Euler e=-2+1/2+2/3+9/11=-1/66. Cap summand N=-P positive-definite
rank 9, sig=+9. Closed cap Xhat=C U N: chi=1+10=11, sig=9,
formal dim d(K)=(K^2-2e-3sig)/4=(K^2-49)/4. Adjunction table for cap spheres.
"""
import json
from fractions import Fraction as F
import numpy as np
import sympy as sp

names = ['c0', 'a1', 'b1', 'b2', 'c1', 'c2', 'c3', 'c4', 'c5']
w = {'c0': -2, 'a1': -2, 'b1': -2, 'b2': -2, 'c1': -2, 'c2': -2,
     'c3': -2, 'c4': -2, 'c5': -3}
edges = [('c0', 'a1'), ('c0', 'b1'), ('b1', 'b2'), ('c0', 'c1'),
         ('c1', 'c2'), ('c2', 'c3'), ('c3', 'c4'), ('c4', 'c5')]
idx = {v: i for i, v in enumerate(names)}
n = len(names)
QP = sp.zeros(n)
for v, i in idx.items():
    QP[i, i] = w[v]
for u, v in edges:
    QP[idx[u], idx[v]] = QP[idx[v], idx[u]] = 1
QN = -QP
QNinv = QN.inv()

def main():
    detP = int(QP.det())
    detN = int(QN.det())
    evP = np.linalg.eigvalsh(np.array(QP.tolist(), dtype=float))
    evN = np.linalg.eigvalsh(np.array(QN.tolist(), dtype=float))
    sigP = int((evP > 1e-9).sum() - (evP < -1e-9).sum())
    sigN = int((evN > 1e-9).sum() - (evN < -1e-9).sum())
    eul = F(-2) + F(1, 2) + F(2, 3) + F(9, 11)
    assert eul == F(-1, 66), eul
    assert abs(detP) == 1, detP
    assert all(x < 0 for x in evP), "P must be negative-definite"
    chi, sig = 11, 9  # closed cap Xhat = C U N
    out = {
        "seifert": "M(-2; 1/2, 2/3, 9/11), euler=-1/66",
        "legs_HJ": {"2/1": [2], "3/2": [2, 2], "11/9": [2, 2, 2, 2, 3]},
        "vertices": names,
        "weights": w,
        "QP": [[int(v) for v in row] for row in QP.tolist()],
        "QN": [[int(v) for v in row] for row in QN.tolist()],
        "det_QP": detP,
        "det_QN": detN,
        "eig_QP": [float(x) for x in sorted(evP)],
        "eig_QN": [float(x) for x in sorted(evN)],
        "sig_QP": sigP,
        "sig_QN": sigN,
        "H1_order": abs(detP),
        "negative_definite_P": True,
        "positive_definite_N": bool(all(x > 0 for x in evN)),
        "closed_cap": {"chi": chi, "sig": sig, "formal_dim": "(K^2-49)/4"},
    }
    diag = [int(QN[i, i]) % 2 for i in range(n)]
    out["char_parity"] = [int(x) for x in diag]
    out["QNinv"] = [[int(v) for v in row] for row in QNinv.tolist()]
    rows = []
    R = 2
    for tup in np.ndindex(*([2 * R + 1] * n)):
        K = [t - R for t in tup]
        if any((K[i] - diag[i]) % 2 != 0 for i in range(n)):
            continue
        Kv = sp.Matrix(K)
        ksq = int((Kv.T * QNinv * Kv)[0])
        rows.append({"K": K, "Ksq": ksq, "d": (ksq - 49) / 4})
    rows.sort(key=lambda r: r["Ksq"])
    out["char_sample_box"] = R
    out["char_sample_count"] = len(rows)
    out["min_Ksq_sample"] = rows[0]["Ksq"] if rows else None
    out["smallest_rows"] = rows[:10]
    out["nonneg_d_in_box"] = sum(1 for r in rows if r["d"] >= 0)
    # Adjunction table: cap spheres = vertices of N, each an embedded S^2
    # with square = -w_P = +2 (x8) or +3 (x1), g=0. Bound: -2 >= S^2 + |K.S|.
    adj = []
    for v in names:
        sq = -w[v]
        adj.append({"sphere": v, "square": sq, "genus": 0,
                    "bound": f"-2 >= {sq} + |K.[{v}]|",
                    "satisfiable": False,
                    "reason": f"S^2={sq}>0 forces RHS>=+{sq}>-2 for every K"})
    out["adjunction_table"] = adj
    out["collision"] = ("Every cap sphere has g=0, S^2 in {+2,+3}; the SW "
                        "adjunction inequality -2>=S^2+|K.S| is unsatisfiable "
                        "for every spin-c K. Hence the naive closed cap "
                        "Xhat=C U (-P) carries no basic classes on either side: "
                        "SW=0 identically. A b2+-large/symplectic cap (Milnor "
                        "fiber M(2,3,11)) is required for the witness route.")
    with open("plumbing_result.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"detP={detP} detN={detN} sigP={sigP} sigN={sigN} euler={eul}")
    print(f"char_sample={len(rows)} minKsq={out['min_Ksq_sample']} nonneg_d={out['nonneg_d_in_box']}")
    print("PLUMBING_OK")

if __name__ == "__main__":
    main()
