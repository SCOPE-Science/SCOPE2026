---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Color-exchange symmetry makes each signed draw centered with variance one. Conditional on the state before draw i, its mean is D_(i-1)/T_(i-1). Independence of the selected rule gives E[S_i D_i]=W_(i-1)+h, since D_i=D_(i-1)+J_i S_i. Iterating the conditional imbalance drift up to j-1 recovers the exact all-lag formula in RESULT.md:39–44, including its denominator T_(j-1); all lag factors are positive. Squaring the update gives W_n-W_(n-1)=[q-(B-2h)W_(n-1)]/T_n. For h>=0 the first sign is determined directly, and W_n>0 for n>=1 because q>0. For h<0, d=B-2h and W_n=(q/d)(1-G_n). The factor (T_(n-1)+2h)/T_n lies in (0,1) under the initial-mass bound; the sum of d/T_n diverges, so G_n strictly decreases to zero. The limiting sign numerator has the sign of q+hd=8b^2 p(p_*-p); at equality the finite-age numerator is still strictly negative. For p approaching p_* from below the first crossing is exactly G_n<=epsilon_p=(q+hd)/q. The uniform Stirling ratio on a compact p-neighborhood gives G_n/(K(p)n^(-d/B))=1+O(1/n). Monotonicity brackets the first integer crossing between (1±eta)(K(p)/epsilon_p)^(B/d) for each fixed eta>0, up to integer rounding, and (p_*-p)log(p_*-p)→0 controls the varying power. Substitution gives the stated prefactor and exponent. At p_* the adjacent numerator is h_*G_(i-1); dividing by T_i gives h_*K_*/B and exponent 1+2b/B. At other negative drifts the limiting numerator is nonzero, yielding the stated i^(-1) term. An independently written rational outcome-tree calculation enumerated whole six-draw histories and matched 105 joint draw pairs (seven settings). This corroborates the recurrence and indices; it does not establish the infinite-age claims. The supplied checker was inspected, not executed, and its count is recorded rather than independently attested.

## originality

PASS

Against the examined evidence the distinct contribution is the exact sampled-draw time-pair sign classification and sharp second-threshold aging law, not the mixed replacement model, the drift identities, or limit theorems for composition. No examined prior result states or directly specializes to the complete claim.

## value

PASS

Sampled colors are a directly observable process, distinct from the evolving composition. The exact separation of first-draw and late-age persistence thresholds resolves when early observations give the opposite sign to later observations, uniformly over the lag. Computing the divergence constant as well as the power, and identifying a different power of covariance precisely at the second threshold, makes this a substantive finite-to-asymptotic classification rather than an isolated moment identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
