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
# Verification notes

Run `python3 verify.py` using Python 3 standard library. All certified sign assertions are comparisons of exact `fractions.Fraction` values and rigorously bounded Taylor remainders; the printed decimal numbers do not participate in assertions. For \(a=9/16\), \(b=4/5\), \(\lambda=2\), the checker constructs enclosures for the two weight numerators and positive determinant, then verifies they satisfy \(N_{\mathrm{outer}}<-1/100\), \(N_{\mathrm{inner}}>1/100\), and \(\Delta>1/100\). Bound \(|e^{-z}-\sum_{j=0}^{80}(-z)^j/j!|\le z^{81}/81!\) follows from the Lagrange remainder for nonnegative \(z\); integrating the pointwise bound over the uniform target gives the mass remainder.

The finite rational computation proves sign at this one shape only. Analytic small/large-shape limits and continuity supply the all-shape reentrance conclusion and the open-set extension. A count of exactly two zero crossings is not established. No external independent audit has been performed.
