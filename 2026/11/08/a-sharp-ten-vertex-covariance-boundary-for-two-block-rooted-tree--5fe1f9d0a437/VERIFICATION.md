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

The formula is obtained by conditioning on the one uniformly selected parent. The sharp depth inequalities and equality conditions establish the theorem for arbitrary finite rooted trees, and the cubic maximum establishes the asymptotic assertion. An independently expressed exact rational enumeration of all parent positions, rather than a mere repetition of the symbolic formula, was executed for all 3,046 unordered rooted-tree shapes through eleven vertices (2 to 11). Known enumerated shape counts were 1, 2, 4, 9, 20, 48, 115, 286, 719, and 1842 for orders two through eleven. The test also inspected explicit broom shapes for orders 10 through 100. The last test report stated approximately 9,320 exact assertions and `PASS`. These tests are finite evidence only.

To reproduce, use Python 3 with no third-party packages and run `python checker.py`. The test constructs each unordered rooted tree recursively, evaluates statistics from the concrete shape, independently enumerates each possible attachment parent, and compares the resulting exact covariance with the theoretical bound. It also checks equality cases and the threshold values. No external or independent audit was performed.
