---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Positive acceptance gives a copying path to consensus from every transient state, making the finite-chain Dirichlet solution unique. Conditional on a hub holding 0, the total rates for hub flip and leaf decrement are α01 k/m and α10 k; conditional on hub holding 1, hub flip and leaf increment have rates α10(m−k)/m and α01(m−k). Dividing by the nonzero k or m−k factors on the corresponding transient intervals gives F_k−F_{k−1}=(r/m)(G_k−F_k) and G_{k+1}−G_k=(1/(rm))(G_k−F_k). Subtraction at consecutive indices multiplies D_k=G_k−F_k by (1+1/(rm))/(1+r/m)=q_m, and the boundaries F_0=0, G_m=1 give D_0=1/Z_m. At equal total seeds the difference is D_{k−1}(1−r q_m/m), whose second factor is (m²−1)/(m(m+r)); this also verifies the m=1 tie. The single-seed ratio is m/(r q_m). At fixed r, m log q_m tends to r^{-1}−r, giving uniform exponential convergence for the powers with 0≤j≤m and hence the moving-endpoint Riemann sums. The neutral case has q_m=1 and Z_m=2. The m=4, r=2 illustration gives q_m=3/4 and Z_m=687/512 as stated. The full-chain checker verify.py was inspected, not executed. Its exact finite cases are corroboration only. The frozen Python 3.8 compatibility note is too broad: int.bit_count at line 60 requires Python ≥3.10, without affecting the theorem.

## originality

PASS

Credit the context-dependent adoption model, its regular-graph law, the neutral case and the equivalence to death–birth with selection on death. The supported distinct claim is the all-initial-state biased law on nonregular stars for this kernel, with exact hub-placement gain and fixed-bias scaling. The closest inspected model-equivalent general paper's scalar count reduction does not apply; the exact star formulas inspected for different replacement rules are not mechanically applicable. Possible broader weighted directed BD coverage in Monk–Green–Paulin could not be confirmed from primary text and remains a specific limit, not evidence of noncoverage.

## value

PASS

On this nonregular graph an adopter count loses the distinction between the hub and leaves. The all-state law restores that dependence in a solvable form and gives an exact placement decision at every fixed seed budget. The distinct nonvanishing hub probability and inverse-size leaf probability at fixed directional bias quantify a degree effect that a regular-graph count formula or neutral degree weighting alone does not provide.

The dated certificate retains the supplied scientific assessment, sources and limitations.
