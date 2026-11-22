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

The public `check.py` was executed with Python 3 and passed 7,799 exact assertions. It independently enumerated all even derangements for \(4\le n\le8\), counted every pair of off-diagonal assignment events, checked the stated parity-correct pair formulas, and verified the resulting covariance action on explicitly constructed zero-row/column matrices. The resulting normalized eigenvalues were:

- \(n=4\): symmetric \(4/3\), skew \(0\);
- \(n=5\): symmetric \(1/4\), skew \(5/12\);
- \(n=6\): symmetric \(18/65\), skew \(3/13\);
- \(n=7\): symmetric \(37/186\), skew \(63/310\);
- \(n=8\): symmetric \(416/2471\), skew \(176/1059\).

These numbers are eigenvalues of the **incidence covariance**, and the degree-one Walsh Gram values are four times as large. The size-uniform result is established by the proof, not by exhaustive enumeration. No independent audit has been performed.
