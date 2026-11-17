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

Run `python3 verify.py` with Python 3 standard library. The included checker performs exact Fraction arithmetic on the weighted eight-snake flow for every odd-order rectangle with dimensions from 3 through 13, checks the closed edge coefficients and conservation identities, and verifies even-order grid Hamiltonian cycles. It also exhaustively evaluates every nontrivial binary cut in 2×2, 2×3, 2×4, 3×3, 3×4, 3×5 and 4×4 grids, plus four larger odd-grid rational certificates.

Successful local execution produced:

```
RECTANGULAR_ALL_PARITY_FLOW_CERTIFICATES_PASS 144
EXHAUSTIVE_ALL_NONTRIVIAL_CUTS_SMALL_GRIDS_PASS 7
LARGE_ODD_GRID_EXACT_RATIONAL_FLUX_CERTIFICATES_PASS 4
ALL_CHECKERBOARD_VARIATION_CHECKS_PASS
```

The all-size theorem depends on the symbolic nonnegative flow construction, boundary/interior inequalities and a corner equality witness in `RESULT.md`. Finite diagnostics alone are not evidence for infinitely many grids. No independent mathematical audit or external certification has been performed.
