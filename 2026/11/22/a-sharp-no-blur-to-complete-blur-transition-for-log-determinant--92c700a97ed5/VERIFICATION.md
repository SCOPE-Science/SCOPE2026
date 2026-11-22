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

The proof of the continuum theorem is in `RESULT.md`; finite checks are only supplementary. Using Python 3.11 or later, place `verify.py` next to this file and execute:

```bash
python3 verify.py
```

Expected output starts with `PASS: 4556 finite assertions`. The standard-library checker implements exact `fractions.Fraction` identities for the minimized quadratic and cleared derivative numerator, `decimal.Decimal` high-precision logarithms for a parameter grid, and an explicit certified-sign barrier example. There is no randomness, external data, network dependency or third-party package requirement.

The code tests neither every positive parameter nor all blur families. The all-parameter assertion is justified analytically by the derivative sign and endpoint-ratio argument in `RESULT.md`. The model assumes \(B>0\), \(\ell,d>0\), \(w\ge0\), and a compact blur interval. Independent mathematical audit and independent validation have not been performed.
