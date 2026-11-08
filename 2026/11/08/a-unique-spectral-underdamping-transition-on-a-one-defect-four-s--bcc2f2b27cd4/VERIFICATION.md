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

The included `verify.py` is the complete checker. It constructs the original \(4\times4\) rate generator rather than taking the reduced cubic as input, and tests the exact characteristic polynomial, discriminant, shifted coefficients and singular-limit polynomials. Independent floating-point generator diagonalizations compare 52 noncritical parameter points against the analytic sign classification; six additional threshold substitutions are checked.

Reproduce with `python verify.py` using Python 3.10 or later, SymPy 1.11 or later and NumPy 1.22 or later. The checker writes diagnostic messages to standard output. Exact root uniqueness and the singular limits are proved in RESULT.md; sampling cannot establish either universal statement. No external scientific certification or independent audit has been performed.
