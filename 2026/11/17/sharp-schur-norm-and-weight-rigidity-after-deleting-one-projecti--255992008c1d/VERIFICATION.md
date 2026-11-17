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

# Verification and reproducibility

The proof uses exact incidence counts, a three-eigenspace Gram diagonalization, the trace-dual extremal formula and the strict-concavity critical equation; these arguments, not any test sample, establish all prime-power cases. The finite checker constructs prime-field incidence matrices independently and compares their singular values with the claimed eigenvalue multiplicities. It runs with Python 3, NumPy and SciPy: `python CHECKER.py`.

The finite checks cover orders 2, 3, 5 and 7 (16 weights), plus numerical optimizers at those orders and asymptotic probes at 31, 101 and 503. These checks are not exhaustive for larger finite fields and cannot establish an infinite theorem by themselves. The proof includes its own analytic justification for the full range. Independent validation has not been performed.
