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
# Reproducibility

The exact proof is in `RESULT.md`. The accompanying `check_two_line_conditioning.py` independently constructs full complex Fourier matrices over explicitly implemented prime and extension fields. It computes singular values using NumPy, checks the predicted complete squared-singular-value lists and condition numbers of each invertible two-line restriction, checks every predicted geometric multiplicity, and compares arithmetic nullity for singular restrictions. It checks all unordered pairs of projective lines for field orders \(2,3,4,5,7,8,9,11,13,16,17\), for 589 complete matrices in all.

To rerun, install Python 3 and the package in `requirements.txt`, then execute `python check_two_line_conditioning.py`. Output from the tested run is in `check_output.txt`. These checks are finite corroboration; they do not prove statements for arbitrary prime powers. No source files other than those embedded in this package are needed to execute the checker.

Analytic proof boundaries: the argument relies on finite-field Gauss-sum orthogonality, the exact constant-character matrix, and the complete classification of isotropic projective directions. It does not address translated or rectangular sampling masks. Historical priority has not been independently verified.
