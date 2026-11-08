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

# Reproduction and scope

Run `python3 verify.py` with Python 3 and its standard library. Actual completed output:

```
VERIFY_OK rational_grid_equalities=65 sharp_gap_cases=10 deformed_inverse_spectra=27
```

The code enumerates binary inverse branches of the original tent map with exact rational arithmetic for cutoffs \(2\) through \(11\), compares them with the two-grid formula, and checks the largest gap of all periodic points through each cutoff after adding the turning point and endpoints. It also checks an exact triangular perturbation of slope error \(1/3\), its exact peak amplitude and the equality of its values at all observed periodic points. For cutoffs \(2\) through \(7\), it numerically recovers periodic points from the deformed inverse branches independently and matches them to the reference rational grids. The finite numerical inverse-branch comparisons use a tolerance of \(2\times10^{-12}\).

These are finite tests, not an exhaustive proof over all \(N\), all \(\delta\), or all admissible maps. The infinite theorem is established by the symbolic-grid and Lipschitz-extension arguments in `RESULT.md`. No external independent audit or human certification has been performed.
