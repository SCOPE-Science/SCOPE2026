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

# Verification

Run `python verify.py` using only Python's standard library. The script builds the exact rational graph Laplacian and independently computes the end-step operator by full rational matrix inversion, then compares it with the derived spectral resolvent formulas. It checks 1,176 complete matrices for all parts up to size five, seven positive rational \(\theta\) values, and seven nonnegative rational steps. It checks the Euler threshold, the strictly positive balance-comparison identity through total order 39, and the two exact Crank--Nicolson boundary examples at total order four.

Recorded result from this package's standalone code: `VERIFY_OK 1176 full exact-rational matrix cases; endpoint, ordering and boundary checks`.

These tests are deliberately finite. The mathematical proof of the formula for all positive part sizes, all real \(\theta\in[0,1]\), and all real steps is the algebraic spectral decomposition and quadratic sign argument in RESULT.md. Numerical instability, non-graph Laplacians, stage preservation, and claims about arbitrary weighted graphs are not certified.
