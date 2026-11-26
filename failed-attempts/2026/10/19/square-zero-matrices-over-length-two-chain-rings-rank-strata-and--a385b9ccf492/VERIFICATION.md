---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For reduction rank a, the residue matrix has Jordan type (2ᵃ,1ᵇ), b=d−2a; each is conjugate to a standard 0–1 matrix whose square is zero over the ring. The basis change lifts because its determinant is a unit. Relative to a square-zero lift J, the term added to J² by adding πX is π(NX+XN); all terms quadratic in π vanish. Multiplication by the diagonal sign change on each size-two Jordan block identifies the anticommuting solutions with the commuting space, including characteristic two. The k[t]-homomorphism dimensions for pairs of Jordan blocks give 2a²+2ab+b². Independently, choosing an image, a kernel containing it and an isomorphism from the quotient to the image counts the reductions. Combining these two counts gives |GL_d(k)|/(PₐP_b). The normalized series separates over d=2a+b as two Euler series, including the empty d=0 convention. The reciprocal-product weights have summably bounded deficits from P∞⁻² along both ends of the rank interval, giving the stated total variation and total-count estimates. Independent exhaustive arithmetic over Z/4Z and the dual numbers over F₂ gave residue-rank counts [512,672,0,0] for d=3 in each ring.

## originality

FAIL

The central exact rank-stratum law and its all-ring invariance are already covered by the earlier indexed joint Smith census 6b8f1c0037a2, which explicitly gives the fixed-reduction-rank marginal. The generating function is the Euler identity applied to the factorized marginal. The two asymptotic conclusions are direct geometric-tail estimates on the same explicit weights, not an independently established new counting or distribution phenomenon beyond that prior formula. This is demonstrated prior coverage and direct implication, not a judgment based on unavailable literature.

## value

FAIL

The statistical interpretation is useful, but as a standalone new contribution this is a coarser census than the prior Smith result, with a routine Euler resummation and endpoint-tail bound on its explicit weights. The frozen record supplies no distinct invariant or nonroutine refinement beyond those consequences. The clean centralizer proof and finite replication are valid exposition but do not add a new result of independent research value here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
