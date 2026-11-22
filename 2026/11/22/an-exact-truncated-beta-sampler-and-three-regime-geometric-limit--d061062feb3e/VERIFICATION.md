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

# Verification record

The mathematical proof is in `RESULT.md`, including exact product-fiber disintegration, beta-binomial reduction, the second independently defined sign-cell sampler and all three limit proofs. Reproduce the optional finite verification by running `python verification.py` with Python 3 and no third-party packages. It checks 361 parameter pairs for three distinct exact volume formulae, 1,083 additional moment bounds, and 140,000 valid random samples. The program printed `PASS: 361 exact volume equalities, 1083 exact moment bounds, 140000 valid sampled points` on the reviewed package.

The source literature comparison uses the 2023 pointed-order-polytope triangulation and the earlier 2021 introduction as primary references, plus the 2026 two-rank signed-chain *different-body* result. The current claim is not a general volume theorem for all pointed posets, and an unindexed stronger paper remains a priority risk. Finite checks do not validate all parameters or asymptotic sequences; those statements follow from the written analytic proof. No independent mathematical review has been performed.
