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

The attached `verify.py` can be run directly with Python and NumPy. Its completed execution checked the exact two-protocol rational identities and positive difference, independent birth-moment recursions, 240 direct Markov-resolvent comparisons for exponential residence times, and 80 constant-stiffness invariance comparisons. All tests passed. The analytic renewal-reward argument in `RESULT.md` is the proof for general holding-time laws; finite numerical comparisons do not prove this infinite-family statement.

The code independently reconstructs all witness rational coefficients from the two explicitly specified distributions, rather than importing a prior numerical log. The specified nonexponential residence laws have finite means and valid probability masses. The full stationary distributions need not be equal; the verified equality concerns only the specified second-order and energetic observables. Publication priority remains subject to independent bibliographic review.
