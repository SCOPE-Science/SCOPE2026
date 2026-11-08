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

The proof in `RESULT.md` is algebraic. To check its finite rational instances, install Python 3 and SymPy, extract the exact embedded `verify.py` next to `RESULT.md`, then execute:

```sh
python verify.py
```

A successful execution prints a line beginning `VERIFY_OK 342`. The script constructs symmetric nonnegative row-stochastic mobility matrices with exact rational entries, checks the infection projection identity and the two-dimensional quotient, and checks sharp and interpolated transverse decay rates for ordinary-group counts two through seven. It does not extrapolate finite checks to all group counts; the analytic spectral argument supplies that quantifier. No external validation or independent audit has been performed.
