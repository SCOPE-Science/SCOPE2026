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
# Verification

`CHECK.py` is a standalone Python 3 script requiring only its standard library. Run `python3 CHECK.py` in the same directory as this file. It builds the two-interface signal using exact integer rankings, applies perturbations of \(1/4\) and \(2/3\), and verifies the claimed sharp ratio for radii \(1\) through \(16\) at cycle lengths \(8r\), \(8r+1\), and \(10r+3\). It also samples 2,400 rational signal pairs over shorter admissible cycles to corroborate the upper bound. The observed terminal lines were:

```
EXACT_SHARP_MEDIAN_WITNESSES_PASSED 96
RATIONAL_BV_PERTURBATION_UPPER_CHECKS_PASSED 2400
ALL_RUNNING_MEDIAN_BV_CHECKS_PASSED
```

Finite sampling cannot establish an all-input operator bound. The universal argument is the order-statistic interval bound plus cycle edge-counting. The critical lower-bound certificate is the explicit median rank interlacing in `RESULT.md`; the diagnostic program reconstructs it without external data. Publication-priority limitations are noted in `REVIEW.md`.
