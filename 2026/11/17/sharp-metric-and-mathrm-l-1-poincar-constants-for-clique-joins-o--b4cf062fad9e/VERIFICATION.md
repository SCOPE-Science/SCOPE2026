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

# Verification of exact constants and cut extrema

The proof in RESULT.md establishes the statements for every integer \(m\ge3\) and \(c\ge1\). The accompanying `checker.py` is a supplementary exact-rational diagnostic covering \(90\) parameter pairs, \(43{,}290\) nontrivial cut triples, and \(409{,}545\) individual triangle inequalities for explicit metric witnesses. Execute with `python3 checker.py`; it uses only the standard library.

Recorded successful output:

```
JOINED_BICLIQUE_EXACT_OK 90 parameter pairs; 43290 exact cuts; 409545 triangle inequalities
```

The code does not certify the universal inequality, independence of the claim from older work, or any external audit. Those limits are explicit; no computer experiment is substituted for proof.
