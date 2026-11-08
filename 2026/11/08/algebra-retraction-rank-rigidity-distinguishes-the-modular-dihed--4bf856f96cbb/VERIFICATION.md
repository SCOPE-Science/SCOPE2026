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

Run `python verify.py` with Python 3 and the standard library; no extra packages or data files are required. The verifier builds the multiplication tables for the two group presentations, performs full enumeration of their augmentation-one generator images over \(\mathbb F_2\), retains those obeying all group relations, and checks the idempotent identity on both generators. It then computes full image ranks. Independent field-arithmetic enumeration checks radical square-zero cones over \(\mathbb F_2\) and \(\mathbb F_4\).

The expected exact output is `idempotent_maps D8 GF2 {1: 1, 2: 64, 8: 1}`, `idempotent_maps Q8 GF2 {1: 1, 8: 1}`, plus zero-cone counts: D8 at \(q=2\): \((16,32)\), D8 at \(q=4\): \((256,1536)\), Q8 at \(q=2\): \((16,0)\), and Q8 at \(q=4\): \((256,0)\), with the pair denoting elements in \(C\) and outside \(C\). The program asserts these checks and finishes with `VERIFY_OK`.

General finite-field formulas and arbitrary-characteristic-two rigidity are established by the algebraic proof; this script does not exhaust infinitely many coefficient fields. Independent mathematical validation has not been performed.
