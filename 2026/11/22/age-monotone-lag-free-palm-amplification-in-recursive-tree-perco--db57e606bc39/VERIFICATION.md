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

The analytical proof uses two exact moment recurrences for the retained root-cluster size and one conditional-expectation propagation identity. The positivity and strict-age comparison follow from an explicit rational multiplier; no simulation is used to infer the infinite statement.

The standalone script `verify.py` enumerates all parent choices and all edge-retention patterns for the indicated finite sizes, including exact rational checks at \(p=1/3\), \(p=1/2\), and \(p=2/3\). It passed 145 assertions. These tests validate small cases but do not replace the all-index proof.

No independent audit has been performed. Publication priority beyond the inspected sources is not independently certified.
