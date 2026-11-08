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

# Reproducibility
Run `python3 checks/strip_checker.py` with Python 3 standard library, from the package root. Actual replay: `ORDER_TWO_STRIP_CHECKS_PASS 404`. The test evaluates the matrix entries with independent Simpson quadrature, checks curvature, examines small- and large-strip asymptotics, and checks the complementary-tail identity. The proof uses the exact two-Hermite direct-integral reduction and the asymptotic determinant expansions stated in RESULT.md. Finite tests do not establish infinite-dimensional or uniform assertions, and no independent mathematical audit has been performed.
