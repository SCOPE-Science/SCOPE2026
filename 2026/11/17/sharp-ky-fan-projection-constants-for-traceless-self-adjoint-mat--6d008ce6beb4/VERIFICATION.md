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
# Reproducible checks and their limits

Execute `python3 check_kyfan.py` with Python 3 and no third-party packages. The checker enumerates every signed support of size \(k\) in the dual polytope for dimensions \(2\) through \(10\). It uses exact fractions, tests explicit primal equality for both active branches, and verifies the nonexpansivity classification through order \(15\).

Successful diagnostic output:

```
DUAL_POLYTOPE_SIGN_SUPPORT_CASES_PASSED 54
EXPLICIT_PRIMAL_EXTREMIZERS_AND_THRESHOLD_CASES_PASSED 54
COMPLETE_NONEXPANSIVITY_CLASSIFICATION_PASSED 14
ALL_EXACT_KY_FAN_CENTERING_DIAGNOSTICS_PASSED
```

The mathematical proof in `RESULT.md` establishes the theorem for every integer \(n\ge2\), \(1\le k\le n\), including the fact that the trace-centering projection is globally minimal; the finite checks are supplementary. No independent audit or external formal certification has been performed.
