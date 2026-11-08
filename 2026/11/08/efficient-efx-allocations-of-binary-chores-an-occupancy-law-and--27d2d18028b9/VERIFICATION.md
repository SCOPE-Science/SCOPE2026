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

# Verification and limits

Run `python3 verification.py` (Python 3 standard library; no network or data dependencies). The program independently enumerates labeled allocations and checks Pareto dominance via cost vectors and EFX via actual removal of each owned item. It then compares the resulting counts with the candidate formula, including boundary cases with empty bundles and zero-cost chores.

Observed verification: 174 instances, 81,620 enumerated complete allocations; eight two-agent parity comparisons; 176 symmetric occupancy-identity parameter combinations. All assertions passed. The verifier checks finite instances; it does not certify the infinite theorem or the Gaussian asymptotic, which follow from the written algebra, multinomial limit theorem, and Stirling's formula. Independent external audit has not been performed.
