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

# Checks and limits

1. Reindexed coordinates \((u,v_0,y)\) and \((x_0,U^*x,z)\) directly show two-sided unitary equivalence to a scalar plus triangular diagonal blocks.
2. Recomputed characteristic polynomial \(z^2-(2+t^2)z+1\) of the positive Gram matrix, giving reciprocal singular values.
3. Verified the scalar coupling crossover by solving \(F(c)=c^{-1}\), obtaining \(c=1/\sqrt2\), and showed the monotone branches meet at value \(2\).
4. Checked positivity-constrained lower and attainment at \(c_0=\max\{1,\mu\}\) and \(c_j=\mu\) for higher coordinates.
5. Executed standalone `CHECK.py` from this package with 7,752 exact-rational assertions passing; these are corroboration of finite identities, not a proof of an infinite-dimensional statement.
6. Examined the motivating 2026 preprint's main theorem and proof. Public-record and topical literature searches did not reveal an exact covering singular-value/condition-number result, but publication priority has not been independently certified.

The formulas do not apply without modification to nondiagonal couplings; no numerical or finite test establishes a full class theorem absent the direct analytical reduction.
