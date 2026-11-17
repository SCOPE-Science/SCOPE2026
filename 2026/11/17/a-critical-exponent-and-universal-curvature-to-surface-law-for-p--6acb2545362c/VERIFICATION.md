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

The exact-rational, standard-library `CHECK.py` reconstructs the vertices and inverts the edge matrix independently of the stated gradient formula. It verifies all barycentric-gradient inner products and every complementary-minor identity needed for ridge measures for 60 positive integer-weight examples in dimensions 2 through 6 (660 ridge instances). Its separate Euclidean Steiner checks reproduce the three-dimensional equal-leg result of Gao and Vitale and the two-dimensional normalization. Asymptotic evaluations at dimensions 100, 1,000, and 10,000 illustrate but do not establish the stated limits.

Reproduce with `python3 CHECK.py` from this package. All proofs are mathematical, not claims of infinite computational certification. No independent mathematical audit has been performed.
