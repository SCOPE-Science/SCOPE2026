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

# Reproduction and evidence boundaries

Run `python3 verify.py` in the directory containing `RESULT.md`. This Python 3 checker uses only the standard library and replays independent direct vertex support calculations, extrema witnesses, angular counting, and critical local-area identities. Its output in this review was:

```
PASS: 20032 supplemental deterministic assertions
```

The exact distribution follows from the analytical support-function and spherical-folding derivation in `RESULT.md`. The two endpoint limits require compact localization plus explicit Taylor expansions, and the crossover limits use first-order separation of competing contact families. Finite testing does not prove a continuum asymptotic. Historical originality is compared in `REVIEW.md` and `AUDIT.json`, and remains provisional. No independent review, certification, or general-purpose proof assistant has been performed.
