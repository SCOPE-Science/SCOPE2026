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

Run `python check_exact.py` with SymPy and `python check_numeric.py` with NumPy in the same folder. Both are standalone with no other required local artifacts.

The exact script reconstructs the seven cubic harmonics and 49 entries of the region/full-sphere Gram matrices by gamma moments, verifies normalization and characteristic-factor identities, and checks the alternating equality vector. Actual execution: `EXACT_OCTANT_CUBIC_PASS 7 harmonic modes; 49 Gram entries; 5 eigenvalues`.

The separately implemented numerical script integrates using 4096 spherical-coordinate quadrature nodes, without invoking the exact monomial-moment formula. Actual execution: `NUMERIC_OCTANT_CUBIC_PASS nodes= 4096 max_eigen_error= 4.3021142204224816e-16`.

The exact proof in RESULT.md supplies the infinite-precision statement. Quadrature corroborates but cannot prove the closed-form spectrum. No external mathematical validation has been undertaken.
