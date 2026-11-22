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

# Reproduction and limitations

The self-contained `verify.py` should be run as `python verify.py` alongside `requirements.txt` using Python 3 with NumPy, SciPy, SymPy and mpmath. The accompanying `verification_output.txt` contains stdout from an actual execution.

Checks include exact SymPy simplification of the logit-variable identity, stationary derivative, symmetry exclusion and low-correlation polynomial certificate; six independent two-dimensional Gaussian quadrant integral evaluations; 1,500 deterministic-random site comparisons; 599 correlation sweep checks; a high-precision scalar equation root and derived risk and information fractions. Exact identities and numerical quadrants are independent cross-checks of key formulas, with no claim that finite sweeps prove all-case optimality.

The full mathematical certificate for global optimality is the analytic chain in RESULT.md: the four-atom sign-field representation, signed derivative factorization, two-regime comparison, strictly monotonic one-dimensional root equation and endpoint exclusions. The proof assumes known Gaussian bridge covariance, two nonadaptive exact sign measurements, and squared-error Bayes loss. No independent mathematical audit or publication-priority certification has been performed.
