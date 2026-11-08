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

# Reproducibility and limits

Run `python3 verify.py` in a directory containing this document and the embedded checker to reproduce the test `VERIFY_OK 301 exact rational assertions` using only the Python standard library. The checker compares complete neighbor-choice enumeration against matching-polynomial coefficient extraction on 16 finite simple regular graphs, and verifies exact moments and recovered parameters. The test covers a 3-regular Petersen graph with 59,049 directed-choice assignments, alongside other connected and disconnected hosts.

The all-parameter proof is the independent event/matching inclusion-exclusion derivation in RESULT.md. These finite enumerations are corroboration, not a proof for arbitrary order. No independent audit is claimed. Statistical estimation error, nonregular graphs, and dependent choices are not addressed.
