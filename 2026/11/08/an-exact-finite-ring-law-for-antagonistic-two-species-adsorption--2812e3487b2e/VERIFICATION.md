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

# Reproduction and proof checkpoints

Execute `python verify_ab_cycle.py` with Python 3 and the standard library. No downloads or external packages are needed. The checker obtains independent cycle expectations from exact finite-state continuous-time transition recursions, including all allowed species/site choices; it separately computes same- and opposite-boundary segment expectations, the analytic first-arrival recurrence, the factorial difference, and the generating-function coefficients. Every comparison uses exact rational arithmetic.

Latest execution: 324 exact comparisons passed. The direct exhaustive finite-state calculation covers cycle lengths \(3\) through \(11\), with \(16,239\) reachable configurations in the largest case, and compares endpoint conditions for segment lengths \(1\) through \(9\). Analytical identities are checked to segment length \(80\), and the strict finite-size increment is checked through ring length \(59\).

The all-size statement is proved through an exact first-success conditioning recurrence and its generating-function solution, **not** by extrapolating finite computations. The infinite-line identification additionally uses independent local minima of first proposal times as permanent shielding anchors; finite enumeration does not establish that part. The full distribution of terminal vacancies and unequal-rate dynamics are not checked or claimed.
