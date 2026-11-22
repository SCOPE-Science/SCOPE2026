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

The analytic proof in `RESULT.md` is the source of the asymptotic statements. The machine-assisted diagnostics run with Python 3, NumPy, and SciPy using the self-contained `checks/width_tail_checker.py` artifact:

```
python checks/width_tail_checker.py
```

The program output observed on the supplied package path was `WIDTH_TAIL_CHECKS_OK 1248`. Tests compare direct support maxima with the folded formula over 600 independently seeded spherical directions for six separations, verify the stated extreme widths, check the analytic crossover profile and its monotonicity, and compare exact folded-coordinate quadratures to asymptotic coefficients for fixed and moving separations. All assertions completed successfully. Exact finite quadratures only confirm the asymptotic formulas numerically at small positive deficits; no extrapolation from those finite tests is used as a proof. The limiting proof uses the exact surface-coordinate density, rigorous event localization, uniform Taylor estimates and the measure-zero boundary of the rescaled domain.

There is no independent mathematical audit or external certificate. The work does not establish historical priority, a global-in-parameter error estimate, or width distributions for arbitrary disk arrangements.
