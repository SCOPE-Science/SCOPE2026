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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 with only its standard library. The program reconstructs the two phase matrix exponentials by Taylor series with scaling and squaring, multiplies the resulting matrices, obtains the dominant eigenvalue from the characteristic quadratic, and checks the closed Floquet formula at seven periods and eleven duty fractions for ten distinct parameter sets. It checks unique duty minimization and strict period growth on the same grid, and evaluates a positive critical-period example and its two exact duty boundaries.

Observed output from the actual embedded-source run:

```text
PASS: 1679 finite direct matrix/duty/period checks
Example: critical period 4.182730782489124; duty range at T=2: (0.239703586223990, 0.760296413776010)
```

The mathematical identity, period monotonicity, critical period uniqueness, square-root boundary law, and nonlinear comparison statement have separate analytic proofs in `RESULT.md`. The finite checks do not certify these statements for all parameters, and they are not an external audit.
