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

# Reproduction and limits

Run `python check.py` from the directory containing this file. The program uses Python 3 and `sympy`, and reports 226 symbolic/rational/finite-transfer checks. It verifies the exact nested conditional-moment algebra at the level of symbolic expressions, zero-lag fourth cumulant, multiple positive rational parameter triples, and nonvanishing short-time transfer coefficients plus positive Laplace resolvent entries for several independent finite chains. The general proofs are written in `RESULT.md` and do not rely on numerical extrapolation.

Critical logical checks: the wall's generator must reset to zero; the fourth cumulant subtracts all three Wick pairings; the OU control must have covariance \((2D/r)e^{-r|t-s|}\); each finite chain must have positive mass, springs, friction and reset rates; all Gaussian bath noise must be independent of clocks and walls; and strictly positive kurtosis must follow from a nonconstant conditional variance, not from the sign of an integral with possibly oscillatory velocity kernels.

These checks are not independent scientific validation, and they do not test thermodynamic size scaling or priority against all unpublished literature.
