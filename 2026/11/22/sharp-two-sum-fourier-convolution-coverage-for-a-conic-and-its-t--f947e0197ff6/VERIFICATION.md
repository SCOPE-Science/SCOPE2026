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

# Verification details

The proof checks the exact quadratic-character signs of both conic and conic–tangent convolutions, handles the shared point by indicator inclusion-exclusion, and separates the one singular quartic fiber before applying the elliptic Hasse estimate. The finite-field algebra cases are \(q=3,5,7,9,11,13,17,19,25,27,49,81\), including nonprime orders. The `conic_tangent_checker.py` script constructs field arithmetic from monic irreducible polynomials and independently enumerates all ordered sums, character signs and the pointwise formula. It tests the complete pair-sum histograms, zero loci, per-fiber formulas and trace bounds.

The execution is reproducible using `python conic_tangent_checker.py` with Python 3 and SymPy. Finite checks do not verify the theorem for all prime powers; the all-order argument is mathematical, using the genus-one Hasse bound and an exhaustive small-field complement.

No independent mathematical audit, third-party verification or machine certification was performed.
