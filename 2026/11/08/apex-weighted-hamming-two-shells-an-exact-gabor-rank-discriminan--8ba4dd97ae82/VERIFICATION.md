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
# Verification notes

Run `python3 verify.py` with Python 3 and NumPy installed. The program independently constructs all \(N^2\) ambiguity coefficients using Gaussian-integer pairs before comparing their integer squared magnitudes against the theorem. Its complete exact checks cover dimensions 4 through 7 and seven rational apex parameters for each dimension, including zero, real, pure-imaginary, integral complex, half-integral complex, and large generic values. It additionally constructs the actual 256 projectors in dimension 4 and compares all 256 Gram eigenvalues for three parameters, thereby testing the precise singular-value normalization. Its success marker is `APEX_WEIGHT_TWO_HAMMING_GABOR_EXACT_CHECKS_PASS`.

The direct Gram diagonalization uses floating-point linear algebra with tolerance, but all other ambiguity calculations, multiplicities, and rank counts use exact integer arithmetic. The infinite-dimensional-parameter conclusions follow from the proof, not finite enumeration. No external mathematical verification was undertaken, and no claim of formal or independent certification is made.
