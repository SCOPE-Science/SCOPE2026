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

# Evidence and limits

The proof is in `RESULT.md`. Its nonstandard step is the exact stabilization of Clebsch–Gordan coefficient sums when the resulting index exceeds the mask degree minus one, with the one potential boundary summand having zero weight. This yields the affine tail, from which finite positivity, invertibility and precise cone geometry follow. Strictness is justified using the impossibility that a nonzero finite atomic measure on \(SU(2)\) has only finitely many nonzero matrix Fourier coefficients. Universality is the standard all-positive-coefficient condition for continuous central invariant kernels on compact groups.

`su2_poisson_checker.py` performs 3200 exact rational tests and finite algebraic comparisons across several distinct radii and degrees. The tests are supplementary evidence, not exhaustive verification of the infinite statements. The public motivating manuscripts and comparison statements are listed in `RESULT.md` and `REVIEW.md`. An earlier quadratic specialization is not claimed as new, and there may be unlocated equivalent statements under other terminology. Independent mathematical auditing has not occurred.
