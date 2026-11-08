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

The proof uses base-change for direct summands, local constancy of rank, the locality of modular \(p\)-group algebras (proved by central-subgroup induction), and explicit polynomial trace calculations. These steps establish the full domain of the stated theorem without computational extrapolation.

The standalone `verify.py` program uses only standard Python. Running `python3 verify.py` exhaustively tests the \(\mathbb F_2[D_\infty]\) finite-support windows of Laurent exponents \(0\), \(-1\ldots1\), \(-2\ldots2\); every window has only the two trivial idempotents. It also multiplies the translation idempotent and verifies \(\sum_i s^i(-x^{p-1})=1\) over \(\mathbb F_p\) for \(p=2,3,5,7\). Success terminates with `VERIFY_OK`. These tests independently corroborate examples, but no bounded enumeration proves the universal classification. The bibliographical check of the complete 1985 Lorenz article remains open; its abstract was inspected.
