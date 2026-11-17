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

# Reproduction and verification

Execute `python3 check_exact.py` with Python 3, without third-party packages. The script enumerates every proper nonempty binary cut for each dimension \(2\le n\le16\); the exact rational comparison is by `fractions.Fraction`, not floating-point estimates. The 494 cases for \(2\le n\le8\) are the complete finite component of the proof. Analytic Steps 2–3 in `RESULT.md` handle infinitely many orders \(n\ge9\). The script also checks the explicit second-vertex witness for \(9\le n\le400\), which is a reproducibility check, not a substitute for the proof.

Checked program output includes:

```
EXHAUSTIVE_ALL_NONTRIVIAL_CUTS_N2_TO_N16_PASSED 131038
EXACT_SECOND_VERTEX_WITNESSES_N9_TO_N400_PASSED
ALL_HALF_LAZY_PATH_GINI_CHECKS_PASSED
```

No independent audit or external proof certification is claimed. The supplied script uses complete enumeration only in its explicitly bounded domain.
