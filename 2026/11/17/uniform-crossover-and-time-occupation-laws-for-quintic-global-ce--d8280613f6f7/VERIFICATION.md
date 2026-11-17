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

# Reproduction and limits

Install Python 3 with `sympy` and `scipy`; run `python verify_crossover.py`. The recorded execution on the supplied program printed:

```
CHECK_OK energy, beta endpoint, monotonicity, large-q limit,
18 finite-amplitude universal brackets, 16 kernel ratios
```

The symbolic computation checks the exact derivative of the conserved energy. Numerical checks evaluate the exact quadratures for representative parameters, verify the Euler beta endpoint and a moderate large-parameter approximation, and test the proven all-scale inequality at 18 parameter choices. Symbolic differentiation and real-analysis inequalities in `RESULT.md`, not these finite samples, establish the statements for all parameters. A finite-precision integration cannot prove monotonicity or weak convergence. The original-time normalization is specified in `RESULT.md`; no external verification or independent audit has been carried out.
