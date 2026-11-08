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

# Verification and scope

The analytic argument uses an exact least-squares reduction, two independent elementary limit theorems (a Gram law of large numbers and four-coordinate CLT), and a Gaussian cone calculation. The limiting discriminant has a smooth density away from a zero-measure polynomial surface, so its strict sign is stable in distribution. The large-\(t\) claim concerns the fixed limiting profile, not relative convergence in every joint growing-gap scaling.

The accompanying `check_collisions.py` passed as `VERIFY_OK` with Python 3, NumPy and SciPy. It exercises: QR whitening similarity and the projected block identity; exact symmetric positive-definiteness and four-dimensional embedding witnesses; ambient-three rank-one spectral reality; the derived one-dimensional integral against simulations of five shifted real Ginibre laws (350,000 draws each); finite-entry Gaussian and Rademacher sketch comparisons for dimensions \(s=48,128,384\) at two scaled gaps; and large-\(t\) prefactor sanity checks. Tests are random with a fixed seed and tolerance specified in the script.

Finite samples establish neither exact infinite-dimensional probabilities nor the universal iid-entry theorem. The proof, not the checker, supports those conclusions. No finite-precision guarantees, statements about structured sketches, or general full-iteration eigensolver convergence are asserted. No independent mathematical audit has been performed.
