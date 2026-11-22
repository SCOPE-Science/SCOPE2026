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

The theorem is proved analytically in `RESULT.md`, with its full parameter domains and equalities. `checker.py` (Python standard library only) provides finite cross-checks, including independently discretized \(L^2\) integrals, the Fourier geometric-series formula, optimal-angle tests, the exact two-component stationary radius, the three-component critical identities, numerical uniform bounds for four or more sources, and one-sided critical scaling.

Run `python3 checker.py` in the same directory as the other files. The observed result was:

```
PASS: 10802 finite diagnostics; analytic proof required for all-parameter conclusions
```

Numerical quadrature and finite mesh inequalities do not certify a continuous or infinite family. The proof in `RESULT.md` supplies those quantifiers; the finite tests are not substituted for its monotonicity and global inequality steps. The classification covers only the defined symmetric model and population squared-error criterion. Independent mathematical review has not been performed.
