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

# Reproducibility and verification
Run `python verify.py` using Python 3 and NumPy. The checker directly enumerates every isotropic vector and all pairwise values of the polar form for ten cases: both quadratic types over \(\mathbb F_2\) in dimensions four and six, over \(\mathbb F_3\) and \(\mathbb F_5\) in dimension four, and over \(\mathbb F_4\) in dimension four. It forms the unnormalized Fourier matrix, computes its Gram eigenvalues, and checks the complete predicted multiplicities. The output ends with `QUADRATIC_CONE_SELF_FOURIER_PASS 10_field_form_cases` when all checks succeed.

The general result is established by the independent symbolic counting argument in `RESULT.md`. Finite matrix diagonalization does not certify all fields or dimensions. Eigenvalue comparison uses a stated floating-point tolerance; no arithmetic Smith form or independent mathematical certification is claimed.
