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

# Reproduction record

The included `verify_profile.py` was executed in a Python 3 environment with SymPy, NumPy and SciPy. It independently counts all 35 generator determinant triples (including six zero cases), proves the two rational expressions and their differentiated factorizations by exact polynomial identities, verifies both Descartes transformations and rational root brackets, checks endpoint and junction normalizations, tests the positive Bernstein coefficients for the entire second regime, and compares five independently constructed signed-sum convex-hull volumes with the derived zonotope formula. The output was:

```
EXACT_ALGEBRA_AND_NUMERIC_HULL_PASS
DESCARTES_CERTIFIED_UNIQUE_CRITICAL_POINTS Counter({(2, 1): 12, (1, 2): 12, (1, 0): 6, (0, 4): 4, (3, 1): 1})
```

Reproduce with `python3 verify_profile.py`; SymPy is required, while NumPy and SciPy enable the additional geometric hull check. The rational-identity assertions plus the paper proof, not numerical samples alone, certify the all-real-parameter claims within the fixed family. The proof uses classical Cauchy and zonotope-volume identities and Descartes' rule of signs. The code is not an independent mathematical audit.

Historical originality remains provisional: the full 2011 class-bound work and the extensive 2026 polyhedral-brightness manuscript could not both be inspected in full, although the known regular-member result and closest full published mathematical statements were compared. No claim is made beyond this three-dimensional one-parameter family.
