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

Use Python 3 and run `python3 verify.py`; no third-party modules are required. The checker independently generates all proper optimum \((n-2)\)-colour partitions via restricted-growth colouring backtracking for \(n=5,6,7\), then computes open-neighbourhood witness multiplicities directly rather than using the tournament proof. It compares the complete defect histograms to the formulas after dividing named counts by \((n-2)!\). The result is:

```
EXHAUSTIVE_OPTIMAL_COLORINGS 5 {1: 20}
EXHAUSTIVE_OPTIMAL_COLORINGS 6 {3: 120, 6: 40}
EXHAUSTIVE_OPTIMAL_COLORINGS 7 {6: 1120, 9: 1120}
CONSTRUCTIVE_UPPER_BOUND_OK n=5..30
VERIFY_OK
```

The proof of the all-order assertions is the mathematical argument in `RESULT.md`; the finite tests neither exhaust arbitrary \(n\) nor establish historical priority. Independent mathematical audit: not performed.
