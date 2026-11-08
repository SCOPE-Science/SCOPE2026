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

# Reproducibility and mathematical boundaries

The proof requires four symbolic identities: the imaginary-axis modulus formula, two endpoint disks, the tangency algebra at \(A+B=2\), and the exact factorization. The first three yield a global upper bound; only the last shows that the bound holds across the **complete interval**. All one-sided boundaries are addressed by a separate local real-part constraint. A finite machine check by itself does not establish the infinite theorem.

`verify.py` runs entirely with Python's standard library and rational numbers. From the directory containing the source, run `python verify.py`; it terminates with `CHECKS_OK` and a count of exact equalities and inequalities tested. The rational suite includes mixed-sign and one-sided frequency bands, coefficient identities, endpoint saturation, interior stability, exterior failure, and the real-coefficient gain. No external data are required.

The hypotheses are \(a,b\geq0\), \(a+b>0\), first order, two stages, complex coefficients, and stability required at every imaginary frequency in the entire prescribed interval. There is no independent audit, no nonlinear or nonnormal stability claim, and no inference from finite tests to arbitrary real inputs.
