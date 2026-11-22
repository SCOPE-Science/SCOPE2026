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

The theorem is proved analytically by the radial-cone parametrization, the strict log-derivative separation, endpoint integration, and the scale equation. These prove all exponents \(q>0\), all positive aspect ratios, the exact boundary behavior, and every allowed inverse fiber. There is no extrapolation from finite numerical experiments.

Run `python3 verify.py` using Python's standard library only. The program compares cone-mass and independent angular-preimage integrations, checks exact rational identities for \(q=4\) and the normalization at \(q=2\), checks sample derivative-sign consequences, tests reciprocal symmetry and inverse reconstruction, checks selected strict existence and nonexistence boundaries, tests explicit off-center equal-opposite-mass witnesses for three exponents below one, and checks the positive derivative underlying symmetry rigidity at representative indices above one. The saved program executed with output `PASS 228 cone/angular/exact/monotonic/inverse/symmetry checks`.

The angular and cone integrals in the program are numerically approximated by composite Simpson quadrature; these are independent formulas but are not rigorously error-certified. Exact rational algebra tests are exact. The program does not certify all real parameters or establish priority in historical literature. The exact-support reduction and the symmetry rigidity are analytic statements for arbitrary convex bodies with the stipulated four-atom data. The off-center solution fiber below \(q=1\) is not claimed to be completely classified; known symmetric existence and uniqueness theorems for \(0<q<2\) are credited.
