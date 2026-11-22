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

The exact reproducibility command is `python3 check.py` with Python 3 and its standard library. It passed 10,792 exact arithmetic assertions: 190 direct Delannoy modulo-five comparisons; 9,998 positive-lag bound/equality assertions; 14 lag-sum and small-correlation identities; and 590 real/imaginary normalized block comparisons. The latter are complete evaluations of those finite blocks only. The infinite theorem follows from the stated Lucas-digit, aligned-block and rational-recursion arguments. A separate external mathematical audit has not been performed.
