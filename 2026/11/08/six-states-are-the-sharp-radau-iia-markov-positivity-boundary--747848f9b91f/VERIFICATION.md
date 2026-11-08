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

# Reproducibility and verification

Run the complete dependency-free script with a standard Python 3 interpreter:

```
python artifacts/verify_radau_markov.py
```

Expected result begins with `VERIFY_OK`. It checks the exact-rational six-by-six matrix formula for 14 prescribed rational steps, 504 entry equalities, 14 row-sum equalities, the first six series coefficients, one rational isolating interval for the unique positive root, and four exact sign witnesses. Independently, exact symbolic polynomial simplification was performed for five transient Jordan-derivative identities and five absorbing-column complement identities. The monotonicity of the boundary polynomial and the universal generator statement are proved in `RESULT.md`; neither can be inferred solely from the finite checker. The local positivity result has generator-dependent neighborhoods; no positive universal step-size bound is claimed.

Independent mathematical audit has not been performed.
