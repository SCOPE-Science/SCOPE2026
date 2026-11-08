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

# Verification scope

The proof reduces the entropy extrema to the sign of a single derivative. The expansion derivative is strictly decreasing. Compression relies on the explicit analytic identity

\[
3F''(y)^2-2F'(y)F'''(y)=\frac{e^y}{y^4}\{e^y(y^2-4y+6)-2y-6\}>0,
\]

where \(F(y)=(e^y-1)/y\) and the bracket has zero initial value and derivative and strictly positive second derivative for \(y>0\).

The standalone `verify.py` was executed with Python, SymPy and mpmath. It verified the symbolic identity and the bracket's second derivative, ten representative parameter-regime predictions, thirty high-precision derivative/finite-difference comparisons, sampled duration monotonicity, and four asymptotic critical-window coefficients. Successful finite checks cannot certify the infinite family; the analytic argument in `RESULT.md` supplies the proof.

Thermodynamic validity is limited to the harmonic expressions and their assumptions. The duration formula is underdamped only. Publication-priority comparison remains qualified where unindexed sources or supplementary derivations are concerned. No independent audit has been performed.
