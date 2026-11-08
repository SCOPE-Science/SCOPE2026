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

For the declared Fock normalization, the independent symbolic checker `check_spectrogram.py` differentiates the real log-intensity and verifies the diagonal Hessian and quartic threshold expansion. It brackets positive solutions for four representative separations and confirms the stated Hessian signs. Execute with Python 3 plus SymPy and SciPy:

```bash
python check_spectrogram.py
```

Observed result: `EVEN_FOCK_MORSE_CHECK_PASS symbolic=7 numeric=87 stationary_axis_roots=20`.

The code does not enumerate infinitely many saddles or prove the universal parameter statements. The mathematical proof in `RESULT.md` does this by strict inequalities, monotonicity, and the global real-axis bound. Historical priority has been evaluated against the cited primary literature, not independently certified.
