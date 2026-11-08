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

# Reproducibility and scientific limits

The formal argument is presented in `RESULT.md`. Three independent computational checks accompany it: `check_field.py` computes complete field Fourier transforms at field sizes \(2\) and \(3\); `check_cyclic.py` eliminates a matrix row and tests Fourier support over \(\mathbb Z/9\mathbb Z\); `check_split.py` makes the corresponding test over \(\mathbb F_3[t]/(t^2)\). Each runs with Python 3 and NumPy. The cyclic and split tests examine six-dimensional slices of the full frequency space, not every frequency of the full twenty-dimensional additive group.

Previously executed output included `ALL_DETERMINANT_CHAIN_CHECKS_OK`, `SPLIT_CHAIN_EXACT_SUPPORT_CHECKS_OK`, and field maximum FFT errors smaller than \(3\cdot10^{-12}\). These floating numerical checks are not exact certificates; the universal claim is supported by the symbolic proof. No independent audit has been undertaken.
