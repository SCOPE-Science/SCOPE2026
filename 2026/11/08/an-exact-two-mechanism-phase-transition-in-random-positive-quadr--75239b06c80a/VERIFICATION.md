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

# Verification and scope

The analytic proof is in `RESULT.md`; computations below are corroborating checks only. To reproduce the finite checks with Python 3 standard library, run `python3 verify.py`. The checker independently tests the node-sign/extreme-product criterion against exact-rational Carathéodory representations, including closed-form Lagrange integration weights, over 46,440 small configurations. It then uses independent numerical integration to compare exact event-law integrals against the three-node closed form and four-node identity at multiple variance values, and compares selected large-sample ratios against both Laplace constants. Seeded Monte Carlo at three variance values serves only as a distributional smoke test.

The checker output on the actual packaged source was `VERIFY_OK 46440 exact-rational configuration checks; integral/moment/asymptotic/MC cross-checks passed`.

The proof's critical nonstandard steps are the exact vertical slice of the sampled moment curve, the disjoint split into extreme-span and nearest-gap events, the partial derivative of the extreme joint CDF, the mixed density of nearest sign-opposite nodes, and two nondegenerate Laplace expansions. None of these rests on the finite checks. No exhaustive search of all mathematical literature or independent audit is claimed.
