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

The proof uses the established symbolic bijection for nontrivial iterate fixed points and derives the exact signed branch-matrix product for all \(n\ge1\). No finite enumeration is used to infer a universal result.

Executed `python check_2d_twisted.py` against the packaged standalone file. The script solves and checks all \(2^n-1\) nontrivial symbolic periodic-point equations for each \(1\le n\le11\) using exact fractions, verifies the correct branch at every iterate, checks derivative matrices, and verifies every conditional binomial cell. The terminal output is `TWISTED_BAKER_BINOMIAL_ANISOTROPY_CHECK_OK`.

The distributional limit uses the standard central limit theorem for independent symmetric signs and a conditioning correction of size \(2^{-(n-1)}\). It is a weak limit only. Its domain is fixed points of iterates, not points of exact least period.
