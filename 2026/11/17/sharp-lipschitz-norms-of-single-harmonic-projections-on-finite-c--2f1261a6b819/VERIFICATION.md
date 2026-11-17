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
# Reproducible finite diagnostics

The standalone `verify.py` uses the standard Python library, and was run under Python 3. It separately constructs all extreme points of the centered increment cube \(\{u\in[-1,1]^n:\sum u_j=0\}\) for \(3\le n\le16\), evaluates the real Fourier projection kernel on those points and compares the resulting sharp finite-dimensional value with the stated formula, for all \(63\) admissible nonconstant harmonic pairs. For odd \(n\), these vertices have one zero and balanced \(\pm1\) entries; for even \(n\), they have equal numbers of \(\pm1\). The program enumerates them rather than assuming a cosine-median formula to calculate the reference maxima.

It also independently checks the six-cycle \(4/3\) value with exact rational arithmetic; checks the cosine-median closed form over \(298\) effective periods; checks \(3540\) full-cycle frequency cases against gcd-reduced formulas; and tests the second-order asymptotic coefficients separately. The executed final diagnostic was `ALL_LIPSCHITZ_CYCLE_FOURIER_CHECKS_PASSED`.

These computations do **not** prove all-parameter theorems or publication priority. Universality follows instead from the displayed zero-sum duality, exact finite trigonometric sums and strict calculus inequalities in RESULT.md. No independent external mathematical audit has been performed.
