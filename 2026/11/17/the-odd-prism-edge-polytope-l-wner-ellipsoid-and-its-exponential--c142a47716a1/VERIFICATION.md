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

Execute `python3 verify_odd_prism.py` with NumPy and SciPy. The checker uses direct \(2m\)-coordinate edge-incidence matrices, an independently computed orthonormal affine tangent basis, and both SVD and numerical optimization; it verifies determinant, eigenvalue and all-contact conditions for odd rim orders \(3,5,7,9,11,13,15,17,19\).

Observed checker output ends with `ODD_PRISM_LOEWNER_PASS nine_orders=3..19 determinant_spectrum_contacts=PASS`; its largest contact error in the checked range is \(7.11	imes10^{-14}\). Numerical agreements do not establish statements for all odd rim orders; the analytic proof of strict concavity, determinant products and contact decomposition is in RESULT.md.

The supported validation is a self-review only, not an independent audit.
