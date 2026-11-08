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

## Executable finite verification
Run `python3 verify.py` with Python 3 standard library. For every test pair it recomputes deletion sets directly, builds the graph without invoking the Type-A lemma, counts all unordered triangles, and verifies that every triple has exactly one required pivot and the claimed equal-junction alternation. It covers binary lengths 1 through 11, ternary lengths 1 through 7 and quaternary lengths 1 through 6. The binary closed expression is checked through length 24.

## Analytic checks and limits
The proof establishes the all-length result using the known Type-A characterization and an exhaustive interval-geometry case split. The computations do not certify infinite lengths or historical originality. There is no independently performed external audit. Originality may be affected by inaccessible or unindexed historical papers; in particular the 2001 founding paper was available at abstract level only.
