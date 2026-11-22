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

The proof uses exact eigenvalue decomposition, strict convexity, and two one-sided derivatives. Execute `python3 verify_k2q_gain.py` using Python's standard library to check finite representative cases and the derivative identities. At package preparation the checker passed 4,599 assertions, including rational matrix inversions and independent scalar budget optimizations.

Finite computation does not establish the all-integer theorem or independent certification. The proof derives those from the exact universal identities and the monotone level-set function \((t+2)^3/t\).
