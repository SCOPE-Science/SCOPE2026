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

# Verification notes

`verify.py` was run with Python, NumPy, and SymPy; the program printed `VERIFY_OK`. It exactly checks the Schur block expression, the hard-pupil idempotence, and the soft-pupil polynomial identity using symbolic parameters. With seed 8119 it checks 160 independent random complex-circulant cases with nontrivial Fourier masks and 480 positive-leakage instances; numerical comparisons include the one-step optimal GMRES squared residual, the geometric minimum over mask-restricted physical states, exact positive-leakage termination, and singular-value condition numbers.

The analytic proof in RESULT.md—not floating-point tests—establishes all dimensions, arbitrary data, all iteration orders, and the flexible mask-range quantification. Exact physical transfer masks, exact arithmetic, and a fixed omitted-frequency subspace are essential. Neither an independent mathematical audit nor physical optical experiments have been performed.
