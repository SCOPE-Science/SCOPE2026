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
Run `python3 verify_period_doubling_mus.py` using Python 3 with no external packages. The checker regenerates \(D_k\) for integer orders \(3\leq k\leq10\), computes every suffix-pair common-prefix length, enumerates all minimal unique substrings by exact suffix uniqueness thresholds, tests the four stated occurrences, and verifies the companion-prefix identities for every relevant offset. All eight tests passed. This computation corroborates, but cannot replace, the unlimited mathematical proof in `RESULT.md`. The script and its dependencies are entirely within the present package.
