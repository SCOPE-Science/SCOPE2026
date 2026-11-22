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
# Mathematical verification

Run `python verify.py` with the `sympy` and `mpmath` packages. The script derives the displayed \(\beta^2\) and \(\beta^3\) coefficients with symbolic integration; verifies the exact critical threshold \(9/2\), derivative \(-9/100\), cubic coefficient \(-1458/1595\), and boundary slope \(-3240/319\); and checks both conditional-derivative identities. Separate 70-digit quadratures evaluate the exact two directional functionals at positive parameters and numerically locate two small-\(\beta\) equality points.

The numerical points are illustrative only. The uniform local Taylor estimate, all-exponent sign statements for fixed noncritical \(\alpha\), and local existence/uniqueness follow from the analytic proof in RESULT.md, not numerical enumeration. The proof does not establish a global phase diagram across all admissible parameters. No independent mathematical audit has yet been performed.
