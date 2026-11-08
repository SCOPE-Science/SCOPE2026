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

The analytic proof controls both the uniqueness of the hazard peak and the uniform remainders. The standalone executable check is `python3 verify.py`, a Python 3 standard-library-only test. Its run produced `VERIFY_OK assertions= 5910`.

It checks exact identities for the \(a=2\) slice using rational arithmetic, and evaluates the critical-window coefficients for \(b=1,2,3,5\) and \(\varepsilon=10^{-2},10^{-3},10^{-4}\) using a finite-binomial incomplete-beta representation. The code checks a finite sample, not the all-parameter result or the stated asymptotic error in the limit.

Analytic dependencies: ordinary calculus, the beta-function derivative identity, and the sign of the derivative of the negative logarithmic density slope. No external software or proof assistant is required for the statement.
