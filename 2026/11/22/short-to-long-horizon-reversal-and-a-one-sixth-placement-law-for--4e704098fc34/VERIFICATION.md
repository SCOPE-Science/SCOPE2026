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

All augmentations have n edges and equal linear trace term. The trace of L² is the sum of squared degrees plus 2n. Hence the first difference from cycle closure is (d_a+d_b−2)t² with the original path degrees; only the endpoint pair makes this coefficient zero. For large time, rank-one interlacing caps the gap at Λ_n. Equality requires b orthogonal to the second positive path mode: otherwise the first two positive modes contain a vector orthogonal to b of Rayleigh quotient strictly below Λ_n. Equality of the two endpoint cosines of the second mode forces reflection centering. Write θ=2π/n and φ=(i+1/2)θ. On the odd-reflection subspace the shifted path Laplacian A has inertia (one negative, no zero, all others positive). Solving Ay=b_i uses c cos((j+1/2)θ) before the source and c cot(φ) sin((j+1/2)θ) after it on the left half; matching is exact at the source, and choosing c=−sin(φ)/sin(θ) gives jump residual 1. The odd reflection gives the other source −1, so b_i^T A^{-1}b_i=−sin((2i+1)θ)/sinθ. The block Schur complement with bottom entry −1 shows that 1+b_i^T A^{-1}b_i≤0 is exactly saturation, with equality giving an extra eigenvalue at Λ_n. This yields the displayed unit-weight index set. The first interior chord has 1+b_i^T A^{-1}b_i=2−4cos²θ<0 for n≥9, whereas cycle closure has equality. Thus the trace difference starts with −exp(−Λ_n t), and finite exponential-sum comparisons stabilize. A gap-saturating simple-gap eventual optimum must maximize the second positive eigenvalue. On the half interval scale a full discrete unit vector by sqrt(2n) and interpolate; its squared derivative norm is n² times the full path difference energy (including the central half-step for even n); its L² norm tends to 1 for bounded rescaled energy. The term 4n²|v_i|² forces the scaled interpolant to vanish at the limiting chord point. Compactness and lower semicontinuity give the minimum of the Neumann–Dirichlet and Dirichlet–Dirichlet eigenvalues. Sampling the first mode of the cheaper interval with a node at the actual chord vertex gives the matching upper bound, using the right interval alone when the limiting left interval degenerates. The next symmetric eigenvalue tends after scaling to 16π², above the maximum 9π² of this odd-sector limit. Comparing with an index near n/6 along every subsequence then proves the optimizer placement law.

## originality

PASS

The unit-weight gap-saturating placement classification is known and is not credited as new. The contribution supported by the comparisons is the heat-trace reversal for one added nonedge, the multiplicity splitting at a fixed optimal gap, and the second-mode eventual placement law. The same-day path heat-trace result changes weights on existing edges under a budget rather than adding a single edge, so the stated results concern different feasible sets.

## value

PASS

There is a concrete design distinction: all sufficiently short horizons choose the cycle, while at long horizons another graph with the very same optimal gap beats it by changing the gap multiplicity. The limiting choice is not arbitrary on the known gap plateau; it balances two different boundary-value modes and fixes the macroscopic tail length. This gives a useful exact example where neither connectivity nor maximization of the gap by itself is enough for heat-trace design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
