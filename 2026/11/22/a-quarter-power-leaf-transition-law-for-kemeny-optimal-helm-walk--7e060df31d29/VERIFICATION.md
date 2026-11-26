---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

On the connected part of the compact feasible weight polytope, the inverse trace of L+J is strictly convex: diagonalizing L+J writes its second variation as a positively weighted sum of squares of the entries of any nonzero perturbation. The cost diverges as support disconnects; uniqueness enforces dihedral invariance among all edge-by-edge feasible walks. An independent check of the reduced objective uses effective resistances. Each pendant edge contributes (2n)/c to the Kirchhoff index; collapse the pendant leaves for the core part, counting each rim vertex twice and the hub once. In the weighted wheel, the sum of core rim-pair resistances is nS, and the sum of hub-rim resistances is 1/a+S, where S=Σ_{k≠0}1/(a+2bt_k): each hub-rim pair has uniform-mode resistance 1/(na) and nonuniform-mode contribution S/n. The core index therefore contributes 4nS+2(1/a+S). Dividing the total index by 2n+1 recovers A_n/c+B_n/a+2S. Increasing b always helps until rim capacity binds. The trial at a=1/n, c=n^(-1/4) and the resolvent comparison with w≤1−ε exclude c≥ε for large n. At fixed c≤1/4 and a≤1/n the sum of (1−t_k)/(a+wt_k)^2 has positive contribution of order n^(5/2) from k≤√n/8, versus negative part O(n). There is a missing factor of two if RESULT.md line 87 is read as the derivative of the entire last term of F_n; its sign is unchanged, and the hub saturation argument uses only the sign. The scalar c-derivative has opposite endpoint signs and is strictly increasing. The exact resolvent can be replayed by expanding (a+w−w cos θ)^(-1) in Fourier coefficients proportional to exp(−|k| acosh(1+a/w)) and averaging at the n grid points. At a=1/n and w→1, differentiating gives −∂_w(2S)∼n^(3/2)/√2, so c_n∼2^(1/4)n^(-1/4). The linear resolvent correction and A_n/c_n each contribute 2^(-1/4)n^(5/4). For the maximum-degree walk the remaining Riemann mean is 1/√5, confirming both comparison constants. This establishes eventual, not explicitly thresholded, hub saturation and the claimed asymptotics only for the stated symmetric stochastic domain and zero-target convention. The bundled finite diagnostics were read, not executed or treated as proof.

## originality

PASS

Bounded to the combined helm result: the quarter-power pendant allocation with its constant and the second optimum term, together with eventual exact hub saturation in the presence of rim pendants. General convexity, wheel hub saturation on its own, and the cyclic resolvent are not new. Inspected close sources do not give an equivalent optimization result or a dominating theorem yielding these claims.

## value

PASS

A classical graph combines two competing uses of rim probability mass. The optimum has an exact eventual active constraint but an intermediate, non-obvious pendant scale, neither the bare-wheel allocation nor the sunlet scale. The second term identifies the cost of that trade-off, and the diverging maximum-degree benchmark gap gives a concrete reason the optimized allocation matters. This is an asymptotic design result for the specified uniform-stationary family, not a claim about arbitrary routing or a numerical sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
