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

Run `python3 verify.py` with Python 3 standard library. The program independently compares signature equivalence with an explicitly evaluated two-round game on all pairs of words of length at most five; enumerates all binary words through length eleven; checks compressed subsequences; and verifies the extremal construction for alphabet sizes one through nine. Its output begins with `VERIFY_OK`. These are bounded tests only; the published argument proves all finite lengths and every alphabet size. No independent audit has been performed.
