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

## Reproducibility

The exact model is specified in `RESULT.md`. Execute `python3 checker.py` with Python 3 and its standard library. It uses seeded finite-difference Robin boundary-value solves and independent scalar golden-section optimizations, comparing both to the analytic formula at 100 parameter choices each. It also checks parameter regions above and below the exact allocation threshold and several boundary-launch identities. The completed check reported 100/100 numerical boundary solves with maximum absolute deviation under \(4.1\times10^{-7}\), 100/100 independent scalar optimizations within \(3.4\times10^{-16}\), and all 30 threshold checks plus the 3030 sampled-allocation checks. No outside dataset or precomputed output file is required.

## Limits

Finite mesh calculations verify finite instances and convergence consistency, not global analytic correctness. The global claims use the exact Robin formula, the derivative-sign proof and the threshold identity documented in `RESULT.md`. Independently reproducing the analytical argument and checking the complete priority literature remain open tasks.
