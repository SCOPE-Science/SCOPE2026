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

# Reproducibility notes

The standalone `verify.py` has no mandatory third-party dependencies. Run `python verify.py` to enumerate the \(2^{m-1}\) explicit incenter vertices and \(\binom{m+2}{2}\) vertices of the zero-supply original polytope for \(1\le m\le12\), validate all normalized center-margin inequalities in exact integer form, and integrate the uniform parking polytope using exact rational polynomial antiderivatives up to dimension twelve. Successful replay prints `TWO_ROW_INCENTER_EXACT_PASS`.

With NumPy and SciPy installed, `python verify.py --lp` also reconstructs the original weighted halfspaces and solves 36 independent maximum-radius linear programs (six real parameter values at each \(1\le m\le6\)); successful replay prints `WEIGHTED_TWO_ROW_LP_PASS cases=36`.

The finite checks do not establish the theorem for arbitrary dimension or arbitrary real parameters. Those follow from the explicit normal-length calculations, two sharp telescoping margin bounds, equality-case classification, and the cited classical parking-function volume formula in `RESULT.md`. No independent mathematical review or external certification has been performed.
