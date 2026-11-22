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

The exact finite checker `check.py` was run in Python with SymPy and passed 218 exact symbolic, rational and characteristic-polynomial checks. Its domain of explicit matrix checks is at most eight rows; the general proof is mathematical and does not rely on enumerating all sizes.

The analysis covers consistent systems, exact block projection, every partition into exactly three nonempty blocks, all nonnegative probabilities and every integer number of equations at least four. Numerical performance, per-flop performance, and multi-step optimality have not been evaluated. Independent mathematical review is not yet performed.
