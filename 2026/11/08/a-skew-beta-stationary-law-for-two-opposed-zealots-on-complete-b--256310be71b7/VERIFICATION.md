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
# Reproduction and proof check

The mathematical proof is in `RESULT.md`. `verify.py` independently enumerates labeled neighbor-copy transitions and confirms the reduced four-rate generator, exact drift and quadratic-variation identities in rational arithmetic for six sizes. It solves the stationary linear equations exactly for five small sizes, verifying the finite means and zero mass at the transient corner, and compares finite stationary moments to the proposed beta limit for three larger bipartite examples. Run `python verify.py` with Python >=3.9, SymPy, NumPy and SciPy. The checks are finite and do not replace the analytic convergence argument. No separate independent human or external scientific audit has been conducted.
