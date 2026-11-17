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

The proof reconstructs Gaussian conjugation, Wiener-chaos singular values, and the Kalman Gramian. The graded Gramian limit is proved using orthogonal projections and its determinant positivity is established by polynomial independence. The trace-class criterion follows from the first-chaos singular values; the sharp rank bound is attained by a concrete family.

The self-contained `CHECK.py` (Python standard library only) verifies Cauchy determinant / factorial identities for chain lengths one through eight, including the degree-three case. An independent exact symbolic calculation for the degree-three chain gave \(\det G=1/1080\). A high-precision numerical check of the covariance determinant and singular-value product at three decreasing positive times agrees with the \(\(t^9\)\) law and its coefficient. Numerical checks are finite sanity checks, not an infinite-dimensional certificate. Only fixed positive Schatten exponent, fixed finite state dimension asymptotics are asserted.
