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

Run `python checker.py` with a standard SymPy installation. The script compares two independent forms of the model generating function (direct Poisson integration and the exponential/gamma mixture); exactly normalizes the parent mixing density; algebraically verifies the mixture weights, the quartic root parameter, and the threshold polynomial; and computes rational logarithmic-coefficient diagnostics. At \(\lambda=1\), the coefficient \(5\nu_5=-3836474651/141985700000\) is negative. The verified first 24 coefficients for rates \(1/10\) and \(1/2\) are positive, but finite tests are neither sufficient nor necessary for the all-index conclusion.

The decisive infinite proof is analytic: the numerator root locations determine strict positivity of every canonical jump coefficient on one side and an infinite negative subsequence on the other, with a separate equality-boundary argument. The numerical critical root is merely an approximation to the unique positive solution of the exact polynomial equality. All scientific assumptions and restrictions are in RESULT.md. No independent audit has been performed.
