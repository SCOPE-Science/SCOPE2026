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

# Verification notes

Execute `python3 verify.py` using Python 3 and only its standard library. The program performs 5761 exact assertions with rational fractions and reports `VERIFY_OK_EXTENDED 5761 exact assertions`. It checks the exact one-tree transition and moments through size 10, paired count laws through size 10, exhaustive independent attachment histories for size at most 6, all cross-time moment identities for fork times through 8 and observation times through 10, upper-tail association inequalities in enumerated ranges, and conditional regression through size 12.

The model counts outdegree-zero rooted terminal vertices. It does not count a root of degree one as terminal. Exact finite enumeration is not evidence for the general joint Gaussian limit, for which the accompanying proof checks the martingale quadratic variation and bounded-increment Lindeberg condition. Source comparisons concern actual inspected material and do not establish worldwide historical uniqueness. No independent review was conducted.
