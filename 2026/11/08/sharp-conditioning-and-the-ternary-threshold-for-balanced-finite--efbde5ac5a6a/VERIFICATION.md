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

The standalone `check.py` uses exact pair arithmetic in the Eisenstein integer ring for root-of-unity phases of order three. It checks real Johnson-sector eigenvectors against original matrix multiplication for all selected balanced and one-extra-coordinate slice cases, totaling 2770 verified matrix rows (up to 252 by 252). It verifies the integer trinomial recurrence and squared spectral endpoints for every degree up to 499. Successful output: `TERNARY_CONSTANT_WEIGHT_SLICE_EXACT_PASS rows= 2770 k_up_to=499`.

Separate independent numerical reconstructions computed singular values of the original complex Fourier matrix for moduli 3, 4, 5, 6, and 8 and k=1,2,3, comparing the observed condition numbers with the claimed formulas; all 15 agreed to displayed eight-digit precision. Those exploratory tests were not packaged as a certificate. The analytic proof, not the tests, covers all field moduli and dimensions. No independent mathematical review has occurred.
