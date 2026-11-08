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

Run `python3 check_cuboid.py` with SymPy and NumPy installed. The checker evaluates cumulants and moment polynomials in exact rational arithmetic, reconstructs four boxes symbolically, confirms a two-moment collision with distinct third moment, checks both closed-form volume profiles, and samples 12,000 random positive profiles against their sharp analytic bounds. It separately draws 450,000 independent point pairs from each of three boxes to test the first three even moments against six empirical standard errors. Exact symbolic results passed; all stochastic comparisons passed with the recorded seed. The finite random tests are corroboration, not an infinite proof.

Expected output: `CUBOID_INVERSE_OK exact_cumulants=3 inverse_shapes=4 nonunique_pair=1 envelope_samples=12000 direct_sample_shapes=3 samples_each=450000`.

Analytical limits: the result applies to strictly positive rectangular edge lengths and the stated interior-uniform sampling model; it is not an estimator error bound. No independent audit has been performed.
