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

`check.py` is a standalone Python program requiring Python 3, NumPy, SciPy, SymPy and mpmath. Run `python check.py` from a directory containing the file. On successful replay it prints `ALL_CHECKS_PASSED` after the following checks:

- 18 exact-rational independent-cut enumerations against the hub-factorized partition polynomial, with up to thirteen spins.
- 18 numeric complex root-locus checks and exact phase-equation root comparisons across three positive interaction values and six petal counts. High-degree, weakly interacting polynomial root solvers are ill-conditioned; the separate analytic argument does not depend on their accuracy.
- Symbolic differentiation of the limiting density with respect to cosine, and five algebraic interior-peak checks.
- Monotonicity of the physical star comparator at sampled arguments.
- Positive normalized limiting-density integration at four couplings and leading-angle asymptotics for twelve large-size tests.

The infinite-size density and root simplicity are independently established by the explicit analytic phase proof in `RESULT.md`, not by exhaustive finite enumeration. The tests do not determine historical priority or provide independent external audit.
