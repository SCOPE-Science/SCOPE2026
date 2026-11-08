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

The theorem is established by exact Walsh decomposition and a Vandermonde rank argument. No external or independent certification is asserted.

Run `python3 CHECK.py` with NumPy installed. It builds raw-sensor analysis matrices from the graph definition, not from the predicted rank, and checks every \(d\in\{2,3,4,5,6\}\), each face codimension, every band cutoff, and up to three observations. It separately compares the full two-snapshot Gram eigenvalues and optimal determinant formula in dimensions \(2\) through \(7\). The checker prints `CHECK_OK rank_cases= 405  two_time_spectrum_dimensions=6` if the tests pass.

The computation is finite and does not prove the general theorem. The infinite-parameter proof depends on elementary Walsh orthogonality, nonvanishing Vandermonde minors for distinct positive heat nodes, and differentiation of a closed determinant product. The reported tests use floating-point tolerance; the formula and proof are exact.
