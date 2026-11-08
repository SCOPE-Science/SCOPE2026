---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification notes

The result has an analytic proof. The exact lens-volume identity is established by slicing and an incomplete-beta substitution; Brunn--Minkowski strictness and endpoint derivative estimates prove one crossing; elementary integral bounds show strict improvement over the earlier threshold; uniform Laplace/Stirling expansions give the finite-dimensional constants. These methods establish claims for all integer dimensions at least two and do not rely on exhaustive finite enumeration.

The companion `verify.py` checks the incomplete-beta expression, numerical root consistency and sign changes, strict improvement in twelve selected dimensions, the exact planar values, and asymptotic estimates in four larger sample dimensions. The script requires Python 3, SciPy, and their standard dependencies. It is a supplementary reproducibility check, not an independent mathematical audit. It makes no numerical claim for untested dimensions.

The universal best coefficient among *all* convex body pairs is not determined below the existing simplex-optimality range. The threshold here compares only Euclidean balls with oppositely oriented simplices, and the asymptotic expansion treats dimension tending to infinity. In particular a tied ball and simplex at the two-family threshold need not be globally optimal. Historical novelty may depend on older literature on lens covariograms and convolution bodies.
