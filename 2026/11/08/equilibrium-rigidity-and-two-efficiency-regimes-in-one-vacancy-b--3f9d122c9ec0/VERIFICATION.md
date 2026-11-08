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

# Reproducible checks and boundaries

Run `python3 verify.py` with Python 3 standard library only. The script independently enumerates every red/blue/vacant placement and directly evaluates strict utility-improving jumps using exact rational arithmetic, without referring to the analytical structural lemma.

Observed output:

```
CENSUS_OK instances=80 assignments=15136
POA_FAMILY_OK instances=4
BALANCED_FAMILY_OK instances=4
```

The census covers all \(2\le a,b\le5\) and all population splits with both colors nonempty. The sharp-welfare family was additionally checked for \(3\le a\le6\), and the balanced family for \(2\le m\le5\). The argument in `RESULT.md` proves all integer parameters; exhaustive finite checks alone do not establish the general claim. The independent external audit status is unperformed, and no external proof certification is claimed.
