---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For z away from the internal eigenvalues, the hub Schur complement subtracts (2z+2t_j cos φ_j)/(z²−t_j²) for each petal. Clearing denominators proves the determinant identity everywhere; the guaranteed multiplicities divide even when extra roots are present. After grouping equal t_j, evaluation at the distinct positive τ_r leaves only its corresponding class term with coefficient −2τ_r times the nonzero product of the squared-weight differences. This verifies the full cospectral equivalence, including class extrema, not only generic phases. Labelled cubic diagonal entries have exactly two closed walks, with conjugate phases, so they recover cos φ_j but not its sign. In the equal-weight example P=z(z²−1)(z²−5) for both assignments and the cubic difference is 6/5. Splitting the weights gives distinct polynomials. An independently built exact example at weights (1,1,3,4) with nontrivial complex phases checked polynomial division/evaluation and the cubic diagonals; replay with `OPENBLAS_NUM_THREADS=1 python /tmp/opencode/frozen-review-diagnostics.py` (check 2). The frozen exact and numerical scripts were inspected, not executed. Finite algebra checks supplement the all-size argument.

## originality

FAIL

The stated weighted complex gain Sachs result is stronger than the forward determinant part. More decisively, its specialization gives a diagonal interpolation for exactly the proposed inverse, with no additional spectral input or nonstandard inference; see claim_vs_prior_implication. The corresponding rooted cubic fact is the standard triangle coefficient applied to the graph and its vertex deletion (equivalently a closed-walk count). Thus the particular known-weight equivalence classes and local repair in this record are direct corollaries of an existing general result and elementary coefficient operations. This is a coverage judgment, not a claim that the earlier paper prints the bouquet theorem or that an inaccessible near match is identical.

## value

FAIL

Knowing which flux observables a spectrum can recover is a motivated problem, and the worked example illustrates it clearly. In this exact family, however, the proposed invariant and local fix reduce to the ordinary weighted cycle coefficient and evaluation at its known distinct poles. There is no further demonstrated non-routine result on, for example, unknown weights, near-coincident strengths or measurement sufficiency under noise. The correct specialization is useful exposition, but not an independently needed new mathematical result under the value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
