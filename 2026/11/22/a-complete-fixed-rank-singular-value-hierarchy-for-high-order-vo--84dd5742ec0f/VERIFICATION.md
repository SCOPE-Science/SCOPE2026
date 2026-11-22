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

## Finite diagnostics and analytical evidence

The analytic proof is the ordered-exterior-power determinant convergence, its tail domination and the exact Laguerre Gram determinant. The standalone `check_spectrum.py` independently checks eight exact-rational moment determinants and verifies the expected scaling for the first four singular values of three finite Nyström matrices. It also checks the squared Hilbert–Schmidt mass against its elementary exact integral.

Run `python check_spectrum.py` in a Python 3 environment with SymPy, NumPy and SciPy. Successful output consists of `EXACT_GRAM_DETERMINANTS_OK` and `FINITE_NYSTROM_DIAGNOSTICS_OK`. These finite diagnostics do not certify the infinite-dimensional limits, the uniform determinant expansion, or novelty. Independent audit is not yet performed.
