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

Run `python3 verify_near_biclique.py` under Python 3 (standard library only) after extracting the files from this finding package. The checker verifies exact rational cut inequalities and equality sets for every integer shore size `2 <= m <= 12` at four rational heat factors, constructs graph heat independently by direct numerical ODE evolution, and checks 5,760 deterministic-seed real-signal inequalities. Output:

```
EXACT_RATIONAL_ALL_CUTS_AND_EQUALITY_CLASS_PASS
INDEPENDENT_HEAT_ODE_AND_ROW_STOCHASTICITY_PASS
RANDOM_REAL_SIGNAL_TV_L1_CHECKS_PASS 5760
ALL_NEAR_BALANCED_BICLIQUE_HEAT_CHECKS_PASS
```

Finite tests do not certify the infinite range of sizes and positive times. The spectral and integer cut inequalities in RESULT.md establish that range. No independent audit is reported.
