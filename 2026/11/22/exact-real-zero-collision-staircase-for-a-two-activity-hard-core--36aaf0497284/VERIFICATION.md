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

# Verification and reproducibility

`verify_wheel_zeros.py` is standalone Python 3, requiring the public package `sympy` and Python's standard library. Execute `python verify_wheel_zeros.py` from a directory containing this file. It checks the cycle coefficient formula against a direct enumeration of all binary independent configurations for all \(n=4,\ldots,14\); it then uses exact-rational Sturm root counts in each strict fugacity phase for each such \(n\), compares critical values against the cosine formula, and checks exactly the double-root gcd at \((n,t)=(4,1),(5,1/4),(7,1/27)\). Expected final line: `WHEEL_ZERO_CENSUS_CHECKS_PASSED`.

The analysis proving all \(n\ge4\) is analytic and given in `RESULT.md`: transfer trace, complete derivative zero list, sign-alternating extrema, continuity and degree, and Taylor curvature. Floating-point critical values are used only to choose rational probe points and compare formula evaluations at finite \(n\); exact Sturm counts and exact duplicate-root gcds do not rely on floating-point root solvers. The finite checker is not an exhaustive proof for all sizes, and the novelty comparison remains contingent on examined literature. No independent external audit or formal proof-system certification was performed.
