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

The variance formula follows from conditioning on four equiprobable hub states, taking two exact moments, and subtracting their squares. The strict transfer inequality is proved analytically by splitting the hub imbalance into the ranges \(0\le d\le4\) and \(d\ge4\), using \(0<B\le A\le1/8\).

To reproduce the independent finite checks, run `python3 verify.py` using Python 3.9 or newer. The checker enumerates all site-retention configurations for every pair of hub-leaf counts on up to 12 vertices, separately calculates pairwise indicator covariances, and verifies exact rational equality with the closed expression. It also tests the rational transfer identity on a finite parameter grid and checks predicted minimizers and maximizers up to 120 vertices. Actual check output: `VERIFY_OK 5263`. These computational checks are finite and cannot alone establish the all-parameter theorem. Independent audit has not been performed.
