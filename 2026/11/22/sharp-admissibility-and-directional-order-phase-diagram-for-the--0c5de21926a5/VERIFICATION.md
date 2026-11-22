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

## Reproducibility

The theorem is established by the exact differentiation and extremization identities in `RESULT.md`. Run `python3 checker.py` from the directory containing the embedded files to reproduce the finite numerical cross-checks of the derivative envelope and illustrative boundary examples. The checker is deterministic and uses only Python's standard library. Its finite grids do not claim to prove the universal result.

## Limits

The model applies to strictly interior shape parameters \(0<a_i<1\), nonzero exponents \(b_i\), and the canonical power-mean formula. No outside mathematical audit has been performed.
