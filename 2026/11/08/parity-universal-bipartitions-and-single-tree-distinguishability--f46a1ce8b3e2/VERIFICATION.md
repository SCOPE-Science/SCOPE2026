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

The theorem is proved directly in `RESULT.md`, without requiring external numerical evidence. A reproducible, independent of the proof-text, exact rational check is included as `check_parity.py`. It enumerates the actual finite tree-growth chains for all walk lengths \(0,1,2,3\) and all sizes \(2\le n\le6\), checks probability normalization, and compares every bipartition distribution to Eulerian or discrete-uniform formulas. The executed script reported 612 exact finite-state checks passed, with no floating-point operations required for the probabilities. The proof of the asymptotic unlabelled total-variation bound uses only the explicit second-moment identity and counting, and is not inferred from finite enumeration. Independent external mathematical validation has not been performed.
