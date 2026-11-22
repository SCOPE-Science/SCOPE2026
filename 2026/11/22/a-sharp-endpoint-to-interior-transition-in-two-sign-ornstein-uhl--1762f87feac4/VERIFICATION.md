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

The analytic proof in `RESULT.md` establishes the exact risk, fixed-separation symmetrization, strict separation-score unimodality, critical rate and asymptotic; these are mathematical arguments with universal quantifiers rather than finite experiments. The reproducible standalone script `verify_ou_sign.py` checks the exact crucial hyperbolic identity in symbolic algebra, the arcsine sign covariance at four parameter choices, direct covariance integrals, 13 correlation rates, random asymmetric placements, the one-dimensional derivative sign, and high-correlation asymptotics. Execution succeeded with 4,967 assertions and printed the displayed critical parameter and several optimum examples.

Run `python -m pip install -r requirements.txt` then `python verify_ou_sign.py`. `mpmath` supplies high-precision quadrature/root tests; `sympy` supplies the exact rational-expression identity. Verification does not check arbitrary untested numerical inputs exhaustively; that coverage comes from the proof. No independent third-party mathematical audit is asserted.
