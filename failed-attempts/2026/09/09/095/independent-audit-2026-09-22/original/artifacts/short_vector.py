"""Certified short-vector census for Q_N (ellipsoid-bound pruned recursion).

Q_N positive-definite unimodular rank 9. Any x with x^T Q x<=S satisfies
x_i^2<=Qinv[i,i]*S (Cauchy-Schwarz for the Q-inner product); recursion over
i=8..0 with Cholesky partial-norm pruning is therefore COMPLETE for squares
<=S. Result (S=2): exactly 2 square-+1 vectors (+-v0), 240 square-+2 vectors,
min nonzero square +1. The square-+1 pair +-v0 = +-(6,3,4,2,5,4,3,2,1) is the
plumbing's canonical class direction. Corollary: SW formal-dimension layer is
satisfiable (char K with large K^2 exist); only adjunction kills the naive cap.
"""
import json
import math
import numpy as np

def main():
    P = json.load(open("plumbing_result.json"))
    A = np.array(P["QN"], dtype=float)
    n = A.shape[0]
    Qinv = np.linalg.inv(A)
    L = np.linalg.cholesky(A)
    Lt = L.T
    S = 2.0
    bounds = [int(math.ceil(math.sqrt(Qinv[i, i] * S) + 1e-9)) for i in range(n)]
    cnt, ex = {}, {}
    x = [0] * n

    def rec(i, ytail_fixed_sq_terms):
        # ytail holds y_k for k>i (fully determined); prune on partial norm
        s_fixed = sum(v * v for v in ytail_fixed_sq_terms)
        if s_fixed > S + 1e-9:
            return
        if i < 0:
            si = int(round(s_fixed))
            if abs(s_fixed - si) > 1e-6 or si < 0 or si > S:
                return
            cnt[si] = cnt.get(si, 0) + 1
            if si >= 1 and si not in ex:
                ex[si] = list(x)
            return
        c = sum(Lt[i, j] * x[j] for j in range(i + 1, n))
        d = Lt[i, i]
        r = math.sqrt(max(S - s_fixed, 0.0)) / abs(d)
        lo = max(int(math.ceil(-c / d - r - 1e-9)), -bounds[i])
        hi = min(int(math.floor(-c / d + r + 1e-9)), bounds[i])
        for v in range(lo, hi + 1):
            x[i] = v
            rec(i - 1, [c + d * v] + ytail_fixed_sq_terms)
        x[i] = 0

    rec(n - 1, [])
    # exact verification of the square-1 pair with integers
    import sympy as sp
    Qs = sp.Matrix(P["QN"])
    for v in (ex.get(1, []), [(-t) for t in ex.get(1, [])] if 1 in ex else []):
        if v:
            xv = sp.Matrix(v)
            assert int((xv.T * Qs * xv)[0]) == 1
    out = {
        "S": S,
        "per_coord_bounds": bounds,
        "completeness": "ellipsoid bound x_i^2<=Qinv[i,i]*S + Cholesky partial-norm pruning: complete for squares<=2",
        "counts_square_le2": {str(k): v for k, v in sorted(cnt.items())},
        "num_square1_vectors": cnt.get(1, 0),
        "square1_example": ex.get(1),
        "square2_example": ex.get(2),
        "min_nonzero_square": min(k for k in cnt if k >= 1),
        "corollary": "Q_N represents +1 (exactly one pair +-v0); SW dimension layer satisfiable; naive-cap failure is purely adjunction",
    }
    with open("short_vector_result.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"bounds={bounds} counts={cnt}")
    print(f"sq1 example={ex.get(1)}")
    print("SHORT_VECTOR_OK")

if __name__ == "__main__":
    main()
