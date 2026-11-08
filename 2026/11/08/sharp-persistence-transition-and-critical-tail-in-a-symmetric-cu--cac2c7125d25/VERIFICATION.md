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

The algebraic proof in `RESULT.md` is the certification basis within this document. The included `check.py` uses only the standard Python library and verifies the endpoint identities, fixed points and monotonicity across representative real parameter samples. At the critical value it iterates the exact inverse-branch recurrence through 10,000 steps and compares the scaled tail with its analytic limit. It is not a finite proof of statements for all real parameters or infinitely many iterates.

At the critical value, the exact symbolic identity is \(c-B(c-v)=v+3\sqrt3v^2-6v^3\). The relation \(y_n-y_{n-1}=3\sqrt3-33/y_n+O(y_n^{-2})\) establishes the asymptotic logarithmic term. This verification is not independent mathematical auditing.
