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

Run `python3 checker.py` with Python 3.9+ and the standard library. The script requires no external data, dependencies or random seed. It enumerates \(1,4,64,4096\) loopless labelled directed graphs on \(1,2,3,4\) vertices and directly compares both all-valuation box commutation and the relation-product identity. It checks exact first moments of absence-of-common-neighbor counts at \(p=1/2\), and exact two-sided absence counts. Successful execution prints `TENSE_COMMON_NEIGHBOR_EXHAUSTIVE_OK`.

# Verified scope and limitations

These finite checks do not certify a general limiting distribution. The infinite claim is supported by the separate displayed uniform fixed-order intersection estimate and factorial-moment argument in RESULT.md. Independence of arcs and fixed-\(c\) scaling are essential assumptions. No independent audit was performed.
