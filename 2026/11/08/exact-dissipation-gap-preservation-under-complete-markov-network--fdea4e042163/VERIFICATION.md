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

For i≠j, the aggregated opposing fluxes are A=P_i q_ij and B=P_j q_ji; their normalized laws are μ_i⊗ν_j and ν_i⊗μ_j. Summing (x−y)log(x/y) over clone pairs yields (A−B)log(A/B) plus A and B times the corresponding directed KL divergences, each additive across coordinates. In block i, summing the opposing exchange fluxes gives c_iP_i times the two-sided divergence between μ_i and ν_i; including diagonal pairs in the product-law calculation changes nothing because their log flux ratio is zero. This verifies each outgoing/incoming coefficient and includes n=1. The penalty vanishes exactly at p_ia=P_iν_i(a). Strict positivity of all rates implies divergence at every boundary law (take an edge joining positive mass and zero mass), hence an interior minimum exists by compactness and lower semicontinuity. Each coarse optimizer has its equality lift and all microscopic optimizers are such lifts. The weighted stationary law follows from coarse balance, with within-block flows cancelling pairwise; exits are bounded by q_i^out+c_i. For the seed, exact rational stationarity and both flux expressions were independently reproduced. The opposing cycle products 6 and 1520 exclude detailed balance, so the minimum is positive. A separate rational dyadic-atanh enclosure gives 50σ_Q(π)−59σ_Q(P*)>4.56 (lower endpoint approximately 4.561926684795). Since the minimum is at most σ_Q(P*), the relative excess is greater than 9/50 for all sizes. This is a bound, not the exact optimizing distribution or an absolute difference.

## originality

PASS

The conditional KL decomposition is established coarse-graining machinery, not new. Likewise the existence of a three-state stationary-versus-minimum discrepancy is old. The supported distinct claim is a positive-rate destination-weighted realization of arbitrary complete-state refinements, with equality on all lifted laws and an explicit fixed relative-gap witness persisting at unbounded sizes and bounded exits. The inspected antecedents supply ingredients but do not produce this complete-network counterexample or establish a general refinement with these constraints.

## value

PASS

This is a constructive boundary to an inference from complete connectivity and growing state count to near-minimum stationary dissipation. It controls the actual global minimum, admits nonuniform microscopic occupations, and supplies a dimension-independent positive relative bound without increasing exit rates. Those features make it a useful deterministic counterexample independent of the KL identity's originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
