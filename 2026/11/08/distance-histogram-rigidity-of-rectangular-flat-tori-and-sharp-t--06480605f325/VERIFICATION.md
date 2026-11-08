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

# Reproducibility and evidence

Run `python torus_distance_verifier.py` after extracting that standalone file. Requires NumPy and mpmath in addition to the Python standard library. Successful execution on the packaged verifier returned:

```
VERIFY_OK exact_cumulants=3 exact_inverse_shapes=4 exact_two_moment_counterexample=1 complex_zero_samples=6 monte_carlo_pairs=120000
NEAREST_FOUND_ZERO=(1.43365931676195287935918 + 5.45705263632490130914145j)
POPULATION_MEAN_VARIANCE=[1.7241666666666668,1.109662777777778]
SAMPLED_MEAN_VARIANCE=[1.725818849219847,1.1053607731758703]
```

The rational tests establish the three cumulant constants and the displayed two-moment collision exactly. The complex numerical samples validate the integral differential identity at precision and locate examples of zeros, but **are not a certified exhaustive root census**. The proof of existence of a nonzero zero uses the zero-free finite-order Hadamard theorem, and the zero-peeling argument uses the infimum of all complex zero moduli, not a numerical approximation. Monte Carlo checks compare direct intrinsic torus distances with theoretical first and second cumulants; they establish no infinite theorem.

Not independently audited or externally certified. No claim about finite-sample numerical condition numbers or skew lattices.
