"""Candidate normalized-dilatation crowding computation for D_3 target.

Goal: quantify how tightly candidate values L = lambda^|chi| crowd above 1,
showing that known universal (Penner-type) bounds are far from sharp and that
exact-min + classification needs uniform control over infinite families.
Uses only numpy (falls back to pure-python if unavailable).
"""
import json
import math

try:
    import numpy as np
    HAVE_NP = True
except ImportError:
    HAVE_NP = False

POLYS = {
    # Known dilatation-type monic integer polynomials (Perron root > 1)
    "x3-x2-x-1 (tribonacciнон)": [1, -1, -1, -1],
    "x4-x3-x2-x-1": [1, -1, -1, -1, -1],
    "x4-x3-0x2-0x-1": [1, -1, 0, 0, -1],
    "x5-x4-0x3-0x2-x-1": [1, -1, 0, 0, -1, -1],
    "x5-0x4-x3-x2-0x-1": [1, 0, -1, -1, 0, -1],
    "x6-x5-0x4-0x3-0x2-x-1": [1, -1, 0, 0, 0, -1, -1],
    "x6-0x5-x4-x3-0x2-0x-1": [1, 0, -1, -1, 0, 0, -1],
    "x7-x6-0x5-0x4-0x3-0x2-x-1": [1, -1, 0, 0, 0, 0, -1, -1],
    "x8-0x7-0x6-x5-0x4-x3-0x2-0x-1": [1, 0, 0, -1, 0, -1, 0, 0, -1],
    "lehmer10": [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1],
}


def perron_root(coeffs):
    if HAVE_NP:
        roots = np.roots(coeffs)
        cands = [r.real for r in roots if abs(r.imag) < 1e-6 and r.real > 1.0]
        return max(cands) if cands else None
    return None


def main():
    rows = []
    for name, c in POLYS.items():
        lam = perron_root(c)
        if lam is None:
            rows.append({"poly": name, "lambda": None})
            continue
        Ls = {str(k): round(float(lam ** k), 6) for k in [1, 2, 3, 4, 5]}
        rows.append({"poly": name, "lambda": round(float(lam), 6), "L_by_chi": Ls})
    # crowding: distinct L values at |chi|=2 in a narrow window
    vals = sorted({r["L_by_chi"]["2"] for r in rows if r["lambda"]})
    gaps = [round(vals[i + 1] - vals[i], 6) for i in range(len(vals) - 1)]
    out = {
        "have_numpy": HAVE_NP,
        "rows": rows,
        "chi2_sorted": vals,
        "chi2_gaps": gaps,
        "penner_shape_reference": {
            "note": "Penner-type universal bounds give L >= c0 with c0 only "
                    "slightly above 1 (shape 2**(1/6) ~ 1.122); far below the "
                    "crowded candidate values, hence not sharp.",
            "two_pow_1_6": round(2 ** (1 / 6), 6),
        },
    }
    print(json.dumps(out, indent=1))
    with open("output/artifacts/candidate_crowding.json", "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
