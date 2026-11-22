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

The all-parameter proof is analytic. The original generating function is normalized by direct substitution at \(z=1\), and the logarithmic coefficients are explicitly summable. Sufficiency is established for all integer jump sizes and all thinning probabilities by comparing analytic derivatives over the whole interval; necessity uses the sign of the single-jump logarithmic coefficient for a thinning probability sufficiently close to one. No finite experiment is substituted for the quantifiers.

To check the arithmetic with standard Python, run `python3 check.py` from this package. The script uses `fractions.Fraction` and exact algebra; it checks the boundary \(A(1/4)=125/81\), the equality of the first two canonical coefficients there, positive innovation coefficients over representative cases, and a negative first coefficient outside the allowed region. The rational WNBL overlap witness was also independently calculated from the same closed PGF.

This is self-review only; independent verification has not been performed.
