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

# Verification and scope

The proof in `RESULT.md` establishes the all-length inequality and its sharpness without relying on finite computation. The supplied `checks/verify_mad.py` is a standalone standard-library Python program requiring Python 3.9 or later, executed as:

```sh
python checks/verify_mad.py
```

Expected final marker: `ALL_MOVING_MAD_WEIGHTED_BV_CHECKS_PASS`.

The program tests the median-of-deviations/minimum-distance identity for sample lengths 3 through 26, creates an exact single-edge jump witness for every input edge at 90 independently chosen positive rational weight profiles per length, performs random two-input inequalities using the same weights, and checks the unweighted transition law. All comparisons of the exact sharp witness quotients use rational arithmetic.

The theorem requires real data, full three-sample windows, arbitrary *positive variation weights*, and the unscaled MAD. It does not assert numerical finite testing proves the universal theorem or claim independent external audit.
