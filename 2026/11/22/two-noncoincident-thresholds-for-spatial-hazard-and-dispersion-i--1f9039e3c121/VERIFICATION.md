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

# Reproducible verification

Invoke `python checker.py` with NumPy, SymPy and SciPy installed. The script checks the normalized stationary density, reset-source Laplace identities, boundary injection, exact mean and variance, spatial-hazard derivative, transition-at-resonance, sign-variation uniqueness and numerical roots. It then independently simulates 120000 pre-alarm observations at each of four capacity rates in dimensionless units and compares the first two stationary moments with analytic predictions; 3000 initial observations are discarded. Exact algebra, positivity and monotonicity arguments in RESULT.md, not finite simulations, establish statements about all positive parameters and positions.

The proof and code do not establish an analogous claim for different boundary rules, other capacity distributions, or nonstationary dynamics. Independent validation has not been performed.
