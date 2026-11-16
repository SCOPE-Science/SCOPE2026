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

The standalone `CHECK.py` was executed using Python 3. The rational checks covered 44 \(m,r\) pairs and exactly verified every two-by-two determinant, the maximal trace inequality and the first-pair block identity. A separate direct complete complex synthesis-frame assembly for another 44 \(m,r\) pairs verified the full frame-operator entries against the block formulas. Ten dimensions were checked numerically against the unique stationary root and both neighboring tapers; a separate check confirms the \(m=2\) radical formula and convergence toward the sharp constant. Exact statements for all dimensions and parameters follow from the written proof, not the finite runs.

No independently executed external mathematical audit is recorded. This document reports only the described reproducible same-model calculations.
