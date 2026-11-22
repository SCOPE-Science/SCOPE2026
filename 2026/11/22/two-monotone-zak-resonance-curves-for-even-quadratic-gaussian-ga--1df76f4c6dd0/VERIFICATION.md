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

# Verification and reproducibility

The real-quadratic Gabor claim follows analytically from the half-density Zak criterion, paired lattice symmetry, Poisson summation, the Jacobi theta product, a positive-coefficient expansion and a weighted-variance estimate. No infinite claim is inferred from a finite search or truncation.

Execute `python3 CHECK.py` with the Python standard library. The code independently recomputes Zak sums on the two critical fibers, compares two formulas for each theta quotient, tests the exact off-resonance fiber-energy identities, and checks monotonicity on a finite range. The checked run passed 1,011 assertions. Double precision and truncation cannot establish global positivity, uniqueness, or historical priority; the written proof carries those claims.

The two resonance curves are not asserted to exhaust every failure of the frame condition. No independent mathematical review has been performed.
