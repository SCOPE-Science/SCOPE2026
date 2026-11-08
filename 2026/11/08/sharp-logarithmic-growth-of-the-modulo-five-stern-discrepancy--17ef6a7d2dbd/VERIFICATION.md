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

The standalone `verify_stern5_discrepancy.py` uses exact integers and standard-library Python. It verifies all twenty-four entries of the vector equalities \(S_5=S_1\), \(A_{28}=A_{16}-4\mathbf1\), and \(B_{28}=B_{16}+4\mathbf1\). It also checks every prefix via direct Stern recurrence for lengths up to \(2^{18}\), tests the dynamic-programming reconstruction of witnesses, and independently enumerates the two large example prefixes of lengths \(2190712\) and \(8693112\).

Those are the only machine-dependent premises. The unrestricted implication is a mathematical induction from the exact vector recurrences and does not assert that any finite experiment alone proves an infinite claim. This is not an independent mathematical audit.
