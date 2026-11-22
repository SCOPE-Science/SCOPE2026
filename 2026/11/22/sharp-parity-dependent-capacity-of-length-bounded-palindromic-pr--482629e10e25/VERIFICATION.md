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

# Verification

The exact maximal-size assertion is supported by a finite-poset injection, a palindromic extension/period equivalence, and an inclusion–exclusion bijection with equality-components in a finite graph. The asymptotic follows from a geometric palindrome count and a union bound on short-period palindromes. This proof is independent of any finite computation.

Run `python3 verify_direct.py` and `python3 verify_period.py` with a standard Python 3 interpreter. The first program builds the actual finite palindrome-prefix forest and recursively checks its maximum-antichain cardinality against its leaf count in 28 explicit cases. The second separately computes the disjoint-set graph inclusion–exclusion and tests it against direct short-period enumeration for every length through 14 (binary), 10 (ternary), and 8 (quaternary). Each finished without assertion failure.

No exhaustive computation is asserted outside those finite ranges. The two programs use no third-party dependencies and no external files. Independent audit: not performed.
