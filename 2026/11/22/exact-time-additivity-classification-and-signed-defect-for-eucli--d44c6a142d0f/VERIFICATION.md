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

The strictly convex coercive objective has a unique minimizer. Soft thresholding at p=1 and radial shrinkage at p=2 compose by threshold addition, including extinction. At p=∞ one can directly constrain the output to a cap λ: within [−λ,λ]^n the least-squares optimizer clips coordinates, and minimizing over λ≥0 gives sum_i(|x_i|−λ)_+=t until extinction at t=||x||_1. A second clipping removes the additional mass s, so its final cap solves the single clipping equation at s+t (or the output is zero). For finite p>1, the implicit equation z+h∇f(z)=x has a jointly smooth local solution around (0,u), with first two h-derivatives at zero −g and 2Hg. The expansion is valid also at the nearby first-step point. Composition contributes 3Hg in order h² compared with 4Hg for the step 2h. Direct differentiation at u gives (Hg)_1=(p−1)(n−1+2^p)^(2/p−3)(2^p−2^(2p−2)). The difference is the negative of this coefficient; it is nonzero except at p=2 and has the stated signs. The n=1 case correctly reduces to the absolute-value map for all p.

## originality

PASS

The supported distinct content is the complete classification across the canonical ℓ_p family and one common witness with an evaluated sign change. Credit the endpoint formulas, abstract flow theory, and the generic quadratic local resolvent calculation to existing evidence. The strongest distinct published catalogue overlap uses that same local calculation but its group-classification theorem is for a different penalty class and does not specialize to any finite 1<p<∞, p≠2 here.

## value

PASS

A complete answer for the basic ℓ_p scale distinguishes when one Euclidean proximal step really is a time semigroup step, a stronger condition than existence of the associated flow. One witness covers every excluded exponent, and the signed leading defect distinguishes the two sides of p=2. This is useful as a worked exact norm-family classification and diagnostic; the standalone Taylor formula and the positive endpoint shrinkages are not the value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
